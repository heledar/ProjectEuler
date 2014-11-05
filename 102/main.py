import sys, math

n = 0
f = open("triangles.txt", "r")
g = lambda x:[[int(x[0]), int(x[1])], [int(x[2]), int(x[3])], [int(x[4]), int(x[5])]]

def isIn(triangle):
    area = float(-triangle[1][1]*triangle[2][0] + triangle[0][1]*(triangle[2][0]-triangle[1][0]) + triangle[0][0]*(triangle[1][1]-triangle[2][1]) + triangle[1][0]*triangle[2][1])
    s = 1/area*(triangle[0][1]*triangle[2][0] - triangle[0][0]*triangle[2][1])
    t = 1/area*(triangle[0][0]*triangle[1][1] - triangle[0][1]*triangle[1][0])
    if s > 0 and t > 0 and (1-s-t) > 0:
        return 1
    return 0

for line in f:
    if isIn(g(line.replace("\n","").split(","))):
        n += 1
print n
