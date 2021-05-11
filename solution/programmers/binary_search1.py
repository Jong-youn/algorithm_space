# 이분탐색
# 2021-05-08
# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

from icecream import ic

def solution(n, times):
    mx = max(times)*n
    mn = 1
        
    while mn <= mx:
        md = (mx+mn)//2
        result = 0
        for time in times:
            result += md//time
        if result >= n:
            res = md
            mx = md-1
        elif result < n:
            mn = md+1
    
    return res
