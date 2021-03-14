import numpy
import random

def jacobi_symbol(a,b):
    a, b = int(a), int(b)
    if a == 1:
        return 1
    else:
        if a % 2 ==0:
            return jacobi_symbol(a/2,b) * (-1)**((b**2 -1)/8)
        else:
            return jacobi_symbol(b % a, a) * (-1)**((a-1)*(b-1)/4)

def generate_prime_candidate(n_size):
    return random.getrandbits(n_size)

def gcd(a,b):
    while not a == b :
        if a > b :
            a = a - b
        else :
            b = b - a
    return a

def generate_prime(n_size):
    b = generate_prime_candidate(n_size)
    #print(b)
    success = True
    for i in range(100):
        a = random.randrange(b)
        if gcd(a, b) == 1 and jacobi_symbol(a, b) == a*(b-1)/2 % b:
            continue
        else:
            success = False
            break
    if success:
        return b
    else:
        return generate_prime(n_size)
    
class RsaKeyPair():
    def __init__(self,n_size=100):
        self.p = 1
        self.q = 1
        self.d = 1
        self.e = 1
        self.n_size = n_size
    


            
        
