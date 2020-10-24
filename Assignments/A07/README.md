# Assignment 7 - Finding Primes
# Categories:

### Deterministic
##### A determinstic primality test, simply outputs true if a number is prime, and false when the number is composite. Below are a couple of deterministic algorithms to test a number's primality.
###      Trial Division:
##### This algorithm checks a number's primality by simply using the fact of a prime number only being divisible by itself and one; and doing the complete opposite, by checking if a number is divisible by some other positive integer besides itself and one, or is a composite.
####
```
def isPrime(n):
    if n < 2: return False
    for i in xrange(2, n):   # from 2 to n-1
        if n % i == 0:       # n is divisible by i
            return False
    return True
```
###      Deterministic version of Miller-Rabin's algorithm:
##### Miller made his algorithm deterministic by only checking all bases <= *O*((ln n)^2). When testing 32-bit integers it is only necessary to check the first 4 prime bases: 2,3,5, and 7. And for testing 64-bit integers it is enough to check the first 12 prime bases: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37. It's also possible to do the check with only 7 bases: 2, 325, 9375, 28178, 450775, 9780504, and 1795265022. However, since these numbers, except 2, are not prime, you need to check additionally if the number you are checking is equal to any prime divisor of the bases: 2, 3, 5, 13, 19, 73, 193, 407521, 299210837.
####
```
bool MillerRabin(u64 n) { // returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    int r = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (int a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
```
### References:
- <a id="1">[1]</a>: https://brilliant.org/wiki/prime-testing/
- <a id="2">[2]</a>: https://cp-algorithms.com/algebra/primality_tests.html
