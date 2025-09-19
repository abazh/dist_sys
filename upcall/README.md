# Upcall
pola komunikasi antar client dan server, dimana server tidak hanya merespons permintaan client secara pasif, tetapi juga mengirimkan callback kepada client. Pada pengujian ini, mekanisme upcall terjadi ketika server menerima pesan dari client,  setelah itu server langsung mengirimkan balasan khusus berupa ;
```
"Upcall event: Processing " + data
```
Ini merupakan callback yang dikirimkan dari server ke client. Contohnya, ketika user mengirimkan pesan '1' ke client, maka server akan menerima pesan tersebut dan mengemasnya menjadi ;
```
Received from client: 1
```
Lalu server mengirimkan callback ke client dengan pesan ;
```
Received upcall from server: Upcall event: Processing 1
```
Ini berlangsung terus menerus hingga salah satu dari mereka (client/server) memutus koneksinya

Pada pola komunikasi upcall, digunakan protokol TCP karena terdapat pada potongan kode dibawah ini yang menunjukkan bahwa secara default, Python akan membuat socket dengan tipe TCP
```
server_socket = socket.socket()
client_socket = socket.socket()
```
Pada kode servercall.py, terdapat juga potongan kode seperti dibawah ini yang menunjukkan karakteristik dari protokol TCP, yaitu .listen() dan .accept() ;
```
server_socket.listen(1)
conn, address = server_socket.accept()  
```
<img src="https://i.imgur.com/DbOqtzz.jpeg">
