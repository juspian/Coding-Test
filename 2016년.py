def solution(a, b):
    days=["SUN","MON","TUE", "WED", "THU", "FRI","SAT"]
    mon=[0,3,1,3,2,3,2,3,3,2,3,2]
    answer = 0
    answer+=sum(mon[0:a])  #월
    answer+=b-1   #일
    answer= (answer+5)%7
    answer=days[answer]
    return answer
