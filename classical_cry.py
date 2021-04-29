# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:03:37 2021

@author: andyp
"""


def main():
    text = "at"
    a = int(input("Enter the multiplier: "))
    s = int(input("Enter the shift number: "))
    
    
    if gcd(abs(a), 26) != 1:
        raise Exception("a and 26 should be coprime!!!")
    result = ""
    
    for i in range(0, len(text)):
        char = text[i].capitalize()
        if (char.isupper()):
            result += chr((a * ord(char) + s - 65) % 26 + 65)
        elif(char == ' '):
            result = result + ' '
        else:
            result += chr((a * ord(char) + s - 97) % 26 + 97)
    print ("Cipher: ", result)
    
def gcd(a, b):
    if a == 0 :
        return b

    return gcd(b%a, a)

main()

  
