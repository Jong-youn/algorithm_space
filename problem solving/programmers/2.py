from icecream import ic


def solution(fire, humans, k):
    answer = 0
    fx, fy = fire
    
    for x, y in humans:
        if ((fx-x)**2+(fy-y)**2)**0.5 <= k:
            answer +=1
    return answer



ic(solution([0, 0],	[[-100, 200], [50, 50], [-400, -300], [450, -100], [500, 500], [-300, 600], [0, -550]], 500))	#4
ic(solution([50, 0],	[[100, 0], [-40, -30], [10, 80], [0, -100]], 100))	#3