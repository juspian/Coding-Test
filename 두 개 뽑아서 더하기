# 내 풀이
def solution(numbers):
    d=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (int(numbers[i])+int(numbers[j])) not in d:
                d.append(numbers[i]+numbers[j])            
    answer = sorted(d)
    return answer

# 다른 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))    # set 함수를 이용하여 중복을 제거하는 방법도 좋다. 
