import time
startTime = time.time()

def frequencyAnalysis(data):
  tmp = dict()
  for c in data:
    if c in tmp:
      tmp[c] += 1
    else:
      tmp[c] = 1
  res = list()
  while len(tmp) > 0:
    max = 0
    val = 0
    for c in tmp:
      if tmp[c] > max:
        val = c
        max = tmp[c]
    res.append(val)
    del tmp[val]
  return res

def encrypt(data, key):
  k = key*(len(data)/len(key)+1)
  res = list()
  for a,b in zip(data, k):
    res.append(chr(a^b))
  return "".join(res)


f = open("cipher.txt", "r")
line = f.readline()
data = map(int, line.replace("\n", "").split(","))
temp = [[], [], []]
for i in xrange(len(data)):
  temp[i%3].append(data[i])
ans = "".join([chr(frequencyAnalysis(temp[i])[1]^ord('e')) for i in xrange(0, 3)])
print ans
print encrypt(data, [ord(i) for i in ans])


endTime = time.time()
