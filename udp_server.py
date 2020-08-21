#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""UDP Server

1. Receive client's lower-case message.
2. Transfrom the message to upper-case and send back.

"""

__author__ = "Jim Gray"
__email__ = "jimgray@outlook.com"
__credits__ = ["Google","Python3.8 Manual"]
__copyright__ = "Copyright 2020, China"
__license__ = "GPL"
__version__ = "0.1"
__status__ = "Development"

import sys
import socket

def main():
    """Main entrance of the UDP server module."""

    # '' means to listen on all interfaces
    server_host, server_port = '', 12345

    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server_socket.bind((server_host, server_port))

    # Sockets are by default always created in "blocking mode" unless set a timeout
    server_socket.settimeout(5*60)
    print("The server is ready to receive datagrams.")

    while True:
        try:
            # UDP uses recvfrom() instead of recv() as the socket may receive datagram from multiple remote sockets
            client_data, client_address = server_socket.recvfrom(2048)
        except socket.timeout as tmt:
            print("Server socket recvfrom() exception:", tmt)
            print("Continue ...")
            continue
        except socket.error as err:
            print("Server socket recvfrom() exception:", err)
            print("Continue ...")
            continue
        else:
            print("Client socket:", client_address)

        client_message = client_data.decode()
        print("Message received:", client_message)

        upper_message = client_message.upper()
        try:
            server_socket.sendto(upper_message.encode(), client_address)
        except socket.timeout as tmt:
            print("Server socket sendto() exception:", tmt)
            print("Continue ...")
            continue
        except socket.error as err:
            print("Server socket sendto() exception:", err)
            print("Continue ...")
            continue
        else:
            print("Message sent: {}\nContinue ...".format(upper_message))

if __name__ == "__main__":
    sys.exit(main())
