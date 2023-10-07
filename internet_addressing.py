import socket

def print_system_internet_info():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    print(hostname)
    print(ipaddress)


if __name__ == '__main__':
    print_system_internet_info()
