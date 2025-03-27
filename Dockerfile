FROM python:3.13-slim
WORKDIR /app
COPY app.py app.py
CMD ["python3", "app.py"]