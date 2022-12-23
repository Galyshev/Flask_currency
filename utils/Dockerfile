# syntax=docker/dockerfile:1

FROM python:3.9-alpine
WORKDIR /flask_currency_dkr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "Flask_currency.py"]

# команда для запуска
# docker build ./utils/ -t doker_flsk
