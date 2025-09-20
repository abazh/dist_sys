# Request and Response
Pada pengujian reqresp, protokol jaringan yang digunakan adalah protokol TCP (Transmission Control Protocol), terdapat juga 2 model yaitu client dan server. Client mengirimkan pesan custom (user defined), lalu server akan menerima pesan tersebut dan mengirimkannya kembali ke client.
Protokol TCP mempunyai karakteristik sebagai berikut ;
```
server_socket.listen(1)
server_socket.accept()
```
Fungsi .listen() digunakan pada tahap SYN (synchronize) saat pertama kali dilakukannya handshake antara client dan server, dan fungsi .accept() digunakan pada tahap ACK (acknowledge) ketika client dan server sudah melakukan handshake
<img src="https://i.imgur.com/zG551ja.jpeg">