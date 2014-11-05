import time
import math
startTime = time.time()
res = 0
lower = 0
n = 1

while lower < 9:
  lower = 10**((float(n-1))/float(n))
  if lower > 9:
    lower = 9
  else:
    lower = int(lower)
  res += 9-lower
  n += 1

endTime = time.time()
print "The number of n-digits integers that are the nth power of an integer is "+str(res+1)
print "Computation took "+str(endTime-startTime)+" seconds"
