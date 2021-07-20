from icecream import ic

#1
# def solution(n):
#     def change3(num, res):
#         num, r = divmod(num, 3)
#         if num == 0:
#             return str(r)+res
#         else:
#             return change3(num, str(r)+res)
#     a = int(change3(n, '')[::-1])
    
#     return int(str(a), 3)

#2
def solution(n):
    res = ''
    while n:
        res += str(n%3)
        n = n//3
    
    return int(res, 3)

ic(solution(45)) #7
ic(solution(125)) #229