from decoder import str2bin, bin2dec, bin2hex, str2hex
from ipack import IPack, BYTE2BIT

PRINT_UDP_FORMAT = '''
src port = {0}
dst port = {1}
udp length = {2} bits ({4} bytes)
udp checksum = {3}
udp data = {5}
udp data_hex = {6}
'''


class UDPack(IPack):
    def __init__(self, data=None):
        super(UDPack, self).__init__(data)
        self.src_port = None
        self.dst_port = None
        self.udp_length = None
        self.udp_check_sum = None
        self.udp_data = None
        if data:
            self.decode(data)

    def decode_udp(self, ip_data):
        bd = str2bin(ip_data)
        self.src_port = bin2dec(bd[0] + bd[1])
        self.dst_port = bin2dec(bd[2] + bd[3])
        self.udp_length = bin2dec(bd[4] + bd[5]) * BYTE2BIT
        self.udp_check_sum = bin2hex(bd[6] + bd[7])
        self.udp_data = ip_data[8:]

    def decode(self, data):
        if self.version:
            self.decode_udp(self.ip_data)
        else:
            super(UDPack, self).decode(data)
            self.decode_udp(self.ip_data)

    def __str__(self, ip=True):
        if ip:
            ip = super(UDPack, self).str_head()
        else:
            ip = ''
        return ip + PRINT_UDP_FORMAT.format(
            self.src_port,
            self.dst_port,
            self.udp_length,
            self.udp_check_sum,
            str(int(self.udp_length) / BYTE2BIT),
            self.udp_data,
            str2hex(self.udp_data)
        )
