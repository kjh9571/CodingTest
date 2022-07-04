# 시간초과 해결
# 17608 ,막대
'''
가장 마지막에 들어간 막대를 기준으로 크면 +1이 되고 커진 수가 기준으로 바뀐다는 로직으로 생각 
실행결과 시간초과 결과가 나온다
input 방식을 stdin으로 변경하여 돌렸더니 작동했다
'''
import sys
n = int(sys.stdin.readline())
stack = [ ]
sum = 1

for i in range(n):
  i = int(sys.stdin.readline())
  stack.append(i)

standard = stack[-1]

for j in range(n):
  change = stack.pop()
  if change <= standard:
    pass
  elif change > standard:
    standard = change
    sum +=1
print(sum)

