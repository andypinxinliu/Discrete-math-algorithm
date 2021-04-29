# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:03:45 2021

@author: andyp
"""


def main():
    print("This function will help you find Chinese reminder theorem")
    print("There is going to be 2, 3 or 4 lines of x = A mod B, then it will calculate x")
    print("The input will be in the form of x = A mod B, then the function will help find x")
    time = int(input("Enter the number of equation for this calculation: "))
    rows, cols = (time, 2)
    array = [[0 for i in range(cols)] for j in range(rows)]
    number = 1
    for i in range(0, time):
        array[i][0] = int(input("Enter the first number A: "))
        array[i][1] = int(input("Enter the second number B: "))
        number = number * array[i][1]
        print("The equation is x = ", array[i][0], " mod ", array[i][1])
        
    output = []
    calculate = []
    modinfront = 0;
    for i in range(0, time):
        output.append(number / array[i][1])
        calculate.append(modInverse(output[i], array[i][1]))
        modinfront = modinfront + calculate[i] * array[i][0] * output[i]
    
    print("The value of x is: ", modcal(modinfront, number), " mod ", number)
    print()
    print()
    
    print("The following is what you can write for an exam question: ")
    s = ""
    for i in range(0, time - 1):
            s = s + str(array[i][1])
            s = s+ " * "
    s = s + str(array[time-1][1])
    print("M", "=", s)
    for i in range(0, time):
        print("M", i+1, " = ", number, " / ", array[i][1], " = ", output[i])
    for i in range(0, time):
        print("y", i+1, " * ", output[i], " = 1 mod ", array[i][1])
        print("y", i+1, " is the iverse of ", output[i], " mod ", array[i][1])
        print("So, by using the Euclidean algorithm, we can find y", i+1, " = ", calculate[i])
     
    s2 = ""
    for i in range(0, time - 1):
        s2 = s2 + str(array[i][0]) + " * " + str(output[i]) + " * " + str(calculate[i]) + " + "
    s2 = s2 + str(array[time-1][0]) + " * " + str(output[time - 1]) + " * " + str(calculate[time - 1])
    print("x = (", s2, " mod ", number)
    print("So x = ", modcal(modinfront, number), " mod ", number)
    
    
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def modcal(a, b):
    if (a > b):
        while a - b > 0:
            a = a - b
    elif (a < 0):
        a = a + b
    else:
        a = a
    return int(a)
 
 
main()