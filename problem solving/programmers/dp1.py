# Dynamic Programming
# 2021-05-11
# 정수삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for top in range(1, len(triangle)):
        for n in range(1, top):
            triangle[top][n] += max(triangle[top-1][n-1], triangle[top-1][n])
        triangle[top][0] += triangle[top-1][0]
        triangle[top][-1] += triangle[top-1][-1]
        print(triangle[top])
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) #30