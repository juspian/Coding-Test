# 내 풀이
def solution(arr, divisor):
    answer = []
    for i  in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
        answer= sorted(answer)
    if not answer:
        answer= [-1]
    return answer

# 다른 풀이 
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

# 다른 풀이
def solution(arr, divisor):
    answer = []

    for i in arr: 
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer = [-1]

    answer.sort()        
    return answer
