from collections import deque
from icecream import ic

def solution(city):
    r = len(city)
    c = len(city[0])
    answer = [[0]*c for _ in range(r)] 
    rr = [-1, 0, 1, 0]
    cc = [0, 1, 0, -1]

    q = deque()
    for i in range(r):
        for j in range(c):
            if city[i][j] == 1:
                q.append([[i, j], 1])
                while q:
                    x, cnt = q.popleft()
                    ic(x, cnt)
                    for k in range(4):
                        nr = x[0] + rr[k]
                        nc = x[1] + cc[k]
                        if 0 <= nr < r and 0 <= nc < c:
                            if city[nr][nc] == 0:
                                answer[i][j] = cnt
                                q = deque()
                                break
                            if city[n]
                            else:
                                q.append([[nr, nc], cnt+1])
    return answer
ic(solution([[0,0,1], [1,1,1], [0,1,1]]))
ic(solution([[1,0,0], [0,1,1], [1,1,1]]))