import socket

import time


class UdpRecver:
    def __init__(self, listen_host, listen_port, buff_size=1024):
        self.listen_host = listen_host
        self.listen_port = listen_port
        self.buff_size = buff_size
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.recv_sock.close()

    def loop_recv(self, buff_size=None):
        self.recv_sock.bind((self.listen_host, self.listen_port))
        while True:
            data = self.recv_sock.recvfrom(self.buff_size)
            print '----- recv from ', data[1], ' -----'
            print data[0]
            print '-----  -----'
            if '$exit' in data[0]:
                break


if __name__ == '__main__':
    local_host = '127.0.0.1'
    port = 6789
    recv = UdpRecver(local_host, port)
    recv.loop_recv()