import os
import sys
import math

def checkPrimes(n):

    if n <= 1:
        print(n,"Is not prime")
        return False
    if n <= 3:
        print(n,"Is prime")
        return True
    if n % 2 == 0 or n % 3 == 0:
        print(n,"Is not prime")
        return False
    i = 5
    for i in range(i*i,n):
        if n % i == 0 or n % (i+2) == 0:
            print(n,"Is not prime")
            return False      
        i = i + 6
    
    print(n,"Is prime")
    return True
    


if __name__ == "__main__":

    checkPrimes(23)
    