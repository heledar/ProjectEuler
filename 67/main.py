from euler import maxSumPath
import time

startTime = time.time()
f = open("triangle.txt", "r")
L = []
for line in f:
  line = line.replace("\n","")
  L.append(map(int,line.split(" ")))
ans = maxSumPath(L)
endTime = time.time()
print "The largest sum in the triangle is: "+str(ans)
print "Computation took: "+str(endTime-startTime)+" seconds"
