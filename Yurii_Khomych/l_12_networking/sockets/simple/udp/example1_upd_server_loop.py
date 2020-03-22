import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8888))

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        print("Socket closed")
        break
    else:
        print("Some message:", result.decode("utf-8"))
