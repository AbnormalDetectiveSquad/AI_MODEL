
## 요약

*   **파이썬 3.12-slim 기반:** 최신 파이썬 버전과 slim 이미지를 사용하여 작동 테스트
*   **Docker 이미지 빌드:** 다음 명령어를 사용하여 Docker 이미지를 빋드 후 작동 확인 (Docker version 27.5.0, build a187fa5)
*    빌드된 이미지 크기가 14.2GB로 다소 큰 편 입니다
    ```bash
    docker build -t ai_model .
    ```

## 폴더 구조
AI_MODEL/
├── Dockerfile          # Docker 이미지 빌드 설정 파일       
├── LICENSE              # 원본 모델 라이선스 파일       
├── main.py             # 메인 실행 스크립트       
├── model/              # 모델 관련 코드 디렉토리       
│   ├── ID_sort.csv       # 링크 정렬정보        
│   ├── Sample.csv        # 샘플 데이터       
│   ├── __init__.py       # 파이썬 패키지 표시 파일       
│   ├── adj_matrix.npz     # 인접 행렬 데이터 (NumPy 저장 형식)       
│   ├── gangnamgu_with_weakday.pt   # 학습 가중치       
│   ├── layers.py          # 모델 레이어 코드       
│   ├── models.py         # 모델 구조 코드       
│   └── utility.py         # 유틸리티 함수 코드       
├── requirements.txt    # 필요한 파이썬 패키지 목록 파일       
└── setup.py         # 파이썬 패키지 설치 설정 파일. 'ai_model' 패키지를 설치하고, 'ai_model' 명령어를 'main:calculattion_data'에 연결.       
