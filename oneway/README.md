# Oneway
Protokol jaringan UDP (User Datagram Protocol) merupakan protokol yang connectionless, membuat user dapat mengirimkan data secara langsung, tidak membutuhkan handshake seperti TCP, dapat dibuktikan dengan kode dari serverUDP berikut ;
```
server_socket.recvfrom(1024)
server_socket.sendto(message.encode('utf-8'), client_address)
```
Fungsi.sendto() hanya secara eksplisit menyatakan tujuan kemana data akan dikirim, tidak memperdulikan apakan tujuan dapat mengonfirmasi dan menerima data, sedangkan pada TCP terdapat fungsi .listen() dan .accept() dimana kedua fungsi ini dibutuhkan untuk melakukan handshake. Fungsi .listen() digunakan pada tahap SYN (synchronize) antara client dan server sedangkan .accept() digunakan pada tahap ACK (acknowledge) yang berarti data sudah siap untuk dikirim.
<img src="https://i.imgur.com/qIaJIXk.jpeg">
Pada packet capture diatas, dapat dilihat tedapat dua komunikasi antara port 57314 dengan 12345. Port 57314 merupakan port yang digunakan client untuk mengirim pesan kepada server dengan port 12345. Pesan yang dikirim berupa ;
```
message = "Hello, UDP server2!"
```
Selain itu, protokol yang digunakan dan ditangkap oleh tcpdump merupakan protokol UDP.