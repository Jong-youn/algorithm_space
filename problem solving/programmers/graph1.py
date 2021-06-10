# 그래프
# 2021-05-05
# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

from icecream import ic

#1
# def solution(n, results):
#     answer = 0
#     points = [[0]*n for _ in range(n)]
#     WIN = 1
#     LOSE = 2
    
#     for w, l in results:
#         w-=1 
#         l-=1
#         points[w][l] = WIN
#         points[l][w] = LOSE
#         # for i in range(n):
#         #     if points[w][i] == LOSE:
#         #         points[l][i] = LOSE
#         #         points[i][l] = WIN
#         #     if points[l][i] == WIN:
#         #         points[w][i] = WIN
#         #         points[i][w] = LOSE
#         # ic(w, l, i, points)

#     for l in range(n): 
#         for c in range(n): 
#             if l == c:
#                 continue
#             for md in range(n): 
#                 if md in (l, c):
#                     continue
#                 if points[l][md] == WIN and points[md][c] == WIN:
#                     points[l][c] = WIN
#                     points[c][l] = LOSE
#                 if points[l][md] == LOSE and points[md][c] == LOSE:
#                     points[l][c] = LOSE
#                     points[c][l] = WIN

#     for point in points:
#         if point.count(0) == 1:
#             answer += 1
#     return answer

#2
# def solution(n, results):
#     answer = 0
#     points = [[0]*n for _ in range(n)]
#     WIN = 1
#     LOSE = 2
    
#     for w, l in results:
#         w-=1 
#         l-=1
#         points[w][l] = WIN
#         points[l][w] = LOSE
#         for i in range(n):
#             if points[w][i] == LOSE:
#                 points[l][i] = LOSE
#                 points[i][l] = WIN
#             if points[l][i] == WIN:
#                 points[w][i] = WIN
#                 points[i][w] = LOSE

#     for point in points:
#         if point.count(0) == 1:
#             answer += 1
#     return answer

#3
from collections import defaultdict

def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)
    answer = 0
    
    for w, l in results:
        win[w].add(l)
        lose[l].add(w)
    
    for i in range(1, n+1):
        for loser in win[i]:
            lose[loser].update(lose[i])
        for winner in lose[i]:
            win[winner].update(win[i])
        ic(win, lose)
    
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == (n-1):
            answer+=1
    
    return answer

print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(3, [[1,2], [2,3], [3,1]]), 0)
# print(solution(4, [[1,2],[2,3],[1,4]]), 1)
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5, [[1, 3], [1, 4], [2, 5], [3, 5], [2, 3], [1, 2], [5, 4]]))
# print(solution(5, [[1,2], [2,3], [3,4], [4,5]]))
# print(solution(5, [[1,2], [2,3], [2,4], [2,5]]))
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
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
# print(solution(5, [[4,3],[4,2],[3,2],[1,2],[2,5]]), 2)
# print(solution(8, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]] ), 8)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)