import socket

import decoder
from ipack import IPack
from udpack import UDPack


class RawRecver:
    def __init__(self, listen_host, listen_port, buff_size=1024):
        self.listen_host = listen_host
        self.listen_port = listen_port
        self.buff_size = buff_size
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)   # socket.htons(0x0800)

    def __del__(self):
        self.recv_sock.close()

    def loop_recv(self, buff_size=None):
        if not buff_size:
            buff_size = self.buff_size
        while True:
            data = self.recv_sock.recvfrom(buff_size)
            ipack = UDPack(data[0])
            # decoder.prints(data[0])
            print ipack
            print '-----  -----'
            if '$exit' in data[0]:
                break


if __name__ == '__main__':
    local_host = '127.0.0.1'
    port = 61512
    recv = RawRecver(local_host, port)
    recv.loop_recv()