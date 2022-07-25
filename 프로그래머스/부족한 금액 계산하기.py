# 내 풀이
def solution(price, money, count):
    i=0
    cost=0
    while i<count:
        i+=1
        cost+= price*i
    if cost<=money:
        answer = 0
    else:
        answer= cost-money
    return answer
    
# 다른 풀이
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))   # for로 쓰로 min으로 정리하는 방법 좋다. 
