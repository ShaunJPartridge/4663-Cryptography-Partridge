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
Now the idea behind Pratt certificates is that a number {n} is prime if and only if the multiplicative group (Z/nZ)^*} is cyclic of order n-1. So if we can produce an element a in  (Z/nZ) such that a^(n-1) = 1  but a^(n-1)/p != 1 for all primes p | n, then it will follow that (Z/nZ)^* contains a cyclic group of order n-1. This will imply that n is prime, because otherwise the Euler function of(n) < n-1.
```
### References:
- <a id="1">[1]</a>: https://brilliant.org/wiki/prime-testing/
- <a id="2">[2]</a>: https://cp-algorithms.com/algebra/primality_tests.html
- <a id="3">[3]</a>: https://link.springer.com/referenceworkentry/10.1007%2F978-1-4419-5906-5_441
- <a id="4">[4]</a>: https://link.springer.com/referenceworkentry/10.1007%2F978-1-4419-5906-5_446
- <a id="5">[5]</a>: https://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/goldwasserkilian.pdf
- <a id="6">[6]</a>: https://amathew.wordpress.com/2011/03/04/gila-2-pratt-certificates-for-primality/
