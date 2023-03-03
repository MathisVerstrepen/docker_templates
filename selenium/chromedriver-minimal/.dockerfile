# sudo docker build -t selenium_chrome:latest -f .dockerfile .

FROM python:3.11.2-alpine

RUN apk add --no-cache \
        chromium \
        chromium-chromedriver \
        # gcc \
        # libc-dev \
        # g++ \
        # libstdc++ \
        && \
    rm -rf /var/cache/apk/*

ENV DISPLAY=:99

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python", "main.py"]