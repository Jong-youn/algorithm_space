# 그래프
# 2021-05-05
# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

from icecream import ic

def solution(n, results):
    answer = 0
    points = [[0]*n for _ in range(n)]
    WIN = 1
    LOSE = 2
    
    for w, l in results:
        for i in range(n):
            if i == (l-1):
                points[w-1][i] = WIN
            if i == (w-1):
                points[l-1][i] = LOSE
            
            if points[w-1][i] == LOSE:
                points[l-1][i] = LOSE
                points[i][l-1] = WIN
            if points[l-1][i] == WIN:
                points[w-1][i] = WIN
                points[i][w-1] = LOSE
        ic(points)
    for point in points:
        if point.count(0) == 1:
            answer += 1
    return answer


# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5, [[1, 3], [1, 4], [2, 5], [3, 5], [2, 3], [1, 2], [5, 4]]))
# print(solution(5, [[1,2], [2,3], [3,4], [4,5]]))
# print(solution(5, [[1,2], [2,3], [2,4], [2,5]]))
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
# print(solution(3, [[1,2],[1,3]]), 1)
# print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
# print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
# print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
# print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
# print(solution(3,[[3,2],[3,1]]), 1)
# print(solution(4, [[1,2],[1,3],[3,4]]), 1)
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(5, [[4,3],[4,2],[3,2],[1,2],[2,5]]), 2)
print(solution(8, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]] ), 8)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
