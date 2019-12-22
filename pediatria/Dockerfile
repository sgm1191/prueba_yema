FROM python:3.7
ENV PYTHONBUFFERED 1    

RUN mkdir /code
WORKDIR /code

ADD . /code
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt