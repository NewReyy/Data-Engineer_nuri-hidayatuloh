# Menggunakan image Python versi ringan
FROM python:3.11-slim

# Mengatur working directory di dalam container
WORKDIR /app

# Menyalin requirements file dan menginstall dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Menyalin seluruh kode aplikasi ke dalam container
COPY . .

# Perintah default ketika container dijalankan
CMD ["python", "etl.py"]
