import numpy
import random

def jacobi_symbol(a,b):
    a, b = int(a), int(b)
    if a == 1:
        return 1
    elif a % 2 ==0:
        return jacobi_symbol(a/2,b) * (-1)**((b**2 -1)/8)
    else:
        return jacobi_symbol(b % a, a) * (-1)**((a-1)*(b-1)/4)

def generate_prime_candidate(n_size):
    return random.getrandbits(n_size)



