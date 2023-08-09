FROM python:3.11


COPY . .

WORKDIR .

RUN pip install -r /requirements.txt
