import math
from itertools import permutations
import time

startTime = time.time()
i = 0
found = False
while not found:
  i += 1
  if len(str(i)) != len(str(6*i)):
    i = int(math.pow(10, math.ceil(math.log10(float(i)))))
    continue
  else:
    perms = [int("".join(j)) for j in permutations(str(i))]
    if 2*i in perms:
      if 3*i in perms:
        if 4*i in perms:
          if 5*i in perms:
            if 6*i in perms:
              found = True
endTime = time.time()
print "The smallest integer is : "+str(i)
print "Computation took : "+str(endTime-startTime)+" seconds"
