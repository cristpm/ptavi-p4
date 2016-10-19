#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
# socketserver.DatagramRequestHandler : heredamos para manejar UDP

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    clientes = {}

    def handle(self): # TRATAMOS EL SOCKET COMO UN FICHERO
        
        Ip_client = self.client_address[0]
        P_client = self.client_address[1]
        print('TUS DATOS SON:')
        print("IP = ", Ip_client, "Puerto = ", P_client)
        for line in self.rfile:# leemos el socket
            l = line.decode('utf-8')
            if l.split(' ')[0] == 'REGISTER':# si la linea tiene la cab REGISTER
                print("El cliente nos manda",l)
                SIPRegisterHandler.clientes[l.split(' ')[1][4:]] = Ip_client
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                print("USUARIOS ==> ", SIPRegisterHandler.clientes)
        
            
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
