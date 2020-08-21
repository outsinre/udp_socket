#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""UDP Client

1. Capture user's lower-case string and send to the server.
2. Receive upper-case string from the server and print on screen.

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
    """Main entrance of the UDP client module."""

    server_host, server_port = "192.168.56.105", 12345

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Sockets are by default always created in "blocking mode" unless set a timeout
    client_socket.settimeout(5)

    user_input = input('Input lower-case sentence: ')

    try:
        client_socket.sendto(user_input.encode(), (server_host, server_port))
    except socket.timeout as tmt:
        print("Socket sendto() exception:", tmt)
        client_socket.close()
        return 1
    except socket.error as err:
        print("Socket sendto() exception:", err)
        client_socket.close()
        return 1
    else:
        print("To server socket: {}.\nMessage sent: {}".format((server_host, server_port), user_input))

    try:
        # UDP uses recvfrom() instead of recv() as the socket may receive datagram from multiple remote sockets
        # recvfrom() does not need server socket address
        server_data, server_address = client_socket.recvfrom(2048)
    except socket.timeout as tmt:
        print("Socket recvfrom() exception:", tmt)
        return 1
    except socket.error as err:
        print("Socket recvfrom() exception:", err)
        return 1
    else:
        print("From server socket: {}\nMessage received: {}".format(server_address, server_data.decode()))
    finally:
        print("Closing client socket ...")
        client_socket.close()
        print("done!")

if __name__ == "__main__":
    sys.exit(main())
