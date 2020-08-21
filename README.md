# udp_socket

1. The client sends a lower-case sentence and the server replies the upper-case variant.
2. _socket address_ refers to an `(ip, port)` tuple.
3. There is no _connection_ so that `sendto()` requires receiver's address, and `recvfrom()` returns sender's address.

   `recvfrom()` does not require server socket address as it's implied by the pairing `sendto()`.
3. Make sure the server port is enabled in `firewalld`.
