
from icecream import ic

def solution(numbers):
    answer = set()
    t = len(numbers)
    for i in range(t):
        for j in range(i+1, t):
            answer.add(numbers[i]+numbers[j])
            
    return sorted(list(answer))

ic(solution([2,1,3,4,1])) #[2,3,4,5,6,7]
ic(solution([5,0,2,7])) #[2,5,7,9,12]
