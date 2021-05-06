# Dynamic Programming
# 2021-05-03
# 스티커
# https://www.acmicpc.net/problem/9465
# top-down

import timeit
from icecream import ic

def solution(num, stickers):
    answer = 0
    rw = [1, 0, -1, 0]
    cl = [0, 1, 0, -1]
    
    for i in range(2):
        for j in range(num):
            if all(stickers[i][j] >= stickers[i+cl[k]][j+rw[k]] 
                    for k in range(4) 
                    if 0 <= (i+cl[k]) < 2 and 0 <= (j+rw[k]) < num
                ):
                answer += stickers[i][j]
                for k in range(4):
                    if 0 <= (i+cl[k]) < 2 and 0 <= (j+rw[k]) < num:
                        stickers[i+cl[k]][j+rw[k]] = 0
                stickers[i][j] = 0
    
    if stickers:
        answer += (sum(stickers[0]) + sum(stickers[1]))
    return answer

if __name__ == "__main__":
    print('답: ', solution(5, [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]))
    # tests = int(input())
    # for test in range(tests):
    #     num = int(input())
    #     startTime = timeit.default_timer()
        
    #     stickers = [list(map(int, input().split()))]
    #     stickers.append(list(map(int, input().split())))
        
    #     print('답: ', solution(num, stickers))
    #     endTime = timeit.default_timer()
    #     print(f"{endTime - startTime} 초 소요")
    
    #[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]
    #7, [[10, 30, 10, 50, 100, 20, 40], [20, 40, 30, 50, 60, 20, 80]]

