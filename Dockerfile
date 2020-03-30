FROM python:3-slim-buster

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app

WORKDIR /app

CMD ["python3","app.py"]