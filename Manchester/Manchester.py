#encoding:utf-8
import sys


#曼彻斯特解码
def Manchester_decode(enc_bin):
    b_len = len(enc_bin)
    assert b_len%2 == 0
    assert sum([int(enc_bin[i]!=enc_bin[i+1]) for i in range(0,b_len, 2)]) == b_len/2
    res = ['','']
    for i in range(0, b_len, 2):
        if int(enc_bin[i]):
            res[0] += '1'
            res[1] += '0'
        else:
            res[0] += '0'
            res[1] += '1'
    return res

#曼彻斯特编码
def Manchester_encode(msg_bin):
    assert sum([(i=='0' or i=='1') for i in msg_bin]) == len(msg_bin)
    res = ['','']
    for i in msg_bin:
        if int(i):
            res[0] += '10'
            res[1] += '01'
        else:
            res[0] += '01'
            res[1] += '10'
    return res

#差分曼彻斯特解码
def Diff_Manchester_decode(enc_bin):
    b_len = len(enc_bin)
    assert b_len%2 == 0
    assert sum([int(enc_bin[i]!=enc_bin[i+1]) for i in range(0,b_len, 2)]) == b_len/2
    res = enc_bin[0]
    for i in range(2, b_len, 2):
        if enc_bin[i] == enc_bin[i-2]:
            res += '0'
        else:
            res += '1'
    return res

#差分曼彻斯特编码
def Diff_Manchester_encode(msg_bin):
    assert sum([(i=='0' or i=='1') for i in msg_bin]) == len(msg_bin)
    tmp = int(msg_bin[0])
    res = '{0}{1}'.format(tmp, tmp^1)
    for i in range(1, len(msg_bin)):
        if int(msg_bin[i]):
            res += res[-2:][::-1]
        else:
            res += res[-2:]
    return res


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 4:
        print 'Usage python Manchester.py <cmds> <modes> <strings>'
        print '  cmds:'
        print '    -e,          曼彻斯特编码'
        print '    -d,          曼彻斯特解码'
        print '  modes:'
        print '    --normal,    标准模式'
        print '    --diff,      差分模式'
        print '  strings:       二进制字符串'
        sys.exit(1)
    cmd = sys.argv[1]
    mode = sys.argv[2]
    strings = sys.argv[3]
    if cmd != '-e' and cmd != '-d':
        print 'Wrong cmd '+cmd
        sys.exit(1)
    if mode != '--normal' and mode != '--diff':
        print 'Wrong mode '+mode
        sys.exit(1)
    if strings.replace('0', '').replace('1', '') != '':
        print 'Wrong strings '+strings
        sys.exit(1)
    if cmd == '-e' and mode == '--normal':
        for i in Manchester_encode(strings):
            print i
    elif cmd == '-e' and mode == '--diff':
        print Diff_Manchester_encode(strings)
    elif cmd == '-d' and mode == '--normal':
        for i in Manchester_decode(strings):
            print i
    elif cmd == '-d' and mode == '--diff':
        print Diff_Manchester_decode(strings)


