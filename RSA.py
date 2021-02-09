
from random import randrange, seed

seed(12345678910)

# GCD
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


# EGCD
def egcd(a, b):
  if b == 0:
    return (1, 0)
  else:
    quo = a // b
    rem = a % b
    (s, t) = egcd(b, rem)
    return (t, s - quo * t)


# Mult Inv
def multinv(a, n):
  (x, y) = egcd(a, n)
  return x % n

# Select two primes, p and q.
p = 191
q = 281


# N is the modulus.
n = p * q

# Compute totient, ϕ(n),
totient = (p-1) * (q-1)

# Construct a list of possible values for e,
# numbers that are relatively prime to the totient.
es = [i for i in range(2,totient) if gcd(i,totient) == 1]
# Select one of them at random.
e = es[randrange(1,len(es))]

# Specify e
e = 33

# Compute d such that d*e = 1 (mod ϕ(n))
d = multinv( e,totient )

# Private and Public keys
pub = (e, n)
pri = (d, n)


def rsa(key, value):
    return value ** key[0] % key[1]

def encrypt(key, bstr):
	return [rsa(key,c) for c in bstr]

def decrypt(key, arr):
	return [rsa(key,a) for a in arr]

print ("public key",pub)
print ("private key",pri)
print ("encrypt",encrypt(pub,[100000]))
print ("decrypt",decrypt(pri,[11759]))

