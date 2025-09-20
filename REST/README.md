# REST (Representational State Transfer)
REST merupakan arsitektur/konsep yang digunakan untuk membangun API yang biasa digunakan untuk web service. REST berjalan di atas protokol HTTP, sehingga komunikasi antara client dan server mengikuti aturan HTTP. Pada pengujian ini, terdapat juga dua node yaitu client dan server, dimana akan mengirimkan HTTP request ke server melalui kode berikut ;
```
r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
```
BASE dan endpoint yang dapat digunakan sudah di-define pada sisi server, yaitu GET, /add dan /mul. Untuk parameter lainnya - seperti a dan b - user dapat mengirimkan angka dengan tipe data integer.

Protokol TCP juga digunakan pada client dan server untuk mengirimkan pesan HTTP. Ini dapat dilihat pada fungsi requests, dimana fungsi ini sekaligus membuat TCP connection antara client dan server dan melakukan 3-way handshake (SYN, SYN-ACK, dan ACK). Ini juga dapat dibuktikan melalui tampilan packet capture di bawah
<img src="https://i.imgur.com/elHDASY.jpeg">
