#encoding:utf-8
import base64

def get_base64_diff_value(stego_line, normal_line):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in xrange(len(normal_line)):
        if stego_line[i] != normal_line[i]:
            return abs(base64chars.index(stego_line[i])-base64chars.index(normal_line[i]))
    return 0

def base64_stego_decode(strings):
    res = ''
    for i in strings:
        stego_line = i.strip()
        normal_line = i.strip().decode('base64').encode('base64').strip()
        diff = get_base64_diff_value(stego_line, normal_line)
        pads_num = stego_line.count('=')
        if diff:
            res += bin(diff)[2:].zfill(pads_num*2)
        else:
            res += '0' * pads_num * 2
        return res



def get_base32_diff_value(stego_line, normal_line):
    base32chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in xrange(len(normal_line)):
        if stego_line[i] != normal_line[i]:
            return abs(base32chars.index(stego_line[i])-base32chars.index(normal_line[i]))
    return 0

def base32_stego_decode(strings):
    res = ''
    for i in strings:
        stego_line = i.strip()
        normal_line = base64.b32encode(base64.b32decode(i.strip()))
        diff = get_base32_diff_value(stego_line, normal_line)
        if '=' not in stego_line:
            continue
        if diff:
            res += bin(diff)[2:]
        else:
            res += '0'
    return res

