from icecream import ic

def solution(numbers):
    nums = list(numbers)
    length = len(numbers)
    answers = set()
    all_nums = set()
    res = 0

    def DFS(num, total):
        if total == length:
            if num and num != ['0']:
                answers.add(''.join(num))
        
        else:
            DFS(num + list(nums[total]), total + 1)
            DFS(num, total + 1)
    
    def shake(num):
        length_num = len(num)
        num_list = [0]*length_num
        ch = [0]*(length_num+1)
        
        def DFS_for_shake(L):
            if L == length_num:
                all_nums.add(int(''.join(num_list)))
            else:
                for idx, n in enumerate(num):
                    if ch[idx] == 0:
                        ch[idx] = 1
                        num_list[L] = n
                        DFS_for_shake(L+1)
                        ch[idx] = 0
        DFS_for_shake(0)
    
    def check(n):
        nonlocal res
        if n > 1:
            for i in range(2, int(n**0.5)):
                if n%i == 0:
                    return 
            res+=1
    
    DFS([], 0)
    for n in answers:
        shake(list(n))
    for n in all_nums:
        check(n)
    
    return res


ic(solution("17")) #3
ic(solution("011")) #2
