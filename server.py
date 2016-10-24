#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json
# socketserver.DatagramRequestHandler : heredamos para manejar UDP


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    clientes = []

    def handle(self):  # TRATAMOS EL SOCKET COMO UN FICHERO

        self.json2registered()
        self.expiration()
        Ip_client = self.client_address[0]
        P_client = self.client_address[1]
        print('TUS DATOS SON:', "IP = ", Ip_client, "Puerto = ", P_client)
        for line in self.rfile:  # leemos el socket
            l = line.decode('utf-8')
            # print(l)
            if l.split(' ')[0] == 'REGISTER':
                direc = l.split(' ')[1][4:]
            if l.split(' ')[0] == 'Expires:':
                t = int(l.split(' ')[1][0:-2])
        exp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + t))
        client = [direc, {"address": Ip_client, "expires": exp}]
        if t == 0:
            for user in self.clientes:
                if user[0] == direc:
                    self.clientes.remove(user)
        if t > 0:
            for user in self.clientes:
                if user[0] == direc:
                    self.clientes.remove(user)
            self.clientes.append(client)
        self.register2json()
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        print("CLIENTES ==> ", self.clientes)

    def register2json(self):
        json.dump(self.clientes, open('registered.json', 'w'), indent=4)

    def expiration(self):
        gmt = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
        for user in self.clientes:
            if gmt > user[1]['expires']:
                self.clientes.remove(user)

    def json2registered(self):
        try:
            with open('registered.json') as data_file:
                self.clientes = json.load(data_file)
        except:
            print('NO EXISTE registered.json')


if __name__ == "__main__":

    # ip y puerto donde escucha el servidor y clase que maneja la peticion
    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        # bucle esperando peticiones
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
