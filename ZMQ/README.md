# ZeroMQ
ZeroMQ merupakan library yang dapat memungkinkan digunakannya berbagai pola komunikasi, seperti Publish-Subscribe, Push-Pull (Pipeline), dan Client-Server
## Publish Subscriber
Sama halnya dengan MQTT, publisher akan terus menerus mengirimkan pesan hingga subscriber menberhentikannya sendiri. Pesan yang dikirimkan publisher berupa pesan waktu seperti:
```
WAKTU Fri Sep 19 12:03:10 2025
```
Serta pada sisi subscriber, diharuskan untuk men-'subscribe' topik yang ingin di-'subscribe'. Pada pengujian ini, subscriber hanya akan menerima pesan yang diawali dengan string "WAKTU"
```
socket.setsockopt_string(zmq.SUBSCRIBE, "WAKTU")
```
Mekanisme pub-sub ini bekerja menggunakan protokol TCP di port 12345, ini ditunjukkan pada potongan kode dari pubzmq.py
```
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:12345")
```
## Push-Pull
Konsep push-pull ini bekerja seperti client-server, push berfungsi untuk mengirimkan pesan ke satu atau lebih penerima dan pull berfungsi untuk menerima pesan dari push.

Pada file pushzmq.py, terdapat producer yang akan menghasilkan workload acak. Ini ditandai dengan potongan kode ;
```
workload = random.randint(1, 100)
```
Lalu pesan tersebut dikirim ke worker dengan ;
```
socket.send(pickle.dumps(workload))
```
Pada sisi pull, worker akan selalu menunggu pekerjaan yang dikirimkan oleh worker
```
work = pickle.loads(socket.recv())
```
Jika sudah mendapat pekerjaan dari producer, maka worker akan menampilkan output seperti ;
```
Worker 1 received work: 40
```
Disini juga digunakan protokol TCP yang secara explisit di-define pada potongan kode ;
```
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:9999")
```
## Client-Server
Mekanisme client-server ini mirip dengan mekanisme request-response, dimana req digunakan oleh client untuk mengirim request dan response digunakan server untuk menerima request dan membalasnya. Client akan mengirimkan request ke server yang ditandai dengan potongan kode ;
```
socket.send(b"Hello")
message = socket.recv()
```
Lalu server mengolah request tersebut dan mengirimkan balasan pesan yang dilakukan oleh potongan kode ; 
```
message = socket.recv()
socket.send(b"World")
```
Contoh tampilan pada sisi client ketika mengirim request ke server adalah sebagai berikut ;
```
Sending request 0 ...
Received reply 0: b'World'
```
Sama seperti mekanisme pub-sub dan push-pull, client-server ini menggunakan protokol TCP untuk berkomunikasi. Ini ditujukan pada potongan kode pada file serverzmq.py maupun clientzmq.py
```
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

socket = context.socket(zmq.REQ)
socket.connect("tcp://zmq-rep:5555")
```
<img src="https://i.imgur.com/zxma0ms.jpeg">