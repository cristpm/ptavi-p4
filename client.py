"""Programa cliente UDP que abre un socket a un servidor."""
# !/usrbin/python3.
# -*- coding: utf-8 -*-
import socket
import sys

try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    USER = sys.argv[4]
    Expires = sys.argv[5]
    LINE = 'REGISTER sip:' + USER + ' SIP/2.0\r\nExpires: ' + Expires + '\r\n'
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))  # nos conectamos con el servidor
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')  # enviamos
    data = my_socket.recv(1024)  # guarda en data lo q recibo tamaño buffer
    print('Recibido -- ', data.decode('utf-8'))  # decodifica de bytes a utf-8
print("Socket terminado.")
