n = int(input())
dungchi_list = []
rank_list = []

while n != 0:
    a, b = map(int, input().split())
    dungchi_list.append([a,b])
    n -= 1

for i in dungchi_list:
    rank = 0
    for j in dungchi_list:
        if i == j:
            continue
        else:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    rank_list.append(rank+1)

print(' '.join(map(str, rank_list)))