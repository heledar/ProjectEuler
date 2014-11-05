from euler import isTriangle

f = open("words.txt", "r")
res = 0
data = f.readline()
data = data.replace('"', "")
data = data.split(",")
for word in data:
  tmp = 0
  for c in word:
    tmp += ord(c)-64
  if isTriangle(tmp):
    res += 1
print res
