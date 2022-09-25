FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

RUN apt-get update
RUN apt install -y vim 
RUN pip install requests