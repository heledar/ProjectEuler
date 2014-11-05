import time
startTime = time.time()
ans = str(pow(2, 7830457, 10000000000)*28433+1)
endTime = time.time()
print "The 10 last digits of 28433*2^7830457+1 are : "+ans[len(ans)-10:]
print "Computation took : "+str(endTime-startTime)+" seconds"
