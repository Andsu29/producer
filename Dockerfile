FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r src/requirements.txt

CMD ["python", "src/main.py"]
