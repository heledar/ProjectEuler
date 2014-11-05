import sys, math
MAX_PRIME = 10000

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

primes = generate_prime_numbers(MAX_PRIME)
ans = []
for prime in primes:
  test = True
  for i in xrange(1, len(str(prime))):
    if int(str(prime)[i:]) not in primes or int(str(prime)[:i]) not in primes:
      test = False
  if test:
    ans.append(prime)
ans.remove(2)
ans.remove(3)
ans.remove(5)
ans.remove(7)
print sum(ans)
