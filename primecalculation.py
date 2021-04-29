# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import math


def main():
    print("this progrm test the prime ")
    number = int(input("Please enter an integer larger than 2: "))
    primes = []
    
    primes = []
    
    for possiblePrime in range(2, 50000):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

    divident = []
    originalnumber = number
    for i in primes:
        while(number % i == 0):
            number = number / i
            divident.append(i)
    if number != 1:
        s1 = ""
        print("Unable to do calculation in this range of primes!!!")
        for i in range(0, len(divident) - 1):
            s1 = s1 + str(divident[i])
            s1 = s1 + " * "
        s1 = s1 + str(divident[len(divident) - 1])
        print(originalnumber, " = ", s1, "* some large prime numbers")
    else:
        print(divident)
        s =""
        for i in range(0, len(divident) - 1):
            s = s + str(divident[i])
            s = s+ " * "
        s = s + str(divident[len(divident) - 1])
        print(originalnumber, "=", s)
        
        
main()
            
    
        
            
        

