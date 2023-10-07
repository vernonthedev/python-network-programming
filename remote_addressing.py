import socket

def get_remote_address_info():
    remote_host = 'www.github.com'

    try:
      print(f"Ip address: {socket.gethostbyname(remote_host)}")
    except (socket.error, err_msg):
      print(f"An exception occurred. {socket.error, err_msg}")


if __name__ == '__main__':
    get_remote_address_info()
