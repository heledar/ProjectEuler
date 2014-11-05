import time
startTime = time.time()
n = 1000
num = 2
den = 1
ans = 0
for i in xrange(n):
    tmp = num
    num = den+2*num
    den = tmp
    if len(str(num-den)) > len(str(den)):
        ans += 1
endTime = time.time()
print "Answer to problem 57 is "+str(ans)
print "Computation took "+str(endTime-startTime)+" seconds"
