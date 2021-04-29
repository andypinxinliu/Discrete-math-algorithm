# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:24:09 2021

@author: andyp
"""

def main():
    print("This function will help you find the mod inverse")
    print("there should be two input value, in the form A mod B. Then the function will help you to calculate Ax = 1 mod B")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = modInverse(number1, number2)
    print("The inverse of ", number1, " mod ", number2, " is ", result)
    coefficient = (result * number1 - 1) / number2
    print("1 = ", result, " * ", number1, " - ", number2, " * ", coefficient)

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
 
 
main()