# Dynamic Programming
# 2021-05-02
# 1로 만들기 
# https://www.acmicpc.net/problem/1463
# top-down

import timeit

from icecream import ic
def solution(num):
    dp = [0]*(N+1)
    for i in range(2, num+1):
        a = []
        if i%3 == 0:
            a.append(dp[i//3])
        if i%2 == 0:
            a.append(dp[i//2])
        a.append(dp[i-1])
        dp[i] = min(a) + 1
    return dp[num]

if __name__ == "__main__":
    startTime = timeit.default_timer()
    N = int(input())
    print(solution(N))
    endTime = timeit.default_timer()
    print(f"{endTime - startTime} 초 소요")
