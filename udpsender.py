import socket

import time


class UdpSender:
    def __init__(self, to_host, to_port):
        self.to_host = to_host
        self.to_port = to_port
        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.send_sock.close()

    def send(self, data, to_host=None, to_port=None):
        if not to_host:
            to_host = self.to_host
        if not to_port:
            to_port = self.to_port
        self.send_sock.sendto(data, (to_host, to_port))


def loop_send(to_host, to_port, data=None, interval=None):
    send_sock = UdpSender(to_host, to_port)
    while True:
        if data and interval:
            send_sock.send(data)
            time.sleep(interval)
        else:
            i = str(raw_input('>'))
            send_sock.send(i)
            if '$exit' in i:
                break

if __name__ == '__main__':
    local_host = '127.0.0.1'
    port = 61544
    loop_send(local_host, port)