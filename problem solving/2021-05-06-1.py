# 플로이드 워샬(13)

from icecream import ic

def solution(n, m, roads):
    answer = [['M']*n for _ in range(n)]
    
    for start, end, price in roads:
        answer[start-1][end-1] = price
    
    for l in range(n):
        for c in range(n):
            if l == c:
                answer[l][c] = 0
                continue
            for md in range(n):
                if md in (l, c) or answer[l][md] == 'M' or answer[md][c] == 'M':
                    continue
                if answer[l][c] == 'M' or answer[l][c] > (answer[l][md] + answer[md][c]):
                    answer[l][c] = answer[l][md] + answer[md][c]
                
    for i in range(n):
        for j in range(n):
            print(answer[i][j], end = ' ')
        print( )
    return answer

ic(solution(6, 9, [[1, 2, 12], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5], [6, 4, 5]]))

solution(5, 8, [[1, 2, 6],[1, 3, 3],[3, 2, 2],[2, 4, 1],[2, 5, 13],[3, 4, 5],[4, 2, 3],[4, 5, 7]]
)
