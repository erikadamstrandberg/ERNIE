import numpy as np
import random
import sys
sys.setrecursionlimit(10**6)

def jacobi_symbol(a,b):
    if a == 1:
        return 1
    else:
        if a % 2 == 0:
            return jacobi_symbol(a/2,b) * (-1)**((b**2 -1)//8)
        else:
            return jacobi_symbol(b % a, a) * (-1)**((a-1)*(b-1)//4)

def generate_prime_candidate(n_size):
    n = random.getrandbits(n_size)
    while n < 3:
        n = random.getrandbits(n_size)
    return n 

def gcd(a,b):
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 
        
def generat e_prime(n_size,n_iter):
    b = generate_prime_candidate(n_size)
    success = True
    for i in range(n_iter):
        a = random.randrange(1,b)
        if gcd(a, b) == 1 and jacobi_symbol(a, b) == a**((b-1)//2) % b:
            continue
        else:
            success = False
            break
    if success:
        return b
    else:
        return generate_prime(n_size, n_iter)

def d_is_coprime(d, p, q):
    if gcd(d, (p-1)*(q-1)) == 1:
        return True
    else:
        return False
    
def generate_d(p,q,n_iter):
    d = np.maximum(p,q) + 1
    found_d = False 
    while not found_d:
        d += 1
        found_d = d_is_coprime(d, p, q, n_iter)
    return d

def generate_e(p,q,d):
    n = p*q
    
class RsaKeyPair():
    def __init__(self,n_size=100,n_iter=10):
        self.p = generate_prime(7,n_iter)
        self.q = generate_prime(7,n_iter)
        self.d = generate_d(self.p,self.q)
        self.e = 1
        self.n_size = n_size

