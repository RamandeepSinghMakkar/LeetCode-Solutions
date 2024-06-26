#Time complexity: O(nlogn)
#Space complexity: O(n)

# LeetCode Question Link: https://leetcode.com/problems/ipo/description/

#502. IPO (Hard)
#Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects. 
#You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#The answer is guaranteed to fit in a 32-bit signed integer.

 

struct T {
  int pro;
  int cap;
  T(int pro, int cap) : pro(pro), cap(cap) {}
};

class Solution {
 public:
  int findMaximizedCapital(int k, int W, vector<int>& Profits,
                           vector<int>& Capital) {
    auto compareC = [](const T& a, const T& b) { return a.cap > b.cap; };
    auto compareP = [](const T& a, const T& b) { return a.pro < b.pro; };
    priority_queue<T, vector<T>, decltype(compareC)> minHeap(compareC);
    priority_queue<T, vector<T>, decltype(compareP)> maxHeap(compareP);

    for (int i = 0; i < Capital.size(); ++i)
      minHeap.emplace(Profits[i], Capital[i]);

    while (k--) {
      while (!minHeap.empty() && minHeap.top().cap <= W)
        maxHeap.push(minHeap.top()), minHeap.pop();
      if (maxHeap.empty())
        break;
      W += maxHeap.top().pro, maxHeap.pop();
    }

    return W;
  }
};
