# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama : Muhammad Navis Raditya Riayatsyah

Kelas : PBP C

NPM : 2106717291

Heroku App Link : [https://pbp-tugas02.herokuapp.com/todolist/](https://rezataufiq56.herokuapp.com/todolist/)

### 1. Apa kegunaan pada elemen ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ?

Kegunaan utamanya adalah sebagai penjaga dari serangan berbahaya. Karena {% csrf_token %} akan menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa kembali token tersebut setiap saat ketika terdapat *request*.

Jika *request* yang masuk tidak berisikan token, maka *request* tidak akan dieksekusi.

### 2. Apakah kita dapat membuat elemen secara manual (tanpa menggunakan generator seperti})? Jelaskan secara gambaran besar bagaimana cara membuat secara manual!

Kita dapat membuat form secara manual. Secara garis besarnya kita membuat formnya sesuai apa yang sudah kita definisikan pada `models.py (kolaborator: Reza Taufiq Yahya)`

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Setelah menambahkan task baru pada aplikasi addtodolist, datanya akan disimpan pada database sebagai sebuah objek yang nantinya akan ditampilkan pada file dengan format .html.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

1. Membuat app todolist dengan perintah `python manage.py startapp todolist`
2. Menambahkan path todolist ke dalam `urls.py` project django seperti `path ('todolist/',include ('todolist.urls')),`
3. Menambahkan `class todolist` pada `models.py` yang memiliki atribut user, date, title, dan description
4. Untuk mengimplementasikan form register kita mengimport `from django.shortcuts import redirect` `from django.contrib.auth.forms import UserCreationForm` `from django.contrib import messages`
5. Selanjutnya kita membuat `todolist.html` yang isinya memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
6. Kita membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
   (kolaborator: Reza Taufiq Yahya)

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Nama : Muhammad Navis Raditya Riayatsyah

Kelas : PBP C

NPM : 2106654183

Heroku App Link : https://pbp-tugas02.herokuapp.com/todolist/

### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Singkat saja, Inline CSS adalah penggunaan CSS yang ada pada line yang sama pada element yang diinginkan. Kelebihannya inline css ini bisa langsung digunakan untuk melihat perubahan secara langsung. Kekurangannya, inline css harus diterapkan pada setiap elemen secara langsung.

Internal CSS, adalah penggunaan CSS yang masih dalam file .html yang sama namun penulisannya tidak dalam 1 (satu) line untuk element yang diinginkan. Kelebihannya hanya akan terdapat satu file yang berisikan layout-ing dari web dan styling-nya. Kekurangannya tidak akan efisien apabila terdapat banyak file yang ingin diubah dalam satu waktu.

External CSS, adalah penggunaan CSS yang berada di file berbeda dengan file .html. Kelebihannya, bisa langsung megubah elemen-elemen dengan tag yang sama dalam berbagai file. Kekurangannya, jumlah file yang dibuat menjadi lebih banyak dan halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

### 2. Jelaskan tag HTML5 yang kamu ketahui.

- head, tag untuk mempersiapkan headline (bagian atas dari suatu laman)
- body, tag untuk mempersiapkan body (bagian munculnya teks pada laman)
- div class, tag untuk memperkenalkan sebuah class
- br, break (new line)
- tr, mendefinisikan row dalam tabel
- td, mendefinisikan sel dalam tabel
- form, mendefinisikan sebuah formulir dalam body
- button, tombol
- a, sebuah hyperlink
- span, 'sesuatu' dalam sebuah line. 'sesuatu' dapat berupa apa saja. bisa berisikan 'null'
- h1, h2, h3, hn; header ke-n
- p, paragraf (teks)
- li, item dalam list
- ul, unordered list

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- .class, untuk mengambil class yang sudah di-define pada file .html
- ::before, memasukkan sesuatu sebelum setiap konten `<p>`
- #id, mengambil id yang sudah di-define pada file .html)

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat folder static dan diisi dengan sebuah folder css yang berisikan style.css
- meng-integrasikan file .html dengan .css dengan menambahkan line <linkrel="stylesheet"href="{% static 'css/style.css' %}"> pada base.html yang dapat ditemukan dalam folder project_django
- mendefinisikan class dan id yang ingin diubah pada file todolist.html, login.html, register.html, dan addtask.html
- menambahkan syntax css pada style.css untuk class dan id terkait
