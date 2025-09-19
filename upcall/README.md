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
