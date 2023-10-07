import socket

def find_service_name():
    protocolName = 'tcp'
    for port in [80, 25]:
        print(f"Port: {port} => Service Name: {socket.getservbyport(port, protocolName)}")
        print(f"Port: {port} => Service Name: {socket.getservbyport(53, 'udp')}")

if __name__ == '__main__':
    find_service_name()
