FROM python:3.10.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY YangJamurJamuraja_v2.h5 YangJamurJamuraja_v2.h5

COPY main.py main.py

ENV PYTHONNUNBUFFERED-1 

ENV HOST 0.0.0.0

EXPOSE 8001

CMD [ "python", "main.py" ]