# 덩치 7568
# 구현→ 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭
n= int(input())
wh = []
for i in range(n): 
  w,h = map(int,input().split())
  wh.append( (w,h) ) # ( )

for a in wh:
  sort = 1
  for b in wh:
    if a[0] < b[0] and a[1] < b[1]: # & , and랑 다르다..
      sort += 1
  print(sort,end=" ")


  #46.165 +1,46.165 +1, x , 46.165 +1 , all +4
