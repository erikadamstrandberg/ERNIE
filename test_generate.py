import generate
import unittest

class test_rsa_key_gen(unittest.TestCase):
    
    def test_generate_one_key(self):
        pair = generate.RsaKeyPair()
        p = pair.p
        q = pair.q
        d = pair.d
        e = pair.e

        de = d*e
        pq = (p-1)*(q-1)
        self.assertEqual(de%pq,1)
        self.assertEqual(generate.gcd(d,(p-1)*(q-1)),1)

    def test_gcd(self):
        a = 24
        b = 18
        greatest_divisor_a_b = 6
        self.assertEqual(generate.gcd(a,b),greatest_divisor_a_b)
    
    def test_generate_d_e(self):
        p = 47
        q = 59
        d_start = 0

        d_test = 441
        e_test = 121

        (d,e) = generate.generate_d_e(p,q,d_start);
        self.assertEqual(d,d_test)
        self.assertEqual(e,e_test)

    ## What is the jacobi symbol?
    ## When is the output 1 or -1?
    ## Time of tests are also very different?
    ## Seems to crash is a = b?
    def test_jacobi_symbol_true(self):
        a = 1202
        b = 11
        self.assertEqual(generate.jacobi_symbol(a,b),1)
    
    def test_jacobi_symbol_false(self):
        a = 19
        b = 11
        self.assertEqual(generate.jacobi_symbol(a,b),-1)

if __name__ == '__main__':
    unittest.main()
