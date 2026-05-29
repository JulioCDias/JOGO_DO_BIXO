FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Install Python deps (minimal set from pyproject)
RUN pip install --upgrade pip
RUN pip install django django-cors-headers djangorestframework django-filter djangorestframework-simplejwt markdown psycopg2-binary python-dotenv

COPY . /code

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
