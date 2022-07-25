https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
# my code
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
      
# other's
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])    # It's simple!!
