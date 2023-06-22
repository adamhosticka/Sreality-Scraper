FROM python:3.10

WORKDIR /server

RUN apt-get update && apt-get install -y \
    postgresql \
    libpq-dev

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "./app.py"]
