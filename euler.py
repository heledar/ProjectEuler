import numpy
import math

def primesFrom2To(n):
  """ Input n>=6, Returns a array of primes, 2 <= p < n """
  sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
  for i in xrange(1,int(n**0.5)/3+1):
    if sieve[i]:
      k=3*i+1|1
      sieve[       k*k/3     ::2*k] = False
      sieve[k*(k-2*(i&1)+4)/3::2*k] = False
  return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def isTriangle(n):
  d = 1+8*n
  res = (1+math.sqrt(float(d)))/2
  if res == math.floor(res):
    return int(res)-1
  else:
    return 0

def isPandigital(n):
  tmp = str(n)
  a = [False]*10
  for i in xrange(len(tmp)):
    if a[int(tmp[i])]:
      return False
    else:
      a[int(tmp[i])] = True
  return True

def isDivisible(n, div):
  if n%div == 0:
    return True
  return False

def isPentagonal(n):
  if math.sqrt(1+24*float(n)) % 6 == 5:
    return True
  return False

def maxSumPath(L):
  tmp = list(L)
  for i in xrange(len(tmp)-2, -1, -1):
    for j in xrange(0, len(tmp[i])):
      tmp[i][j] += max(tmp[i+1][j], tmp[i+1][j+1])
  return tmp[0][0]

def isPalyndromic(n):
  tmp = str(n)
  l = len(tmp)
  for i in xrange(0, l/2+1):
    if not tmp[i] == tmp[l-i-1]:
      return False
  return True
