import sys
from operator import itemgetter

#  N = int(input())
#  a = [list(map(int, l.split())) for l in sys.stdin]

N = 100 
a = []
for i in range(N):
    for j in range(N):
        a.append([i,j,0])
import pdb
pdb.set_trace()
max_height_pos = sorted(a, key=itemgetter(2))[-1]

for y in range(101):
    for x in range(101):
        height = max_height_pos[2] + abs(x-max_height_pos[0]) + abs(y-max_height_pos[1])

        for _x, _y, _h in a:
            if height - abs(x-_x) - abs(y-_y) < 0 and _h == 0:
                continue
            if height != _h + abs(x-_x) + abs(y-_y):
                break
        else:
            print(x, y, height)
            exit()

raise Exception("hoge")
