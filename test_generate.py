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
        self.assertEqual(de%pq,1,'hej')
        self.assertEqual(generate.gcd(d,(p-1)*(q-1)),1)

if __name__ == '__main__':
    unittest.main()
