# Testing if candidate is a prime number
include <gmp.h>

cdef char * c_jacobi_symbol(char * a, char * b):
    mpz_t a_g, b_g, two, r
    mpz_init_set_str(a_g, a, 10)
    mpz_init_set_str(b_g, b, 10)
    if a == "1":
        return "1"
    else: # I know that a > b ?
        return "0"
#        mpz_init_set_str(two, "2", int 10)
#        mpz_cdiv_r(a_g, two, r)
#        root = mpz_get_ui(r)
#        if root == 0:
#            mpz_get_str(char *str, int 10, a)
#            return c_jacobi_symbol(a/2,b) * (-1)**((b**2 -1)//8)
#        else:
#            return c_jacobi_symbol(b % a, a) * (-1)**((a-1)*(b-1)//4)

def jacobi_symbol(a, b):
    return c_jacobi_symbol(a, b)