import sys, math
MAX = 852000

def decimal(n):
  found = 0
  prev = 0
  val = 0
  while not found:
    val += 1
    sum = 0
    for i in xrange(1, val+1):
      sum += int(math.pow(10, i-1)*9*i)
    if n <= sum:
      tmp = int(math.ceil(float(n-prev)/val))
      rest = (n-prev) % val
      a = str(int(tmp+math.pow(10, val-1))-1)
      return int(a[rest-1])
    prev = sum

l = list()
for i in xrange(7):
  l.append(int(math.pow(10, i)))

ans = 1
for i in l:
  ans *= decimal(i)
print ans
