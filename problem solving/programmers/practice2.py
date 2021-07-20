# 2021-07-20
# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

from icecream import ic

# def solution(arr1, arr2):
#     l1 = len(arr1)
#     l2 = len(arr1[0])
#     l3 = len(arr2[0])
#     answer = []
    
#     for i in range(l1):
#         answer.append([])
#         for k in range(l3):
#             total = 0
#             for j in range(l2):
#                 total += arr1[i][j]*arr2[j][k]
#                 ic(total)
#             ic(i, j, j, k, total)
#             answer[-1].append(total)
            
#     return answer

def solution(A, B):
    ic(*B)
    ic(list(zip(*B)))
    return [[ sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

ic(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]	)) #[[15, 15], [15, 15], [15, 15]]
ic(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],	[[5, 4, 3], [2, 4, 1], [3, 1, 1]])) #[[22, 22, 11], [36, 28, 18], [29, 20, 14]]