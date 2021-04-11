import numpy as np
import random
import sys
sys.setrecursionlimit(10**6)

# Generates a prime number with the bitsize n_size.
# Tries to check if the number actually is prime n_iter times.
# If b is a composite number each check has a probability to
# find it with 50% for each check, thus the probablity of 
# b being prime is 2**(n_iter)
def generate_prime(n_size,n_iter):
    b = generate_prime_candidate(n_size)
    success = True
    for i in range(n_iter):
        ## Generate a random number in the range 1 to b-1
        ## Jacobi symbol crashes if a = b!
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

# Generates a random number with the bitsize n_size
def generate_prime_candidate(n_size):
    n = random.getrandbits(n_size)
    while n < 3:
        n = random.getrandbits(n_size)
    return n 

# Testing if candidate is a prime number
def jacobi_symbol(a,b):
    if a == 1:
        return 1
    else:
        if a % 2 == 0:
            return jacobi_symbol(a/2,b) * (-1)**((b**2 -1)//8)
        else:
            return jacobi_symbol(b % a, a) * (-1)**((a-1)*(b-1)//4)


# Find greatest common divisor (GCD) of a and b
def gcd(a,b):
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 
             
# Generate d as relative prime to (p-1)*(q-1)
# Then find e from the extended euclidean algorithm
def generate_d_e(p,q,d_start):
    d = np.maximum(p,q) + d_start
    d_is_found = False 

    # Just iterate until a relativly prime d is found
    while not d_is_found:
        d += 1
        d_is_found = d_rel_prime(d, p, q)

    # Extended Euclidean algorithm with the 
    # variables from wikipedia article
    x0 = (p-1)*(q-1)
    x1 = d

    r0 = d
    r1 = x0

    s0 = 1
    s1 = 0

    while not x0 == 1:
        x_temp = x1
        x1 = x0%x1
        x0 = x_temp
        
        quotient = r0//r1

        r_temp = r1
        r1 = r0 - quotient*r1
        r0 = r_temp
        
        s_temp = s1
        s1 = s0 - quotient*s1
        s0 = s_temp
        
    e = s1

    # If e < log2(p*q) we choose a new d and 
    # repeat the process! 
    # NOTE More recursion might been stupid?
    if e < np.log2(p*q):
        (e,d) = generate_d_e(p,q,d)

    return (d,e)
    
def d_rel_prime(d, p, q):
    if gcd(d, (p-1)*(q-1)) == 1:
        return True
    else:
        return False

# Constructor!
class RsaKeyPair():
    def __init__(self,n_size=10,n_iter=11):
        self.p = generate_prime(n_size,n_iter)
        self.q = generate_prime(n_size,n_iter)
        (self.d,self.e) = generate_d_e(self.p,self.q,1)
        self.n_size = n_size
