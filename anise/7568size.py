# N 입력받기
N = int(input())
data =[]
height = []
weight = []
rank = []
# 한 줄 씩 입력받아 리스트에 추가
for i in range(N) :
    x,y = map(int,input().split())
    data.append((x,y))

# 
for i in data :
    height.append(i[0])
    weight.append(i[1])
print(height, weight)
# count = N
# for i in height :
#     for j in range(len(height) - i) :
#         if (height[i] > height[i+j]) | (weight[i] > weight[i+j]) :
#             count-=1
#         else :
#             break
#     rank.append(count)
#     count = N
# print(rank)