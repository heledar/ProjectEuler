import time
import itertools
startTime = time.time()

fcache = dict()

def squareChain(n):
  global fcache
  if n in fcache:
    return fcache[n]
  s = sum([int(i)**2 for i in str(n)])
  fcache[n] = s
  return s

ans = 0
cache = dict()
for i in xrange(10000000, 1, -1):
  if i in cache:
    continue
  else:
    perms = set(int("".join(perm)) for perm in itertools.permutations(str(i)))
    tmp = int(i)
    while (not tmp == 1 and not tmp == 89):
      tmp = squareChain(tmp)
    if tmp == 89:
      for perm in perms:
        cache[perm] = True
        ans += 1
    else:
      for perm in perms:
        cache[perm] = False
endTime = time.time()

print "The number of starting numbers below ten million that arrive to 89 is "+str(ans)
print "Computation took "+str(endTime-startTime)+" seconds"
