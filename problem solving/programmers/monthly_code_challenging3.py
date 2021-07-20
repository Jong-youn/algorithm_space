# 2021-06-30
# 월간 코드 챌린지2 - 110 옮기기
# https://programmers.co.kr/learn/courses/30/lessons/77886

from icecream import ic

def solution(s):
    answer = []
    def relocate(num):
        place = num.rfind('110')
        if place != -1:
            new = num[:place] + num[place+3:]
            b = new.find('111')
            if b != -1 and place > b:
                new = new[:b] + '110' + new[b:]
                relocate(new)
            elif place < b:
                
            else:
                
        else:
            return num
        
    for num in s:
        relocate(num)
        
    return answer

ic(solution(["1110","100111100","0111111010"])) #["1101","100110110","0110110111"]
