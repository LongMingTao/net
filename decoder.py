def prints(data):
    print 'str:'
    print data
    print 'hex:'
    print str2hex(data)
    print '\ndec:'
    print str2dec(data)
    print '\nbin'
    print str2bin(data)


def str2dec(data):
    ret = []
    for i in data:
        ret.append(int(i.encode('hex'), 16))
    return ret


def str2hex(data):
    ret = []
    for i in data:
        ret.append(i.encode('hex'))
    return ret


def bin2dec(data):
    t = data.replace('0b', '')
    if not t:
        return 0
    else:
        return int(t, 2)


def bin2hex(data):
    t = data.replace('0b', '')
    if not t:
        return 0
    else:
        return hex(int(t, 2))


def str2bin(data):
    ret = []
    for i in data:
        ret.append(bin(int(i.encode('hex'), 16)).replace('0b', '').zfill(8))
    return ret


def get_ip(bd):
    return '{0}.{1}.{2}.{3}'.format(bin2dec(bd[0]), bin2dec(bd[1]), bin2dec(bd[2]), bin2dec(bd[3]))
