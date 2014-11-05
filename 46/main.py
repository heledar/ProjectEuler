import euler
import math

primes = euler.primesFrom2To(10000)
found = False
res = 7
while not found:
  res += 2
  t = 0
  for prime in primes:
    if prime > res:
      break
    t = math.sqrt((float(res-prime))/2)
    if int(t) == t:
      break
  if not int(t) == t:
    found = True
print res
