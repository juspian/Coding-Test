# 내 풀이 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # i번째에 0이 있으면 i+1번째 인덱스에 0을 추가하고
        # 마지막 숫자를 지움
        i=0
        while i <=len(arr)-1:
            if arr[i]==0:
                arr.insert(i+1,0)
                del arr[-1]
                i+=2
            else:
                i+=1

# 다른 풀이 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):   # 뒤에서부터 차례대로 
            if i + zeroes < n:    # 남은 0의 개수와 i를 더한 값이 n보다 작으면
                arr[i + zeroes] = arr[i]   # 기존의 i번째 리스트의 값을 i+zeros에 저장한다. 
            if arr[i] == 0:    # i번째에 0이 있으면 
                zeroes -= 1   # 0의 숫자를 하나 차감하고
                if i + zeroes < n:    i+zeroes가 n보다 작으면 
                    arr[i + zeroes] = 0    i+zeroes의 인덱스를 0으로 한다. 
