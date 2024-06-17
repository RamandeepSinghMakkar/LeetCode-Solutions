#Time complexity: O( root c)
#Space complexity: O(1)

#Leetcode Question Link: https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17

# 633. Sum of Square Numbers
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    l = 0
    r = int(sqrt(c))

    while l <= r:
      summ = l * l + r * r
      if summ == c:
        return True
      if summ < c:
        l += 1
      else:
        r -= 1

    return False
