# Time complexity: O(n)
# Space complexity:O(1)

# LeetCode Question Link: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

# 995. Minimum Number of K Consecutive Bit Flips (Hard)
#You are given a binary array nums and an integer k.
#A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
#A subarray is a contiguous part of an array.
  
class Solution:
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    ans = 0
    flippedTime = 0

    for i, num in enumerate(nums):
      if i >= k and nums[i - k] == 2:
        flippedTime -= 1
      if flippedTime % 2 == num:
        if i + k > len(nums):
          return -1
        ans += 1
        flippedTime += 1
        nums[i] = 2

    return ans
