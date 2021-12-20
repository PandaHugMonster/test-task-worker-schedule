FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app/requirements.txt /app
RUN apt update -y && apt install -y jq
RUN pip install -r requirements.txt
COPY . /app
