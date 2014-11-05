import sys, math
import numpy

def primesfrom2to(n):
  """ Input n>=6, Returns a array of primes, 2 <= p < n """
  sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
  for i in xrange(1,int(n**0.5)/3+1):
    if sieve[i]:
      k=3*i+1|1
      sieve[       k*k/3     ::2*k] = False
      sieve[k*(k-2*(i&1)+4)/3::2*k] = False
  return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def is_pandigital(n):
  tmp = str(n)
  if "0" in tmp:
    return False
  if len(tmp) == len(tmp):
      p = dict()
      for c in tmp:
        if c not in p:
          p[c] = True
      for i in xrange(1, len(tmp)+1):
        if str(i) not in p:
          return False
      return True
  return False


primes = primesfrom2to(987654321)
for prime in primes:
  if is_pandigital(prime):
    print prime
