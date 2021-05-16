## Python imports
import numpy as numpy
import argparse
import os
## Helper functions
import generate
import file_util

## Calculate exponent and moduls quickly
## with exponential squaring!
def crypt(bas, exp, n):
    if exp == 0:
        return 1
    if exp == 1:
        return bas%n
      
    t = crypt(bas, int(exp/2), n)
    t = (t**2)%n
      
    if exp%2 == 0:
        return t      
    else:
        return ((bas%n)*t)%n

def encrypt(message, encrypt_to):
    with open("RSA_KEY/rsa.private", "r") as infile:
        n, e = [int(private_int.strip()) for private_int in infile.readlines()[:2]]
    file_e = open(encrypt_to, "x")
    with open(message, "r") as m:
        while True:
            char = m.read(1)
            if not char:
                break
            file_e.write(str( pow(ord(char), e, n)) + "\n")
    file_e.close()

    
def decrypt(cipher, decrypt_to):
    with open("RSA_KEY/rsa.public", "r") as infile:
        n, d = [int(public_int.strip()) for public_int in infile.readlines()[:2]]
    file_cipher = open(cipher, "r")
    file_decrypt_to = open(decrypt_to, "x")
    for line in file_cipher:
        file_decrypt_to.write(chr(pow(int(line.strip()), d, n)))
    file_cipher.close()
    file_decrypt_to.close()

if __name__== "__main__":
    parser = argparse.ArgumentParser('rsa encrypt')
    parser.add_argument("-r","--rsa_key", required=False, action='store_true', help="generate new key pair")
    parser.add_argument("-e","--encrypt", help="encrypt a file")
    parser.add_argument("-d","--decrypt", help="decrypt a cipher")
    args = parser.parse_args()

    if args.rsa_key:
        # generate a rsa key (public private pair) 
        KEY_folder = "RSA_KEY"
        file_util.save_rsa_key(generate.RsaKeyPair(), KEY_folder)

    if args.encrypt:
        file_to_encrypt = args.encrypt
        if os.path.exists(file_to_encrypt):
            encrypted_file = "encrypted_" + file_to_encrypt
            if os.path.exists(encrypted_file):
                os.remove(encrypted_file)
            encrypt(file_to_encrypt, encrypted_file)
        else:
            print("No message with that filename!")

    if args.decrypt:
        cipher_to_decrypt = args.decrypt
        if os.path.exists(cipher_to_decrypt):
            decrypted_message = "decrypted_message.txt"
            if os.path.exists(decrypted_message):
                os.remove(decrypted_message)
            decrypt(cipher_to_decrypt, decrypted_message)
        else:
            print("No cipher with that filename")
 
