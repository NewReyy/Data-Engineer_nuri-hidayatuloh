**Docker** adalah platform perangkat lunak yang digunakan untuk mengembangkan, mengirim, dan menjalankan aplikasi dalam lingkungan kontainer. Kontainer Docker memungkinkan pengembang untuk mengemas perangkat lunak dan semua dependensinya ke dalam unit yang dapat dijalankan secara konsisten di berbagai lingkungan.

**Docker Container** adalah unit dasar dari Docker yang berisi aplikasi dan semua dependensinya. Container Docker berjalan di atas mesin fisik atau virtual, dan mereka terisolasi satu sama lain serta dari lingkungan host. Mereka berbagi kernel dari sistem operasi host tetapi memiliki file sistem terpisah.

**Docker Images** adalah templat yang digunakan untuk membuat container Docker. Image Docker berisi semua informasi yang diperlukan untuk menjalankan sebuah container, termasuk kode, runtime, library, variabel lingkungan, dan konfigurasi.

**Docker Build** adalah proses membuat image Docker dari Dockerfile dan sumber daya aplikasi lainnya. Dockerfile adalah file teks yang berisi instruksi langkah demi langkah tentang cara membangun image Docker. Proses Docker Build melibatkan langkah-langkah seperti menyalin file, menginstal dependensi, menjalankan perintah, dan menentukan variabel lingkungan.

**Fungsi dan Kegunaan**:

1. **Kemasan Aplikasi**: Docker memungkinkan pengembang untuk mengemas aplikasi beserta dependensinya ke dalam kontainer yang portabel dan dapat dijalankan di lingkungan apa pun.

2. **Isolasi**: Docker menggunakan teknologi kontainerisasi untuk memastikan bahwa aplikasi diisolasi satu sama lain dan dari lingkungan host, sehingga menghindari konflik dan masalah ketergantungan.

3. **Portabilitas**: Dengan Docker, Anda dapat dengan mudah memindahkan aplikasi antara lingkungan pengembangan, pengujian, dan produksi tanpa perubahan signifikan, karena container berisi semua yang diperlukan untuk menjalankan aplikasi.

4. **Efisiensi**: Kontainer Docker ringan dan cepat dimulai, memungkinkan aplikasi untuk dijalankan dengan overhead minimal.

5. **Skalabilitas**: Docker memungkinkan Anda untuk menambah atau mengurangi jumlah kontainer sesuai kebutuhan, sehingga memudahkan skalabilitas aplikasi.

6. **Orkestrasi**: Docker dapat diintegrasikan dengan alat-orkestrasi seperti Kubernetes atau Docker Swarm untuk mengelola dan menata kontainer dalam lingkungan yang lebih besar.

Secara keseluruhan, Docker memberikan cara yang konsisten, portabel, dan efisien untuk mengembangkan, mendistribusikan, dan menjalankan aplikasi modern di berbagai lingkungan komputasi.


Contoh penggunaan:

docker pull redis:latest #mengambil images redis

docker container create -it --name redis1 redis:latest #membuat container dengan menggunakan docker images redis

docker container create -it --name redis2 redis:latest #membuat container dengan menggunakan docker images yang sama

docker container ls #melihat semua docker container yang sudah dibuat dan sedang berjalan

docker container ls -a #menampilkan semua container yang sudah dibuat, dijalankan, maupun yang sudah exit

docker container start redis1 #menjalankan container

docker inspect redis1 #melihat informasi container

docker logs redis1 #melihat log dari aplikasi

docker ps -a #melihat container yang berjalan maupun dibuat

docker exec -it redis1 redis-cli #menjalankan aplikasi di CLI didalam container

#perintah didalam container cli redis
docker exec -it redis1 redis-cli
127.0.0.1:6379> SET "name" "nuri"
OK
127.0.0.1:6379> SET "city" "bangkalan"
OK
127.0.0.1:6379> KEYS
(error) ERR wrong number of arguments for 'keys' command
127.0.0.1:6379> KEYS ^
(empty array)
127.0.0.1:6379> KEYS *
1) "city"
2) "name"
127.0.0.1:6379>

docker container stop redis1 #menghentikan container

docker container rm redis1 #menghapus container (container harus sudah tidak running)

docker container rm -f redis2 #menghapus container secara paksa

docker build -t mini-python-app:1.0.0 . #build aplikasi menggunakan docker

docker images #digunakan untuk menampilkan images yang berhasil di build

