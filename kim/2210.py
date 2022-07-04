graph = []
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx <= -1 or nx >= 5 or ny <= -1 or ny >= 5:
            continue
        else:
            dfs(nx,ny, num + graph[nx][ny])
            
for i in range(5):
    graph.append(list(map(str, input().split())))
                      
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
        
print(len(result))