def solution(d, budget):
    d= sorted(d)
    answer=0
    for i in range(0,len(d)):
        if sum(d[0:i+1])<=budget:
            answer+=1
    return answer
