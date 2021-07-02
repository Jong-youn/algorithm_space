# 2021-07-01
# Dev-Matching - 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

from icecream import ic

def solution(rows, columns, queries):
    answer = []
    board = [[j*rows + i for i in range(1, rows+1)] for j in range(columns)]
    
    def smallest(quary):
        r1, c1, r2, c2 = quary
        small = rows*columns
        r, c = r1, c1
        before = board[r][c]
        c+=1
        
        while True:
            if before < small:
                small = before
            ic(r, c)
            before, board[r][c] = board[r][c], before
            
            if (r, c) == (r1, c1):
                break
            elif c1 <= c < c2 and r == r1:
                c+=1
            elif c == c2 and r1 <= r < r2:
                r+=1
            elif c1 < c <= c2 and r == r2:
                c-=1
            elif c == c1 and r1 < r <= r2:
                r-=1
            
        return small
        
        
    for quary in queries:
        quary = list(map(lambda x: x-1, quary))
        answer.append(smallest(quary))
            
    return answer

ic(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))	#[8, 10, 25]
ic(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))	#[1, 1, 5, 3]
ic(solution(100, 97, [[1,1,100,97]])) #[1]
