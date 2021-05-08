# 그래프
# 2021-05-06
# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from icecream import ic
import timeit

from collections import defaultdict

def solution(n, edge):
    edges = defaultdict(set)
    routes = defaultdict(set)
    for f, e in edge:
        edges[f].add(e)
        edges[e].add(f)
    routes[1] = edges[1]
    check = {1}.union(edges[1])
    i = 1

    while len(check) < n:
        for next in routes[i]:
            routes[i+1].update(edges[next])
        routes[i+1].difference_update(check)
        check.update(routes[i+1])
        i+=1
    
    return len(routes[i])

startTime = timeit.default_timer()
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(10, [[1, 2], [1, 3], [2, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]))
endTime = timeit.default_timer()
print(f"{endTime - startTime} 초 소요")


