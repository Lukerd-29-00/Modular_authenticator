import json
import math
import egcd
from sage.all import *
from pwn import *
import random
import time
with open("public_key.json",'r') as f:
    public_key = json.load(f)

p = public_key["p"]
e = public_key['e']
ssq = public_key['s^e']

e2 = math.gcd(e,p-1)
assert (e & (e - 1)) == 0

d = egcd.egcd(e,p-1)[1] % (p-1)

s = pow(ssq,d,p)
start = time.time()
while e2 > 1:
    s = int(Mod(s,p).sqrt())
    e2 >>= 1
assert pow(s,e,p) == ssq
print(time.time() - start)
secrets = [random.randint(1,1<<32) for _ in range(128)]

squares = [pow(r,e,p) for r in secrets]

r = remote("0.cloud.chals.io",14202)

r.sendline(json.dumps(squares).encode('utf-8'))

challenges = json.loads(r.recvline().decode('utf-8'))

responses = [r if chal == 'r' else (r * s) % p for r, chal in zip(secrets,challenges)]

r.sendline(json.dumps(responses).encode('utf-8'))

r.interactive()