import torch
import torch.nn as nn

from model import layers
class STGCNChebGraphConv_OSA(nn.Module): #필요
    def __init__(self, args, blocks, n_vertex):
        super(STGCNChebGraphConv_OSA, self).__init__()
        modules = []
        for l in range(len(blocks) - 3):# ST블록 배치 앞 1 뒤2 블록 갯수를 고정이라고 가정해서 3개를 뺸 나머지레 반복문으로 ST 블록을 배치함
            modules.append(layers.STConvBlock(args.Kt, args.Ks, n_vertex, blocks[l][-1], blocks[l+1], args.act_func, args.graph_conv_type, args.gso, args.enable_bias, args.droprate))
        self.st_blocks = nn.Sequential(*modules)
        Ko = args.n_his - (len(blocks) - 3) * 2 * (args.Kt - 1) #ST블록 통과 후 시간축 크기 구하기
        self.scaleconv = nn.Conv2d(
            in_channels=(blocks[-3][2]),
            out_channels=blocks[-2][1],  # 원하는 아웃 채널 수로 변경
            kernel_size=1,
            stride=1,
            padding=0,
            bias=True)
        self.Ko = Ko #시간축 크기 저장
        if self.Ko >= 1: #시간축 크기가 1보다 크면 정규화 레이어를 통해 FC 레이어로 넘김
            self.output = layers.OutputBlock_OSA(Ko, blocks[-3][-1], blocks[-2], blocks[-1][0], n_vertex, args.act_func, args.enable_bias, args.droprate,args) #출력 블록 생성
        elif self.Ko == 0: #시간축 크기가 0이면 바로 FC 레이어로 넘김
            self.fc1 = nn.Linear(in_features=blocks[-3][-1], out_features=blocks[-2][0], bias=args.enable_bias)
            self.fc2 = nn.Linear(in_features=blocks[-2][0], out_features=blocks[-1][0], bias=args.enable_bias)
            self.relu = nn.ReLU()
            self.dropout = nn.Dropout(p=args.droprate)

    def forward(self, x):
        features = None
        # 각 ST block의 출력을 저장
        for block in self.st_blocks:
            x = block(x)
            if features is None:
                features = x
            else:
                features = torch.cat([features, x], dim=2)

        features = self.scaleconv(features)
        features= features.permute(0, 2, 3, 1)
        x = self.output(x,features) 
        return x
 