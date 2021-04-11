## Python imports
import numpy as numpy
import argparse
import os

## Helper functions
import generate
import file_util

def encrypt(message):
    file_private_n = open("RSA_KEY/rsa.private", "r")
    n = int(file_private_n.readlines()[0].strip())
    file_private_d = open("RSA_KEY/rsa.private", "r") 
    d = int(file_private_d.readlines()[1].strip())
    
    return (message**d)%n
    
def decrypt(cipher):
    file_private_n = open("RSA_KEY/rsa.public", "r")
    n = int(file_private_n.readlines()[0].strip())
    file_private_e = open("RSA_KEY/rsa.public", "r") 
    e = int(file_private_e.readlines()[1].strip())

    return (cipher**e)%n
    

if __name__== "__main__":
    parser = argparse.ArgumentParser('rsa encrypt')
    parser.add_argument("--rsa_key", required=False, action='store_true', help="generate new key pair")
    parser.add_argument("--encrypt", required=False, action='store_true', help="encrypt a file")
    args = parser.parse_args()

    if args.rsa_key:
        # generate a rsa key (public private pair) 
        KEY_folder = "RSA_KEY"
        file_util.save_rsa_key(generate.RsaKeyPair(), KEY_folder)

    if args.encrypt:
        to_encrypt = 120
        cipher = encrypt(to_encrypt)
        print(cipher)
        message = decrypt(cipher)
        print(message)
   #     new_parser = argparse.ArgumentParser('encryption set up')
    #    new_parser.add_argument("--public_key", required=True, default=None, type=str, help="public key to use for encryption")
     #   new_parser.add_argument("--file", required=True, default=None, type=str, help="file to encrypt")
 
