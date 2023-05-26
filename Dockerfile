FROM ubuntu:latest

RUN apt-update && apt install -y python3-pip
WORKDIR /app

COPY . .
#COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ['pytest', 'test_pipeline.py']