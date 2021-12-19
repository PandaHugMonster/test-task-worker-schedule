FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8005"]