import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)
# sock.setblocking(False)
sock.settimeout(5)
# sock.settimeout(0)    #sock.blocking(False)
# sock.settimeout(None) #sock.blocking(True)


while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print("no clients")
    # except socket.timeout:
    #     print('timeout')
    else:
        client.setblocking(True)
        result = client.recv(1024)
        print(f"client: {client}")
        print(f"addr: {addr}")
        print("Some message: ", result.decode("utf-8"))
        client.close()
        print("client close")
