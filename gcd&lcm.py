# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:24:57 2021

@author: andyp
"""
import math


def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
# Function to return LCM of two numbers
def lcm(a,b):
    return int((a / gcd(a,b)) * b)

def main():
    number1 = eval(input("Enter the first number: "))
    number2 = eval(input("Enter the second number: "))
    if number2 > number1:
        maxnum = number2
        minnum = number1
    else:
        maxnum = number1
        minnum = number2
    primes = []
    if maxnum < 50000:
        for possible in range(2, maxnum + 1):
            isPrime = True
            number = int(math.sqrt(possible)) + 1
            for j in range(2, number):
                if possible % j == 0:
                    isPrime = False;
                    break
            if isPrime:
                primes.append(possible)
    else:
        for possible in range(2, 50000):
            isPrime = True
            number = int(math.sqrt(possible)) + 1
            for j in range(2, number):
                if possible % j == 0:
                    isPrime = False;
                    break
            if isPrime:
                primes.append(possible)

    divident1 = []
    divident2 = []
    originalnumber1 = maxnum
    originalnumber2 = minnum
    for i in primes:
        while(maxnum % i == 0):
            maxnum = maxnum / i
            divident1.append(i)
        while(minnum % i == 0):
            minnum = minnum / i
            divident2.append(i)
    if maxnum != 1 or minnum != 1:
        print("Unable to do calculation in this range of primes!!!")
        s1 =""
        s2 = ""
        for i in range(0, len(divident1) - 1):
            s1 = s1 + str(divident1[i])
            s1 = s1 + " * "
        s1 = s1 + str(divident1[len(divident1) - 1])
        for i in range(0, len(divident2) - 1):
            s2 = s2 + str(divident2[i])
            s2 = s2 + " * "
        s2 = s2 + str(divident1[len(divident2) - 1])
        print(s1, "* some large prime numbers")
        print(s2, "* some large prime numbers")
    else:
        s1 =""
        s2 = ""
        for i in range(0, len(divident1) - 1):
            s1 = s1 + str(divident1[i])
            s1 = s1 + " * "
        s1 = s1 + str(divident1[len(divident1) - 1])
        for i in range(0, len(divident2) - 1):
            s2 = s2 + str(divident2[i])
            s2 = s2 + " * "
        s2 = s2 + str(divident1[len(divident2) - 1])
        print(originalnumber1, "=", s1)
        print(originalnumber2, "=", s2)
        print("GCD of ", originalnumber1, 'and', originalnumber2,
              'is', gcd(originalnumber1, originalnumber2))
        print('LCM of', originalnumber1, 'and', originalnumber2,
              'is', lcm(originalnumber1, originalnumber2))
        
        
main()
            
        
        