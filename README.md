# Apakah Ini Wordpress ?
 Sebuah program yang saya buat menggunakan bahasa program python3 , untuk mengetahui sebuah website apakah terbuat dari cms wordpress atau tidak, dengan memgirim requests ke url wp-login.php program ini tidak murni dari saya sendiri, ada campur tangan teman saya

<img src="https://raw.githubusercontent.com/akasakaid/Apakah-Ini-Wordpress/main/aiw.png">

# Cara menggunakan
```
Note : pastikan kalian sudah menginstall python 3 

1. clone repository ini dulu bisa menggunakan git, jika tidak install git bisa download manual (.zip)
2. Menuju ke folder/repository ini menggunakan cmd / terminal
3. Install module yg digunakan dalam program ini
    pip3 install requests colorama
4. Jalankan program dengan perintah 'python3 scan.py'
5. Masukkan list website yang akan di scan
6. Masukkan Thread (sesuaikan dengan kemampuan komputer)
7. Tunggu
8. Hasil website yang valid wordpress akan di simpan ke file _wp.txt dan website yg tidak valid akan di simpan ke file _no_wp.txt
```