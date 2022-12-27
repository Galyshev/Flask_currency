# syntax=docker/dockerfile:1

FROM python:3.9-alpine
WORKDIR /flask_currency_dkr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# команда для запуска (не актуальна)
# docker build ./utils/ -t doker_flsk
