import time
startTime = time.time()

NMAX = 100
L = [[1], [1, 1]]
ans = 0
for i in xrange(1, NMAX):
  tmp =[1]
  for j in xrange(len(L[i])-1):
    a = L[i][j]+L[i][j+1]
    if a > 1000000:
      ans += 1
    tmp.append(a)
  tmp.append(1)
  L.append(tmp)

endTime = time.time()
print "The number of Cnk sup to 1M is "+str(ans)
print "Computation took "+str(endTime - startTime)+" seconds"
