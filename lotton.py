# Q1 Answer template https://programmers.co.kr/learn/courses/30/lessons/77484

def grade(num):
    grd=[6,6,5,4,3,2,1]
    return grd[num]

def solution(lottos, win_nums):
    answer = []
    correct=0
    hidden=0
    
    for num in lottos:
        if num==0:
            hidden+=1
        elif num in win_nums:
            correct+=1
    
    hidden+=correct
    
    answer.append(grade(hidden))
    answer.append(grade(correct))
        
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos, win_nums)
print(answer)
