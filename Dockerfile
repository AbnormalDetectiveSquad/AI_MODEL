# Python 3.12 Slim 버전 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pip 업그레이드 및 필수 패키지 설치 (한 RUN 명령어로 통합)
RUN pip install --no-cache-dir numpy && \
    pip install --no-cache-dir pytz && \
    pip install --no-cache-dir python-dateutil && \
    pip install --no-cache-dir scipy && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir scikit-learn && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
# 소스 코드 복사
COPY . .

# 기본 실행 명령
CMD ["python", "main.py"]