https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                cnt+=1
        return cnt
        
