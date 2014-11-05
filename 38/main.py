import sys, math

def isPandigital(n):
  tmp = str(n)
  if "0" in tmp:
    return False
  if len(tmp) == 9:
      p = dict()
      for c in tmp:
        if c not in p:
          p[c] = True
      if len(p) == 9:
        return True
  return False

ans = []
for i in xrange(1, 100000):
  tmp = str(i)
  j = 2
  while len(tmp) < 9:
    tmp = "".join([tmp, str(j*i)])
    j += 1
  if len(tmp) > 9:
    continue
  else:
    if isPandigital(tmp):
      ans.append(tmp)
ans.sort()
print int(ans[len(ans)-1])
