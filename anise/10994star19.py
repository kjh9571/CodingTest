n = int(input())
stars = [[' ' for i in range(4*n-3)]for i in range(4*n-3)]
# 빈칸으로 이루어진 행렬 공간을 리스트를 이용해 만듦

def fill_stars(n,x,y) :
    # 빈칸에 별을 찍어 넣을 함수, 열방향을 x축, 행방향을 y축이라 한다. 
    if n == 1:
        stars[y][x] = '*'
        return
    # n = 1 일때는 * 하나만 찍고 끝나도록 if 문 사용

    length = 4*n-3
    
    for i in range(length) :
        stars[y][x+i] = '*'
        stars[y+i][x] = '*'
        stars[y+length-1][x+i] = '*'
        stars[y+i][x+length-1] = '*'
    # [y][x]위치를 기준으로 ㅁ모양으로 *을 찍는다. 이때 [y][x]는 ㅁ의 왼쪽 가장 위이다.
    
    fill_stars(n-1, x+2, y+2)
    # n=1이 될때까지, 재귀 함수를 사용해 계속 안쪽으로 *을 찍는다.

fill_stars(n,0,0)
# [0][0]위치를 기준으로 시작한다.
for s in stars :
    print(''.join(s))
    # join함수 :  매개변수로 들어온 리스트를 '구분자'를 이용해 문자열로 합쳐서 반환