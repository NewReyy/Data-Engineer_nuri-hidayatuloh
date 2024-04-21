# Resume Data Engineering in the Cloud

## Mengapa perlu untuk belajar mengenai materi ini?
Dikarenakan yang pertama banyak digunakan di Industri dan salah satu skill yang dibutuhkan untuk menjadi Data Engineer.

## Keunggulan menggunakan Cloud dalam Data Engineering
Keunggulan menggunakan Cloud dalam Data Engineering yakni menjadi lebih efisien, cocok digunakan untuk dataset yang ukurannya besar, dan yang terakhir bisa untuk berkolaborasi dengan mudah.

## Contoh Teknologi Cloud untuk Data Engineering
Contoh Teknologi Cloud untuk Data Engineering meliputi: 
- Google Cloud Storage
- Google BigQuery
- Amazon Redshift
- Google Cloud Composer

## Google Storage
Google Storage merupakan layanan yang dapat digunakan sebagai media penyimpanan file dengan berbagai format.

### Penggunaan Google Storage
Penggunaan Google Storage meliputi: 
- Mengunggah file (upload)
- Mengunduh file (download)

### Set Up Awal pada Google Storage
1. Mengunjungi laman [Firebase](https://firebase.google.com/)
2. Sign in menggunakan akun Google
3. Buka Console
4. Buat Project & Disable Google Analytics
5. Ubah Rules pada Storage
6. Generate Private Key dan simpan kedalam project lokal dan rename menjadi accountKey.json
7. Install dependencies firebase-admin

### Cara Upload File ke Google Storage
```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('/path/to/accountKey.json')
firebase_admin.initialize_app(cred, {"storageBucket": "your-bucket.appspot.com"})

bucket = storage.bucket()
blob = bucket.blob(blob_name='test.csv')
blob.upload_from_filename("test.csv")
```

### Cara Download File dari Google Storage
```python
# download.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Ganti ini dengan path ke file accountKey.json Anda
cred = credentials.Certificate("/your/path/to/accountKey.json")

# Ganti ini dengan nama bucket Firebase Storage proyek Anda
firebase_admin.initialize_app(cred, {"storageBucket": "your-bucket.appspot.com"})

bucket = storage.bucket()
blob = bucket.get_blob("test.csv")
blob.download_to_filename(filename="test_download.csv")
```

### Penggunaan Google Storage untuk Pipeline ETL
Google Storage juga bisa dimanfaatkan untuk membuat sebuah pipeline ETL sebagai media penyimpanan Cloud.