# sudo docker build -t selenium_firefox_full:latest -f .dockerfile .

FROM python:3.11.2

# Install Firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update && \
    apt-get install -y --no-install-recommends firefox

# Download geckodriver
RUN wget -O /tmp/geckodriver.tar.gz $(curl -sSLI -o /dev/null -w '%{url_effective}' https://github.com/mozilla/geckodriver/releases/latest | awk -F/ '{print "https://github.com/mozilla/geckodriver/releases/download/"$NF"/geckodriver-"$NF"-linux64.tar.gz"}')
RUN tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/

ENV DISPLAY=:99

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python", "main.py"]
