FROM python:3.8-slim-buster
 
# 사용자 지정
USER root

ADD . /service-simple-rest-server

# 작업 디렉토리로 이동
WORKDIR /service-simple-rest-server

COPY requirements.txt .

#RUN apt-get update && apt-get -y install gcc
RUN python -m pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 24573

CMD python app.py
# CMD python app_grpc.py
#CMD ["/bin/sh"]