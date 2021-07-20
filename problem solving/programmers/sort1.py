from icecream import ic
from collections import defaultdict, deque

def solution(numbers):
    answer = ''
    nums = deque(sorted(list(map(str, numbers)), reverse=True))
    ic(nums)
    n1 = nums.popleft()
    while nums:
        n2 = nums.popleft()
        if n1+n2 >= n2+n1:
            answer+=n1
            n1 = n2
        else:
            answer+=n2
    return answer+n1

ic(solution([6, 10, 2])) #"6210"
ic(solution([3, 30, 34, 5, 9])) #"9534330"
ic(solution([19,18,17,16,15,14,13,12,11,10,1]))
ic(solution([7, 70, 70, 70, 70, 7])) #이게 문제임...솔팅부터 고쳐야됨

#     answer = '0'
#     a = len(numbers)
#     def dfs(at, end):
#         nonlocal answer
#         if end == a:
#             if int(at) > int(answer):
#                 answer = at
#                 return True
            
#         for i in range(end, a):
#             print(at)
#             if dfs(at + str(numbers[i]), end+1):
#                 break
#     dfs('', 0)