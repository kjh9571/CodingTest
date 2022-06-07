#2839 Grid
# 최적의 해, 정당성 분석 필요
# 거스름 돈 예시처럼 리스트로 구현하려 했으나 정당성 분석(3으로만 나누어떨어짐 or -1이 출력되는 결과) 에 의해 다른 방법으로 시도. 
n = int(input())
cnt = 0

## bong = [5,3]

while (1):
  if n % 5 == 0 :
    cnt += n // 5 
    n %= 5          # n = n%5
    print(cnt)
    break
    
  n -= 3
  cnt += 1

  if n < 0:
    print(-1)
    break


