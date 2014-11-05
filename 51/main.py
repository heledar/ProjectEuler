from euler import primesFrom2To
import itertools

def findsubsets(S,m):
  return set(itertools.combinations(S, m))

primes = primesFrom2To(1000000)
found = False
for prime in primes:
  if prime < 56003:
    continue
  pStr = str(prime)
  possibilities = [str(i) for i in xrange(1, len(pStr)+1)]
  toCheck = []
  tmp = findsubsets(possibilities, 3)
  for t in tmp:
    toCheck.append(list(map(int, t)))
  for check in toCheck:
    tmpAns = []
    pList = map(int, list(pStr))
    for i in xrange(10):
      for j in check:
        pList[j-1] = i
      if int("".join(map(str, pList))) in primes and len ("".join(map(str, pList))) == len(pStr):
        tmpAns.append(int("".join(map(str, pList))))
    if len(tmpAns) == 8:
      print tmpAns
      found = True
      break
  if found:
    break
