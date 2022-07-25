# 내 코드: 직접 3진법 계산
def solution(n):
    a=''
    b=[]
    while n//3!=0:
        a+=str(n%3)
        n//=3
    a+=str(n)
    a=a[::-1] # 3진법 변환
    a=a[::-1] # 앞뒤 반전
    i=0
    while i<len(a):  # 10진법으로 표현
        for j in range(len(a)-1,-1,-1):
            b.append(int(a[i])*(3**j))
            i+=1
    return sum(b)

# 다른 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)   # int('문자열',해당 진법) -> 10진법의 수로 변환
    return answer
