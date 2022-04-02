
import socket
import sys


def main():
    # creating the socket
    #sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    # just connecting
    sck.connect(('localhost', 2000))




    print("Sending data...")
    a=input("enter a value :").encode()
    b=input("enter b value :").encode()
    s=" ".encode()
    c=a+s+b
    sck.send(c)
    print("sent bytes:",sys.getsizeof(c))
    # I don't care about your response server, I'm closing
    sck.close()


if __name__ == "__main__":
    main()

