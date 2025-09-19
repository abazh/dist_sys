# Message Queueing Teleportary Transport
Dalam demonstrasi MQTT, terdapat 2 model yaitu publisher (pub) dan subscriber (sub). Publisher sebagai server yang mengirimkan pesan broker ke MQTT, subscriber sebagai client yang menerima pesan yang dikirimkan oleh publisher. Subscriber harus subscribe ke topik 'sister/temp' yang disediakan oleh publisher, sehingga publisher akan mengirimkan pesan ;
```
Published: Suhu: 28°C
```
Pesan ini dikirim secara looping sampai client dihentikan 
<img src="https://i.imgur.com/oyGtyOj.jpeg">
Pada screenshot diatas, terdapat 2 jenis protokol yaitu MQTT dan TCP yang melakukan looping untuk mengirim pesan. Publisher menggunakan protokol MQTT untuk mengirim pesan ke subscibernya sedangkan subscriber menggunakan protokol TCP untuk mengirimkan pesan ACK atau Acknowledgement, yang berarti pesan MQTT dari publisher sudah sampai ke subscriber dan subscriber mengonfirmasinya.
Adapun port yang digunakan merupakan port 1883, unsecured port yang sering digunakan untuk protokol MQTT. Ini juga dapat divalidasi dengan melihat potongan kode dari sub.py.
```
broker = "mqtt-broker"
port = 1883  # Port default untuk MQTT
topic = "sister/temp"
```