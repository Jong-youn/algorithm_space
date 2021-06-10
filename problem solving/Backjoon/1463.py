# Dynamic Programming
# 2021-05-02
# 1로 만들기 
# https://www.acmicpc.net/problem/1463
# top-down

import timeit

def solution(num):
    if dp[num] == -1:
        a = []
        if num%3 == 0:
            a.append(solution(num//3))
        if num%2 == 0:
            a.append(solution(num//2))
        a.append(solution(num-1))
        dp[num] = min(a) + 1
    return dp[num]

if __name__ == "__main__":
    startTime = timeit.default_timer()
    N = int(input())
    dp = [0, 0] + [-1]*(N-1)
    print(solution(N))
    endTime = timeit.default_timer()
    print(f"{endTime - startTime} 초 소요")

