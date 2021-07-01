# 2021-06-29
# 월간 코드 챌린지2 - 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

from icecream import ic

def solution(numbers):
    answer = []
    for number in numbers:
        binary = format(number, 'b')
        if binary.find('0') == -1:
            ans = int('10' + binary[1:], 2)
            answer.append(ans)
        else:
            for i in range(len(binary)-1, -1, -1):
                if binary[i] == '0':
                    if i == len(binary)-1:
                        ans = int(binary[:i] + '1', 2)
                        answer.append(ans)
                    else:
                        ans = int(binary[:i] + '10' + binary[i+2:], 2)
                        answer.append(ans)
                    break
    return answer



ic(solution([2,7])) #[3,11]
ic(solution([10,7])) #[3,11]
