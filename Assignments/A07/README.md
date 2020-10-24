# Assignment 7 - Finding Primes
## Categories:

### Deterministic:
##### 
```
A determinstic primality test, simply outputs true if a number is prime, and false when the number is prime. Below
are a couple of deterministic algorithms to test a number's primality.
```
###    - Trial Division:
#####
```
This algorithm checks a number's primality by simply using the fact of a prime number only being divisible by itself
and one; and doing the complete opposite, by checking if a number is divisible by some other positive integer besides
itself and one, or is a composite.
```
####
```
def isPrime(n):
    if n < 2: return False
    for i in xrange(2, n):   # from 2 to n-1
        if n % i == 0:       # n is divisible by i
            return False
    return True
```
