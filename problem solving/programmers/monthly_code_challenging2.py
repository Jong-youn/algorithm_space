# 2021-06-30
# 월간 코드 챌린지2 - 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

from icecream import ic

def solution(left, right):
    nums = list(range(left, right+1))
    answer = 0
    
    for num in nums:
        if (num**0.5).is_integer():
            answer-=num
        else:
            answer+=num
    return answer


ic(solution(13, 17)) #43
ic(solution(24, 27)) #52