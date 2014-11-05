import sys, math
import time
start = float(time.time())
MAX_PRIME = 1000000

def generate_prime_numbers(n):
  l = list()
  l.append(2)
  for i in xrange(3, n+1, 2):
    t = True
    for j in l:
      if j > math.sqrt(i):
        break
      if i%j == 0:
        t = False
    if t == True:
      l.append(i)
  return l

def circulars(n):
  ans = []
  tmp =str(n)
  for i in xrange(len(tmp)):
    ans.append(int(tmp[i:] + tmp[:i]))
  return ans

primes = generate_prime_numbers(MAX_PRIME)
checked = set()
circularPrimes = []
count = 0
for prime in primes:
  if prime in checked:
    continue
  test = True
  for circ in circulars(prime):
    if circ not in primes:
      test = False
  if test == True:
    count += 1
    circularPrimes.append(prime)
print circularPrimes
print "Answer is : "+str(count)
print "Processing took "+str(float(time.time())-start)
