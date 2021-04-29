# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:26:57 2021

@author: andyp
"""

def decode():
    print("This function will help to decode with RSA")
    p = int(input("Enter the p: "))
    q = int(input("Enter the q: "))
    key = int(input("Enter the key: "))
    value = int(input("Enter the encoded code: "))
    d = modInverse(key, (p-1) * (q-1))
    result = fme(int(value), int(d), int(p * q))
    print("d is the inverse of ", key, " mod (p-1) * (q-1)", )
    print("d here is", d)
    print("Decoded code is", result)


def encode():
    print("This function will help to encode with RSA")
    origin = int(input("Enter the number you want to encode: "))
    p = int(input("Enter the p: "))
    q = int(input("Enter the q: "))
    key = int(input("Enter the key: "))
    result = fme(int(origin), int(key), int(p * q))
    print("The encrypted result is ", result)
    
    
def fme(a, b, m):
    e = 1
    while (b > 0):
        if (b & 1):
            e = (e * a) % m
            b = b - 1
        a = (a * a) % m
        b = int(b / 2)
    return e % m;


def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

decode()