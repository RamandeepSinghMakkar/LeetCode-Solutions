# LeetCode Question Link: https://leetcode.com/problems/grumpy-bookstore-owner/

# 1052. Grumpy Bookstore Owner (Medium)

#There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
#On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
#The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
#Return the maximum number of customers that can be satisfied throughout the day.

class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    satisfied = sum(c for i, c in enumerate(customers) if grumpy[i] == 0)
    madeSatisfied = 0
    windowSatisfied = 0

    for i, customer in enumerate(customers):
      if grumpy[i] == 1:
        windowSatisfied += customer
      if i >= X and grumpy[i - X] == 1:
        windowSatisfied -= customers[i - X]
      madeSatisfied = max(madeSatisfied, windowSatisfied)

    return satisfied + madeSatisfied
