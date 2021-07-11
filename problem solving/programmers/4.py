from icecream import ic


def solution(r, c):
    answer = 1
    n = r+c-2
    
    if 1 in (r, c):
        ic()
        return 1
    elif r > c:
        r = c-1
    else:
        r -= 1
    
    while r != 0:
        answer *= (n/r)
        ic(n, r, answer)
        n-=1
        r-=1
    return int(answer)


ic(solution(2, 4))	#4
ic(solution(3, 3))	#6
ic(solution(5, 1))	#1
ic(solution(1, 5))	#1
ic(solution(2, 2))	#2