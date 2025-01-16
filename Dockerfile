# Python 3.12 Slim 버전 기반
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 종속성 복사 및 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# 추가적인 Python 패키지 설치
COPY setup.py ./
RUN pip install .

# 소스 코드 복사
COPY . .

# 기본 실행 명령
CMD ["python", "main.py"]