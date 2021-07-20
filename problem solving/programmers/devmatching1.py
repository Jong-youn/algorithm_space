from icecream import ic

def solution(lottos, win_nums):
    answer = []
    right = 0
    erase = 0
    for num in lottos:
        if num in win_nums:
            right += 1
        elif num == 0:
            erase += 1
    
    while len(answer) < 2:
        if right <= 1:
            answer.append(6)
        else:
            answer.append(7-right)
        right += erase
    return answer[::-1]


ic(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))	#[3, 5]
ic(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))	#[1, 6]
ic(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))	#[1, 1]