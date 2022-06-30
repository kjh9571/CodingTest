import sys 
input = sys.stdin.readline
N = int(input())

sticks = [int(input()) for _ in range(N)]
##other method
# sticks = []
# for i in range(N) :
#     s = int(input())
#     sticks.append(s)
    
max = sticks[-1]
result = 1

for i in range(N) :
    if sticks[N-i-1]>max :
        result += 1
        max = sticks[N-i-1]
        # please check position : "variable name" = "variable substance "

## other method
# for i in range(len(sticks)-1,-1,-1) :
#     if sticks[i]>max :
#         result += 1 
#         max = sticks[i]

print(result)
