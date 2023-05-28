# features
- Binding dengan address dan port
- Parsing HTTP request
- Mencari file 
- Memberikan response atas request yang dilakukan
- Mengirimkan pesan Error

# Web-Server-TCP
**Contents**
- cara bekerja

### Cara Kerja
Setelah server di run, ketika akan mengakses web server (dilakukan dengan menuju localhost:8000/index.html, dimana akan ditampilkan web server sederhana dengan kolom untuk menginput link video dari youtube yang ingin diputar di web server, ketika link sudah di input maka user dapat menekan tombol ‘Watch’ dan video akan di load oleh web server dan akan bisa diputar, jika link belum di input ketika user menekan tombol ‘Watch’ akan ditampilkan error.

Implementasi TCP Socket
Implementasi TCP Socket tidak terlihat secara langsung karena Anda menggunakan modul “http.server” yang sudah mengabstraksi layer socket.

Modul http.server menyediakan kelas HTTPServer yang merupakan turunan dari kelas socketserver.TCPServer, yang pada dasarnya menggunakan socket untuk menerima koneksi dan menangani permintaan HTTP.

Pada bagian ini, HTTPServer dibuat dengan memberikan alamat host dan nomor port pada konstruktor. Kemudian, metode serve_forever() digunakan untuk menjalankan server secara berkesinambungan, yang akan mengikat socket ke alamat dan port yang telah ditentukan, kemudian menerima koneksi masuk dan menangani permintaan HTTP.

Implementasi detail dari TCP Socket dan lapisan transport lainnya, seperti socket, socketserver, dan protokol HTTP, diambil alih oleh modul http.server sehingga tidak perlu lagi mengelolanya secara terlihat dalam kode tersebut.

Menerima dan Memparsing HTTP Request
Bagian yang menerima dan memparsing HTTP Request terdapat pada method do_POST dan do_GET dalam class SimpleHTTPRequestHandler

Pada do_POST, kita mengakses header Content-Length menggunakan self.headers['Content-Length'] untuk mendapatkan panjang konten yang dikirimkan dalam permintaan.
Menggunakan self.rfile.read(content_length) untuk membaca data yang dikirimkan dalam body permintaan sebanyak panjang konten yang telah diperoleh.
Data yang diterima dalam format string di-decode menggunakan post_data.decode('utf-8').
Menggunakan parse_qs dari modul urllib.parse untuk memparsing data yang diterima menjadi dictionary yang lebih mudah diakses.
Mengambil nilai name dan email dari data yang sudah diparse menggunakan data.get('name', [''])[0] dan data.get('email', [''])[0].
Menampilkan data yang diterima ke console menggunakan print.

Pada do_GET, kita memeriksa apakah path bukan '/'. Jika kondisi ini terpenuhi, server akan mengirimkan respons dengan kode status 404 (Not Found) menggunakan self.send_error.
Dalam kedua method tersebut, kita mengakses atribut-atribut self.headers untuk mendapatkan informasi header permintaan HTTP dan self.rfile untuk membaca data yang dikirimkan dalam body permintaan. Data yang diterima dapat diparsing dan diakses menggunakan modul urllib.parse seperti parse_qs.
Mengambil dan Mencari File yang Diminta dan HTTP Response
Bagian yang mengambil dan mencari file yang diminta serta HTTP response terdapat pada method do_GET dalam class SimpleHTTPRequestHandler.

Pada do_GET, kita memeriksa apakah path bukan '/'. Jika kondisi ini terpenuhi, server akan mengirimkan respons dengan kode status 404 (Not Found) menggunakan self.send_error.
Jika path adalah '/', kita membuka file 'index.html' menggunakan open('index.html', 'rb') dalam mode baca biner ('rb') karena kita akan membaca konten file dalam bentuk byte.
Menggunakan with open(...) as file: untuk memastikan bahwa file ditutup secara otomatis setelah selesai digunakan.
Membaca isi file menggunakan file.read() dan menyimpannya dalam variabel content.
Mengirimkan respons HTTP dengan kode status OK menggunakan self.send_response(HTTPStatus.OK).
Mengatur header Content-type menjadi 'text/html' menggunakan self.send_header('Content-type', 'text/html').
Menambahkan header Access-Control-Allow-Origin dengan nilai '*' untuk mengizinkan akses dari semua domain menggunakan self.send_header('Access-Control-Allow-Origin', '*').
Mengakhiri pengaturan header menggunakan self.end_headers().
Mengirimkan konten file sebagai respons HTTP menggunakan self.wfile.write(content).
Dalam bagian ini, kita menggunakan open untuk membuka file yang diminta ('index.html' dalam contoh ini) dan membacanya. Kemudian, konten file tersebut dikirimkan sebagai respons HTTP dengan menggunakan metode self.wfile.write.

### Contributor
TUGAS BESAR JARINGAN KOMPUTER
- Rafi Azizi Raya
- Raditha Ariyani
- M Habib Ramadhan
