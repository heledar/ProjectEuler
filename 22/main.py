import sys, math

f = open("names.txt", "r")
names = f.readline()
names = names.replace('"', '')
names = names.split(",")
names.sort()
sum = 0
i = 1
for name in names:
    tmp_score = 0
    for char in name.replace('"', ""):
        tmp_score += ord(char) - 64
    sum += tmp_score * i
    i += 1
print sum
