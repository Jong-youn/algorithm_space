from icecream import ic

def solution(a, b):
    answer = 0
    length = len(a)
    ic(length)
    for i in range(length):
        print(i)
        answer += a[i]*b[i]
    return answer

ic(solution([1,2,3,4], [-3,-1,0,2])) #3
ic(solution([-1,0,1], [1,0,-1])) #-2

