def prints(data):
    print 'str:'
    print data
    print 'hex:'
    for i in data:
        print '0x' + i.encode('hex'),
    print '\ndec:'
    for i in data:
        print int(i.encode('hex'), 16),
    print '\n'