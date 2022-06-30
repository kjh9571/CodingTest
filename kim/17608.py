import sys

h = [int(sys.stdin.readline()) for i in range(int(input()))]
cnt = 0

h2 = list(reversed(h))
cp = h2[0]

for i in h2:
    if i > cp:
        cp = i
        cnt += 1

print(cnt+1)

    