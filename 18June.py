#Time complexity: 𝑂 (𝑛 log𝑛 + 𝑚 log𝑚)
#Space complexity: O(n)

#Leetcode Question Link: https://leetcode.com/problems/most-profit-assigning-work/submissions/1292161122/?envType=daily-question&envId=2024-06-18

# 826. Most Profit Assigning Work (Medium)

#You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
#difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
#worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

#Every worker can be assigned at most one job, but one job can be completed multiple times.
#For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

#Return the maximum profit we can achieve after assigning the workers to the jobs.

class Solution:
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    ans = 0
    jobs = sorted(zip(difficulty, profit))
    worker.sort(reverse=1)

    i = 0
    maxProfit = 0

    for w in sorted(worker):
      while i < len(jobs) and w >= jobs[i][0]:
        maxProfit = max(maxProfit, jobs[i][1])
        i += 1
      ans += maxProfit

    return ans
