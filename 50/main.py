from euler import primesFrom2To

primes = primesFrom2To(1000000)
max = 0
ans = 0
for i in xrange(len(primes)):
  sum = 0
  prev = 0
  added = list()
  for prime in primes[i:]:
    added.append(prime)
    sum += prime
    if sum >= 1000000:
      if prev in primes and len(added) > max and len(added) > 1:
        max = len(added)
        ans = prev
        print ans
      break
    prev = sum
print ans
