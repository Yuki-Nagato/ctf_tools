from Crypto.Util import number
from Crypto import Random
from Crypto.PublicKey.pubkey import *
import sys

def generateKeys(msg_len):
	randomFunc = Random.new().read
	upperbound = 1<<(2*msg_len+4)
	sk = [number.getRandomRange(1, upperbound, randomFunc)]
	for i in range(1, msg_len):
		sk.append(number.getRandomRange(sum(sk) + 1, upperbound, randomFunc))
		upperbound = upperbound << 2
	N = number.getRandomRange(sk[msg_len-1] + 1, 2*sk[msg_len-1], randomFunc)
	mask = number.getRandomRange(N/4, 3 * N/4, randomFunc)
	while number.GCD(mask, N) != 1:
		mask = number.getRandomRange(1, N, randomFunc)
	pk = [ s * mask % N for s in sk ]
	return sk, N, mask, pk
## sk随机数

def encrypt(msg, pk):
	assert(len(msg) == len(pk))
	return sum([ int(msg[i]) * pk[i] for i in range(len(pk)) ])

def decrypt(cipher, sk, N, mask, pk):
	msg = ['0'] * len(pk) 
	cipher = cipher * number.inverse(mask, N) % N
	# sk = [ p * number.inverse(mask, N) % N for p in pk]
	for i in range(len(pk))[::-1]:
		if cipher >= sk[i]:
			cipher -= sk[i]
			msg[i] = '1'
	print msg
	return hex(int(''.join(msg), 2))[2:].rstrip('L').decode('hex')


if __name__ == "__main__":
	msg = sys.argv[1]
	msg_bit = bin(int(msg.encode('hex'), 16))[2:]
	sk, N, mask, pk = generateKeys(len(msg_bit))
	print sk, N, mask, pk
	open('key.pub','w').write(str(pk))
	enc = encrypt(msg_bit, pk)
	print enc
	print decrypt(enc, sk, N, mask, pk)
	open('enc','w').write(str(enc))
