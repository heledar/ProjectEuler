from euler import isPalyndromic
import time
startTime = time.time()

ans = 0
for i in xrange(1, 10000):
  tmp = i
  for j in xrange(50):
    tmp += int(str(tmp)[::-1])
    if isPalyndromic(tmp):
      break
  if not isPalyndromic(tmp):
    ans += 1
endTime = time.time()

print "The number of Lychrel numbers below 10000 is : "+str(ans)
print "Computation took "+str(endTime-startTime)+" seconds"
