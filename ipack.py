from decoder import bin2dec, bin2hex, get_ip, str2bin, str2hex

BYTE2BIT = 32 / 8

PRINT_FORMAT = '''
ip version: {0}
head length: {1} bits ({12} bytes)
server type = {2}
total length = {3} bits ({13} bytes)
16bit id = {4}
3bit flag = {5}
13bit offset = {6}
ttc = {7} jumps
protol = {8}
16bit checksum = {9}
src ip = {10}
dst ip = {11}
'''

PRINT_IP_FORMAT = PRINT_FORMAT + '''
ip data = {0}
ip data_hex = {1}
'''


PROTOL_MAP = {
    1: 'ICMP',
    6: "TCP",
    17: "UDP"
}



class IPack(object):
    def __init__(self, data=None):
        self.version = None
        self.head_length = None
        self.server_type = None
        self.total_length = None
        self.id = None
        self.flag = None
        self.offset = None
        self.ttc = None
        self.protol = None
        self.check_sum = None
        self.src = None
        self.dst = None
        self.ip_data = None
        if data:
            self.decode(data)

    def decode(self, data):
        bd = str2bin(data)
        self.version = bin2dec(bd[0][:-4])
        self.head_length = bin2dec(bd[0][-4:]) * BYTE2BIT
        self.server_type = bin2hex(bd[1])
        self.total_length = bin2dec(bd[2] + bd[3]) * BYTE2BIT
        self.id = bin2hex(bd[4] + bd[5])
        self.flag = bd[6][0:3]
        self.offset = bin2dec(bd[6][3:] + bd[7])
        self.ttc = bin2dec(bd[8])
        self.protol = PROTOL_MAP[bin2dec(bd[9])]
        self.check_sum = bin2dec(bd[10] + bd[11])
        self.src = get_ip(bd[12:16])
        self.dst = get_ip(bd[16:20])
        self.ip_data = "".join(data[self.head_length:])

    def str_head(self):
        return PRINT_FORMAT.format(
            self.version,
            self.head_length,
            self.server_type,
            self.total_length,
            self.id,
            self.flag,
            self.offset,
            self.ttc,
            self.protol,
            self.check_sum,
            self.src,
            self.dst,
            str(int(self.head_length) / BYTE2BIT),
            str(int(self.total_length) / BYTE2BIT),
        )

    def __str__(self):
        return self.str_head() + PRINT_IP_FORMAT.format(
            self.ip_data,
            str2hex(self.ip_data)
        )
