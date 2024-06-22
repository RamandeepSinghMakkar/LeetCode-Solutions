#LeetCode Question Link: https://leetcode.com/problems/count-number-of-nice-subarrays/?envType=daily-question&envId=2024-06-22
#1248. Count Number of Nice Subarrays (Medium)

#Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#Return the number of nice sub-arrays.

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def numberOfSubarraysAtMost(k: int) -> int:
      ans = 0
      l = 0
      r = 0

      while r <= len(nums):
        if k >= 0:
          ans += r - l
          if r == len(nums):
            break
          if nums[r] & 1:
            k -= 1
          r += 1
        else:
          if nums[l] & 1:
            k += 1
          l += 1
      return ans

    return numberOfSubarraysAtMost(k) - numberOfSubarraysAtMost(k - 1)
