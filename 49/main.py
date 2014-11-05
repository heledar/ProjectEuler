from euler import *
from itertools import permutations

def t49(p):
  for n in p:
    for i in p:
      d = abs(n-i)
      tmp = [n]
      for j in p:
        if abs(n-j) == d:
          tmp.append(j)
      if len(tmp) == 3:
        print tmp
        return None

checked = set()
primes = primesFrom2To(9999)
for prime in primes:
  if prime < 1234:
    continue
  if prime in checked:
    continue
  perms = map(int, [''.join(p) for p in permutations(str(prime))])
  primePerms = set()
  for perm in perms:
    if perm in primes:
      checked.add(perm)
      primePerms.add(perm)
  if len(primePerms) > 2:
    primePerms = list(primePerms)
    primePerms.sort()
    t49(primePerms)
