def solution(answers):
    answer = []
    top = -1
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    total = len(answers)
    students = [A, B, C]
    
    for s in range(3):
        student_answer = len(students[s])
        grades = 0
        for i in range(total):
            pbm = i % student_answer
            ic(i, pbm, answers[i], students[s][pbm])
            if answers[i] == students[s][pbm]:
                grades += 1
        
        if grades > top:
            top = grades
            answer = [s+1]
            
        elif grades == top:
            answer.append(s+1)
    return answer

# ic(solution([1,2,3,4,5])) #[1]
# ic(solution([1,3,2,4,2])) #[1,2,3]
ic(solution([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])) #[1,2,3]
