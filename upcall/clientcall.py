#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:16:13 2024

@author: widhi
"""

import socket
import logging

# Konfigurasi logging
logging.basicConfig(filename='client_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def client_program():
    try:
        client_socket = socket.socket()
        client_socket.settimeout(10)  # Timeout 10 detik untuk koneksi
        client_socket.connect(('upcall-server', 4141))
        logging.info("Connected to server at upcall-server:4141")
        
        while True:
            try:
                # Meminta pengguna untuk memasukkan beberapa pesan sekaligus, dipisahkan dengan koma
                messages = input("Enter messages (separated by commas): ").split(',')

                for message in messages:
                    message = message.strip()
                    if message.lower() == 'bye':
                        print("Exiting...")
                        client_socket.close()
                        logging.info("Connection closed by user.")
                        return

                    client_socket.send(message.encode())
                    logging.info(f"Sent: {message}")

                    data = client_socket.recv(1024).decode()
                    logging.info(f"Received: {data}")

                    print('Received upcall from server:', data)
            except socket.timeout:
                print("Timeout: No response from server.")
                logging.warning("Timeout: No response from server.")
                break
        
        client_socket.close()
        logging.info("Connection closed.")
    except socket.error as e:
        print(f"Socket error: {e}")
        logging.error(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    client_program()
