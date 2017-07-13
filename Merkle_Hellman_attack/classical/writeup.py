#encoding:utf-8
from sage.all import *

pubKey = eval(open('key.pub', 'r').readline())
cipher = int(open('enc', 'r').readline())
nbit = len(pubKey)
print nbit
#nbit = 263, 被加密的文本共66字节

A = Matrix(ZZ, nbit+1, nbit+1)

for i in xrange(nbit):
    A[i,i] = 1

for i in xrange(nbit):
    A[i, nbit] = pubKey[i]

A[nbit, nbit] = -int(cipher)

#res = A.LLL()
res = '''[   1    1    0    0    1    1    0    0    1    1    0    1    1    0    0    0    1    1    0    0    0    0    1    0    1    1    0    0    1    1    1    0    1    1    1    1    0    1    1    0    1    0    0    1    1    0    1    0    0    1    1    0    0    1    1    0    1    1    0    1    0    1    1    0    0    1    1    0    0    0    1    0    0    1    1    0    0    1    1    0    1    0    1    1    1    1    1    0    1    1    0    1    0    0    0    0    1    1    0    0    1    0    1    0    0    1    1    0    0    0    1    0    0    1    1    0    0    0    1    0    1    0    0    1    1    0    1    0    0    1    1    0    1    0    0    0    1    0    0    1    1    1    0    0    1    0    1    1    1    1    1    0    0    1    1    0    0    0    1    0    1    1    0    1    0    0    1    0    1    1    0    1    0    1    1    0    0    1    1    0    0    1    1    0    1    1    1    0    0    1    1    0    1    0    1    1    1    1    1    0    0    1    1    0    0    0    1    0    1    0    0    0    0    0    1    0    1    1    1    0    1    0    0    0    1    1    1    0    1    0    0    0    0    1    1    0    0    0    1    0    1    1    0    0    0    1    1    0    1    1    0    0    1    0    1    0    1    1    1    1    1    0    1    0]
'''.replace(' ', '').replace('[', '').replace(']', '')

print res
print len(res)
flag = hex(int(res,2)>>1)[2:].strip('L')
flag = '0'*(len(flag)%2)+flag
print flag.decode('hex')