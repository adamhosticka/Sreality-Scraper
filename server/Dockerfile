FROM python:3.10

WORKDIR /server

RUN apt-get update && apt-get install -y \
    postgresql \
    libpq-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python3", "./main.py"]
