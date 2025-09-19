#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:49:00 2024

@author: widhi
"""

import paho.mqtt.client as mqtt
import sys

# Gunakan broker lokal dalam docker compose
broker = "mqtt-broker"  # Service name
port = 1883  # Port default untuk MQTT

# Tambahkan dukungan untuk banyak topik
topics = ["sister/temp", "sister/humidity"]

# Callback ketika koneksi berhasil
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Berhasil terhubung ke broker MQTT {broker}")
        # Berlangganan ke semua topik dalam daftar
        for t in topics:
            client.subscribe(t)
            print(f"Berlangganan topik: {t}")
    else:
        print(f"Gagal terhubung ke broker, kode error: {rc}")
        sys.exit(1)

# Callback untuk pesan yang diterima
def on_message(client, userdata, message, properties=None):
    msg = f"Received message: {message.payload.decode()} (Topic: {message.topic})"
    print(msg)
    # Simpan pesan ke file log
    with open("mqtt_messages.log", "a") as log_file:
        log_file.write(msg + "\n")

# Inisialisasi klien MQTT dengan API versi terbaru
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# Menghubungkan ke broker dengan error handling
try:
    print(f"Menghubungkan ke {broker}...")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"Gagal menghubungkan ke broker: {e}")
    sys.exit(1)

# Menjaga koneksi tetap terbuka
try:
    print("Menunggu pesan... (Tekan Ctrl+C untuk keluar)")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber dihentikan.")
    client.disconnect()
