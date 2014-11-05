import sys, math

res = dict()
def factorial(n):
  global res
  if n in res:
    return res[n]
  if n == 0:
    return 1
  else:
    res[n] = factorial(n-1)*n
    return res[n]

ans = 0
for i in xrange(3, 50000):
  sum = 0
  for c in str(i):
    sum += factorial(int(c))
  if sum == i:
    ans += i
print ans
