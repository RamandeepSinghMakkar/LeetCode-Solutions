# Time complexity: O(n)
#Space complexity: O(1)
#Leetcode Question Link: https://leetcode.com/problems/patching-array/description/?envType=daily-question&envId=2024-06-16

# 330. Patching Array (Hard)

#Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
#Return the minimum number of patches required.

from typing import List

class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    ans = 0
    i = 0  
    miss = 1  

    while miss <= n:
      if i < len(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      else:
        miss += miss
        ans += 1

    return ans
