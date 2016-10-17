#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.argv[2]) 
LINE = ' '.join(sys.argv[3:]) 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
# tipo de red, tipo de paquete son constantes de paquete socket
# socket.AF_INET : camino de internet
# socket.SOCK_DGRAM: utilizamos UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT)) # nos conectamos con el servidor tupla
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')# enviamos 
    # cadena de caracteres en bytes 
    data = my_socket.recv(1024) # guarda en data lo q recibo tamaño buffer
    print('Recibido -- ', data.decode('utf-8'))# decodifica de bytes a utf-8
#cerramos el with
print("Socket terminado.")
