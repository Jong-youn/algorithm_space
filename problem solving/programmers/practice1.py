# 연습문제
# 2021-06-10
# N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

from icecream import ic

def solution(arr):
    answer = arr[0]
    
    for obj in arr[1:]:
        cmn_divisor = 1
        min_divisor = min(answer, obj)
        
        for value in range(min_divisor, 1, -1):
            if (answer%value == 0) and (obj%value == 0):
                answer //= value
                obj //= value
                cmn_divisor = value
                
            if 1 in [answer, obj]:
                break
        answer *= (cmn_divisor * obj)
                
    return answer
  

print(solution([2,6,8,14])) #168
print(solution([1,2,3])) #6