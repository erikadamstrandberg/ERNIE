## Python imports 
import numpy as numpy
import argparse

## Helper functions
import generate

if __name__=="__main__":
    parser = argparse.ArgumentParser('rsa encrypt')
    parser.add_argument("--rsa_key", required=False, action='store_true', help="generate new key pair")
    parser.add_argument("--encrypt", required=False, default=False, type=bool, help="encrypt a file")
    args = parser.parse_args()

    if args.rsa_key:
        # generate a rsa key (public private pair)
        pair = generate.RsaKeyPair()
        print(pair.p)
        print(pair.q)
        print(pair.d)
        print(pair.e)

    if args.encrypt:
        new_parser = argparse.ArgumentParser('encryption set up')
        new_parser.add_argument("--public_key", required=True, default=None, type=str, help="public key to use for encryption")
        new_parser.add_argument("--file", required=True, default=None, type=str, help="file to encrypt")
        
