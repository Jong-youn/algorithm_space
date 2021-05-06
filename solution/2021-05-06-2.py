# 플로이드 워샬 응용(14)
# 회장 뽑기

from icecream import ic

def solution(t, friends):
    answer = [[0]*t for _ in range(t)]
    mx = 1
    for f1, f2 in friends:
        answer[f1-1][f2-1] = 1
        answer[f2-1][f1-1] = 1
    
    for l in range(t):
        for c in range(t):
            if l == c:
                continue
            for md in range(t):
                if md in (l, c) or answer[l][md] == 0 or answer[md][c] == 0:
                    continue
                point = answer[l][md] + answer[md][c]
                if answer[l][c] == 0 or answer[l][c] > (point):
                    answer[l][c] = point
                    answer[c][l] = point
                    
    candidate = [0]*t
    result = []
    mn = 50
    for i in range(t):
        candidate[i] = max(answer[i])
        if candidate[i] < mn:
            mn = candidate[i]
    for c in range(t):
        if candidate[c] == mn:
            result.append(c+1)
            
    print(mn, len(result))
    print(result)
    return answer
    

ic(solution(5, [[1, 2],[2, 3],[3, 4],[4, 5],[2, 4],[5, 3]]))

