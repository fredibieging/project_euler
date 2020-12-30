#!/usr/bin/python
import sys

f = open("p059_cipher.txt", "r")
message = [int(c) for c in f.readline().split(',')]

for k1 in range(97, 123):
    for k2 in range(97, 123):
        for k3 in range(97, 123):
            key = [k1, k2, k3] * (len(message) / 3)
            original = [m ^ k for m, k in zip(message, key)]
            decrypted = "".join([chr(c) for c in original])
            if " and " in decrypted:
                print decrypted
                print sum(original)
                sys.exit(0)
