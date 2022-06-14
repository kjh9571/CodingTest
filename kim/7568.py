n = int(input()) # 덩치 리스트 개수
dungchi_list = [] # 덩치 리스트
rank_list = [] # 덩치 랭크 리스트

while n != 0: # 입력한 덩치 리스트 개수만큼 덩치 데이터 입력 받음
    a, b = map(int, input().split())
    dungchi_list.append([a,b]) # 리스트 안에 리스트 형태로 추가
    n -= 1

for i in dungchi_list:
    rank = 0
    for j in dungchi_list: 
        if i == j: # 덩치 데이터가 중복되거나 수치가 같은 경우
            continue
        else:
            if i[0] < j[0] and i[1] < j[1]: # 비교 대상인 덩치 데이터가 더 작을 경우
                rank += 1
    #print(rank+1, end=' ')
    rank_list.append(rank+1) # 랭크 리스트에 덩치 랭크 입력

print(' '.join(map(str, rank_list))) # 랭크 리스트를 빈칸으로 구분해서 출력