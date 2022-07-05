https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/
  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
