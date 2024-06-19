# Time complexity: O(nlog(max(bloomDay)))
# Space complexity: O(1)

#LeetCode Question Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/?envType=daily-question&envId=2024-06-19

# 1482. Minimum Number of Days to Make m Bouquets (Medium)

#You are given an integer array bloomDay, an integer m and an integer k.
#You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

class Solution:
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay) < m * k:
      return -1

    def getBouquetCount(waitingDays: int) -> int:
      bouquetCount = 0
      requiredFlowers = k
      for day in bloomDay:
        if day > waitingDays:
          
          requiredFlowers = k
        else:
          requiredFlowers -= 1
          if requiredFlowers == 0:
           
            bouquetCount += 1
            requiredFlowers = k
      return bouquetCount

    l = min(bloomDay)
    r = max(bloomDay)

    while l < r:
      mid = (l + r) // 2
      if getBouquetCount(mid) >= m:
        r = mid
      else:
        l = mid + 1

    return l
