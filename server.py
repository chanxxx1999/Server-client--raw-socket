import socket
import sys


def main():
    # creating the socket
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binding the socket to the port 7456
    # notice that bind() take a tuple as argument
    sck.bind(('localhost', 7456))

    # now is time to say, I'm ready for connection OS, could you let me please?
    # the 1 specified how many connection it will queue up, until
    # start rejecting attempts of connections.
    sck.listen(1)

    print("Hey you I'm listening on 7456...weird port by the way")

    # accepting the incoming connection
    (client_sock, address) = sck.accept()
    while True:
        # 1024 is a magic number used on every networking tutorial out there
        # so here I also make use of it. Also in this case means that the socket
        # will process up to 1024 bytes of the incoming message from the client
        c=0
        msg = client_sock.recv(1024)
        if not msg:
            break
        for i in msg.decode('utf-8').split(" "):
            c += int(i)
        print("reserved bytes is: " ,sys.getsizeof(msg))
        print("bytes of sum is: ", sys.getsizeof(c))
        print(f"FROM: {address} sum: {c}")
        print()

    client_sock.close()


if __name__ == "__main__":
    main()
