from icecream import ic

def solution(n):
    ant = ['1']
    
    def nxt(num):
        ans = ''
        a = ''
        total = 1
        for n in num:
            if a == n:
                total +=1
            else:
                if a != '':
                    ans += a+str(total)
                    total = 1
                a = n
        ans += a + str(total)
        return ans
        
    while len(ant) < n:
        ant.append(nxt(ant[-1]))
    
    return ant[n-1]



ic(solution(2)) #	"11"
ic(solution(5)) #	"122111"