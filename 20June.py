# LeetCode Queston Link: https://leetcode.com/problems/magnetic-force-between-two-balls/description/

# 1552. Magnetic Force Between Two Balls (Medium)

#In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
#Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
#Given the integer array position and the integer m. Return the required force.

class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    position.sort()

    l = 1
    r = position[-1] - position[0]

    def numBalls(force: int) -> int:
      balls = 0
      prevPosition = -force
      for pos in position:
        if pos - prevPosition >= force:
          balls += 1
          prevPosition = pos
      return balls

    while l < r:
      mid = r - (r - l) // 2
      if numBalls(mid) >= m:
        l = mid
      else:
        r = mid - 1

    return l
