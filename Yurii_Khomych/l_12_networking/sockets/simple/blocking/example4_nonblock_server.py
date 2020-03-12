import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)
sock.setblocking(True)

client, addr = sock.accept()
print(f"client: {client}")
print(f"addr: {addr}")
result = client.recv(1024)
print("Some message: ", result.decode("utf-8"))

client.close()
print("socket close")
