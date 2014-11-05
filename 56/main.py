import time
startTime = time.time()

max = 0
for i in xrange(1, 100):
  for j in xrange(1, 100):
    dsum = sum(int(n) for n in str(i**j))
    if dsum > max:
      max = dsum
endTime = time.time()

print "Biggest digit sum in a^b for a,b < 100 is "+str(max)
print "Computation took "+str(endTime-startTime)+" seconds"
