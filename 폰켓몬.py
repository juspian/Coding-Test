# 중복되는 값을 제거하고 그 값의 길이와 n/2값을 비교한다. 
def solution(nums):
    answer = 0
    set_nums=set(nums)
    if len(set_nums)<=len(nums)/2:
        answer+=len(set_nums)
    else:
        answer+=len(nums)/2
    return answer
  
  # 다른 풀이 
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
