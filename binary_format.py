# inet_ntoa()
# inet_aton()

import socket

def convert_ipv4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        un_packed_id_addr = socket.inet_ntoa(packed_ip_addr)
        print(f"Ipaddress packed: {packed_ip_addr}")
        print(f"Ipaddress unpacked: {un_packed_id_addr}")

if __name__ == '__main__':
    convert_ipv4_address()
