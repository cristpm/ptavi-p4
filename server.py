#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
# socketserver.DatagramRequestHandler : heredamos para manejar UDP

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self): # TRATAMOS EL SOCKET COMO UN FICHERO
        Ip_client = self.client_address[0]
        P_client = self.client_address[1]
        
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:# leemos el socket
            print("IP cliente = ", Ip_client, "Puerto cliente = ", P_client)
            print("El cliente nos manda ", line.decode('utf-8'))
            

if __name__ == "__main__":

    # ip y puerto donde escucha el servidor y clase que maneja la peticion
    PORT = int(sys.argv[1]) 
    serv = socketserver.UDPServer(('', PORT), EchoHandler) 
    print("Lanzando servidor UDP de eco...")
    try:
        # bucle esperando peticiones
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
