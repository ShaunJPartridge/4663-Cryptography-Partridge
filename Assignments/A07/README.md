# Assignment 7 - Finding Primes
# Categories:

### Deterministic
##### A determinstic primality test, simply outputs true if a number is prime, and false when the number is composite. Below are a couple of deterministic algorithms to test a number's primality.
####      Trial Division:
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
####      Deterministic version of Miller-Rabin's algorithm:
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
### Certification
##### "A certificate of primality (or prime certificate) is a small set of values associated with an integer that can be used to efficiently prove that the integer is a prime number."
####      Elliptic Curve Primality Proving (ECPP):
##### "ECPP is a method to prove primality of an integer n that uses elliptic curves modulo n."
####
```
3.1. A PRIMALITY CRITERION USING ELLIPTIC CURVES. Using Lemma 1, we
can prove the following primality criterion. Theorem 2 is the heart of this paper;
the remainder shows how to implement, use and analyze it in detail.
THEOREM 2. Let n be an integer, not divisible by 2 or 3. Let A, B [ Zn, and
(4A3 1 27B2
, n) 5 1 and let L [ EA,B(Zn), with L Þ I. If qL 5 I, for some prime
q . n1/2 1 2n1/4 1 1, then n is prime.
Formally, qL is shorthand for performing the repeated doubling algorithm
described in Section 2.
PROOF. Our proof is by contradiction. If n is composite, then there exists a
prime divisor p such that p # =n and p Þ 2, 3. Furthermore, 4A3 1 27B Þ 0
mod p. Thus Lp [ EA,B( p) and qLp 5 I, by repeated application of Lemma 1.
Hence, the order of Lp must divide q and since Lp Þ I and q is prime, its order
must be equal to q. However, clearly, the order of Lp is at most #p( A, B) #
p 1 2=p 1 1 , q, a contradiction. e
3.2. OVERVIEW OF THE PRIMALITY PROVING ALGORITHM. We focus on the
problem of proving that a (prime) number is prime; throughout this discussion, p
is prime.
We use our primality criterion to reduce the primality of p to the primality of
a new prime, q, where q # p/ 2 1 o( p), and recursively prove that q is prime.
For technical reasons, we eventually stop when the number to be proven prime is
sufficiently small that it may be deterministically verified as prime. If too much
time passes, the algorithm times out and starts over from scratch.
```
####      Pratt Certificates:
####
```
Now the idea behind Pratt certificates is that a number n is prime if and only if the multiplicative group (Z/nZ)^* is cyclic of order n-1. So if we can produce an element a in  (Z/nZ) such that a^(n-1) = 1 but a^(n-1)/p != 1 for all primes p | n, then it will follow that (Z/nZ)^* contains a cyclic group of order n-1. This will imply that n is prime, because otherwise the Euler function of(n) < n-1.
```
### Compositeness
##### "A composite number is a positive integer that can be formed by multiplying two smaller positive integers. Equivalently, it is a positive integer that has at least one divisor other than 1 and itself. Every positive integer is composite, prime, or the unit 1, so the composite numbers are exactly the numbers that are not prime and not a unit."
####      Fermat Compositeness Test:
##### This test is done by applying Fermat's little theorem. "If this test determines that an odd number n, is composite, it is guaranteed to be so, otherwise the number is either a prime or a Carmichael number (if all coprime bases from 2 to (n-1)/2 are considered, otherwise a Fermat pseudoprime to all coprime bases considered."
```
import random
def isPrime(n, k):
    for i in range(k):
        a = random.randrange(2, n)  # 2 <= a <= n-1
        if pow(a, n-1, n) != 1:     # compute a^(n-1) mod n
            return False            # definitely composite
    else:
        return True   
 ```
####      Miller-Rabin Test:
##### Miller uses the contrapositive of the following theorem:
```
Let p be an odd prime, and let p-1 = 2^s x d, where d is an odd integer and s is a positive integer. Also let a be a positive integer coprime to p. Then at least one of the following must hold:
-   Some of a^(2^s x d), a^(2^s-1 x d),..., a^d is congruent to -1(mod p).
-   a^d is congruent to 1 (mod p).
```
##### "That is, if for some a, neither of the above holds, then p is clearly not prime."
```
import random
def isPrime(n, k):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False    # speedup

    # now n is odd > 3
    s = 0
    d = n-1
    while d % 2 == 0:
        s += 1
        d //= 2
    # n = 2^s * d where d is odd

    for i in range(k):
        a = random.randrange(2, n-1)    # 2 <= a <= n-2
        x = (a**d) % n
        if x == 1: continue
        for j in range(s):
            if x == n-1: break
            x = (x * x) % n
        else:
            return False
    return True
```
####       Solovay-Strassen Primality Test:
##### This tests is a probablistic test to determine if a number is composite or probably prime and can be referred to as an Euler-Jacobi pseudoprime test.
```
Euler proved that for any prime number p and any integer a,

a^(p-1)/2 is congruent to (a/p)(mod p) where (a/p) is the Legendre symbol. The Jacobi symbol is a generalisation of the Legendre symbol to (a/n), where n can be any odd integer. The Jacobi symbol can be computed in time O((log n)²) using Jacobi's generalization of law of quadratic reciprocity.

Given an odd number n we can contemplate whether or not the congruence

a^(n-1)/2 is congruent to (a/n)(mod n) holds for various values of the "base" a, given that a is relatively prime to n. If n is prime then this congruence is true for all a. So if we pick values of a at random and test the congruence, then as soon as we find an a which doesn't fit the congruence we know that n is not prime (but this does not tell us a nontrivial factorization of n). This base a is called an Euler witness for n; it is a witness for the compositeness of n. The base a is called an Euler liar for n if the congruence is true while n is composite.

For every composite odd n, at least half of all bases

 a in (Z/nZ)^*
are (Euler) witnesses as the set of Euler liars is a proper subgroup of (Z/nZ)^*. For example, for n=65, the set of Euler liars has order 8 and {1,8,14,18,47,51,57,64}, and (Z/nZ)^* has order 48.
This contrasts with the Fermat primality test, for which the proportion of witnesses may be much smaller. Therefore, there are no (odd) composite n without many witnesses, unlike the case of Carmichael numbers for Fermat's test.
```
```
inputs: n, a value to test for primality
        k, a parameter that determines the accuracy of the test
output: composite if n is composite, otherwise probably prime

repeat k times:
    choose a randomly in the range [2,n − 1]
    x <- (a/n)
    if x = 0 or a^(n-1)/2 not congruent to x (mod n) then 
        return composite
return probably prime
```

### References:
- <a id="1">[1]</a>: https://brilliant.org/wiki/prime-testing/
- <a id="2">[2]</a>: https://cp-algorithms.com/algebra/primality_tests.html
- <a id="3">[3]</a>: https://link.springer.com/referenceworkentry/10.1007%2F978-1-4419-5906-5_441
- <a id="4">[4]</a>: https://link.springer.com/referenceworkentry/10.1007%2F978-1-4419-5906-5_446
- <a id="5">[5]</a>: https://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/goldwasserkilian.pdf
- <a id="6">[6]</a>: https://amathew.wordpress.com/2011/03/04/gila-2-pratt-certificates-for-primality/
- <a id="7">[7]</a>: https://oeis.org/wiki/Compositeness
- <a id="8">[8]</a>: https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test