docker run --name pythonapp mini-python-app:1.0.0 #menjalan aplikasi secara langsung pada foreground. (pythonapp, berfungsi sebagai nama containernya dan mini-python-app sebagai imagesnya)

docker tag mini-python-app:1.0.0 nurihidayatuloh147/mini-python-app:1.0.0 #menandai images yang sudah ada, dan connect kan ke repository yang ada di Docker Hub

docker push nurihidayatuloh147/mini-python-app:1.0.0 #push kedalam docker hub yang sudah dibuat repositorynya

docker pull nurihidayatuloh147/mini-python-app:1.0.0 #digunakan untuk mengambil images yang sudah ada didalam docker hub

docker run --name testdocker --rm nurihidayatuloh147/mini-python-app:1.0.0 #menjalankan container dengan images yang sudah di pull dan langsung menghapus container yang dibuat menggunakan -rm

docker run -itd --name testdb -p 3306:3306 -e MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=yes mariadb:latest #berguna untuk menjalankan di background dengan nama container testdb dengan dengan port 3306 dan mengabaikan password lalu menggunakan images mariadb:latest yang sudah ada di docker hub

docker logs testdb #digunakan untuk melihat status atau logs pada container

docker exec -it testdb mariadb #menjalankan command untuk masuk kedalam database mariadb

Docker Network adalah fitur yang memungkinkan container Docker untuk berkomunikasi satu sama lain, baik pada host yang sama maupun antar host yang berbeda. Dalam lingkungan Docker, setiap container mendapatkan alamat IP sendiri dan dapat diakses melalui jaringan yang diatur oleh Docker.

Berikut beberapa konsep dasar terkait Docker Network:

1. **Bridge Network**: Ini adalah jenis jaringan default yang digunakan oleh Docker. Saat Anda menjalankan container tanpa menentukan jaringan tertentu, Docker secara otomatis menempatkan container tersebut dalam jaringan bridge. Dalam jaringan bridge, container dapat berkomunikasi satu sama lain melalui alamat IP yang diberikan oleh bridge.

2. **Host Network**: Dengan menggunakan jaringan host, container akan menggunakan antarmuka jaringan host yang sebenarnya, bukan memiliki antarmuka jaringan virtual sendiri. Ini membuat container dapat diakses menggunakan alamat IP host langsung.

3. **Overlay Network**: Overlay network memungkinkan container di host yang berbeda untuk berkomunikasi satu sama lain. Ini berguna dalam skenario di mana Anda memiliki cluster Docker yang tersebar di beberapa host dan ingin container pada host yang berbeda untuk berkomunikasi.

4. **Macvlan Network**: Macvlan memungkinkan Anda untuk memberikan alamat MAC dan IP yang unik kepada setiap container, sehingga membuatnya tampak seperti perangkat fisik di jaringan.

5. **None Network**: Jika Anda ingin container tidak terhubung ke jaringan apa pun, Anda dapat menggunakan jaringan None. Container dengan jaringan None hanya dapat diakses melalui interaksi langsung dengan host atau melalui Docker exec.

Anda dapat membuat, mengelola, dan menggunakan jaringan Docker menggunakan perintah CLI Docker atau melalui Docker Compose. Berikut adalah beberapa perintah yang sering digunakan untuk bekerja dengan jaringan Docker:

- `docker network create <nama_jaringan>`: Membuat jaringan baru.
- `docker network ls`: Menampilkan daftar jaringan yang ada.
- `docker network inspect <nama_jaringan>`: Melihat detail dari suatu jaringan.
- `docker network connect <nama_jaringan> <nama_container>`: Menghubungkan suatu container ke jaringan.
- `docker network disconnect <nama_jaringan> <nama_container>`: Mencabut koneksi suatu container dari jaringan.
- `docker network rm <nama_jaringan>`: Menghapus jaringan.

Dengan menggunakan Docker Network, Anda dapat mengelola komunikasi antar container dengan lebih mudah dan efisien dalam lingkungan Docker.

mkdir cobavolume #buat folder baru

docker run -itd --name cobadb -e MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=yes -p 3306:3306 -v D:\Apps\dcvolume\myvolume:/var/lib/mysql mariadb:latest

docker volume create <nama_volume>: Membuat volume baru.

docker volume ls: Menampilkan daftar volume yang ada.

docker volume inspect <nama_volume>: Melihat detail dari suatu volume.

docker volume rm <nama_volume>: Menghapus volume.

docker compose up -d #menjalankan docker compose pada background

docker compose down #menghentikan docker compose yang sudah dibuat