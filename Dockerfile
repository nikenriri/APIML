FROM python:3.10.8

ENV PORT 8001
ENV HOST 0.0.0.0

EXPOSE 8001

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "main.py"]
