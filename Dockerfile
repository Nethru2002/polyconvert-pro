FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libmagic1 \
    ffmpeg \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Run the CLI version
ENTRYPOINT ["python", "main.py"]