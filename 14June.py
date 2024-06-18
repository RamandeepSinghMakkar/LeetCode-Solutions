#Time complexity: O(sort)
#Space complexity: O(sort)
#Leetcode Question Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14

#945. Minimum Increment to Make Array Unique (Medium)
#You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1. Return the minimum number of moves to make every value in nums unique. The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
  def minIncrementForUnique(self, nums: List[int]) -> int:
    ans = 0
    minAvailable = 0

    for num in sorted(nums):
      ans += max(minAvailable - num, 0)
      minAvailable = max(minAvailable, num) + 1

    return ans
