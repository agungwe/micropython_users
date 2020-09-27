FROM python:3.8.5-alpine

WORKDIR /app

COPY ./virtualenvi ./

ADD . /app

RUN pip install -r req.txt

CMD ["flask","run"]