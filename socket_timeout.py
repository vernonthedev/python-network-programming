import socket

print(socket.getdefaulttimeout())

# set a new socket timeout value
socket.setdefaulttimeout(100)
print(socket.getdefaulttimeout())
