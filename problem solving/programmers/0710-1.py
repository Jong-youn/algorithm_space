

from icecream import ic


def solution(n, k):
    answer = 1
    reminder = []
    t = n//10
    r = n%k
    # while len(reminder) < 9 or r not in reminder:
    #     r = n%k
    #     if r == 0:
    #         return answer
    #     reminder.append(r)
    #     nn = (r)*(10**(t))+n
    #     answer += 1
    #     ic(r, answer, reminder)
            
    if r == 0:
        return answer
    else:
        while len(reminder) < 9 or r not in reminder:
            nn = (r)*(10**(t))+n
            r = nn%k
            answer += 1
            if r == 0:
                return answer
            reminder.append(r)
            
    return -1

ic(solution(22, 9))
ic(solution(25, 15)) #3