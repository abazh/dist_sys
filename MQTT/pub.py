#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:49:49 2024

@author: widhi
"""

import paho.mqtt.client as mqtt
import time
import sys
import random

# Gunakan broker lokal dalam docker compose
broker = "mqtt-broker"
port = 1883  # Port default untuk MQTT

# Inisialisasi topik dan pesan suhu
topic_temp = "sister/temp"
topic_humidity = "sister/humidity"

# Callback untuk koneksi
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Berhasil terhubung ke broker MQTT {broker}")
    else:
        print(f"Gagal terhubung ke broker, kode error: {rc}")
        sys.exit(1)

# Inisialisasi klien MQTT dengan API versi terbaru
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

# Menghubungkan ke broker dengan timeout dan error handling
try:
    print(f"Menghubungkan ke {broker}...")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"Gagal menghubungkan ke broker: {e}")
    sys.exit(1)

# Mengirimkan data suhu dan kelembapan secara periodik
try:
    while True:
        suhu = random.randint(20, 35)  # Suhu acak antara 20°C dan 35°C
        kelembapan = random.randint(30, 50)  # Kelembapan acak antara 30% dan 50%

        # Publikasi ke topik suhu
        client.publish(topic_temp, f"{suhu}°C")
        print(f"Mengirim suhu: {suhu}°C")

        # Publikasi ke topik kelembapan
        client.publish(topic_humidity, f"{kelembapan}%")
        print(f"Mengirim kelembapan: {kelembapan}%")

        time.sleep(1)  # Tunggu 1 detik sebelum mengirim data berikutnya
except KeyboardInterrupt:
    print("Publisher dihentikan.")
    client.disconnect()
