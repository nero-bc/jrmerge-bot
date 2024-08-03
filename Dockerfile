FROM python:3.11

WORKDIR /usr/src/mergebot
COPY . /usr/src/mergebot

RUN pip install --upgrade pip
RUN python -m venv venv && venv/bin/pip install --no-cache-dir -r needs.txt

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y git wget curl pv jq ffmpeg neofetch mediainfo \
    && apt-get clean 

    
EXPOSE 8080

COPY . .

RUN chmod +x start.sh

CMD ["bash", "start.sh"]
