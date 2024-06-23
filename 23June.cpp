#LeetCode Question Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/?envType=daily-question&envId=2024-06-23

# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)
#Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

class Solution {
 public:
  int longestSubarray(vector<int>& nums, int limit) {
    int ans = 1;
    deque<int> minQ;
    deque<int> maxQ;

    for (int l = 0, r = 0; r < nums.size(); ++r) {
      while (!minQ.empty() && minQ.back() > nums[r])
        minQ.pop_back();
      minQ.push_back(nums[r]);
      while (!maxQ.empty() && maxQ.back() < nums[r])
        maxQ.pop_back();
      maxQ.push_back(nums[r]);
      while (maxQ.front() - minQ.front() > limit) {
        if (minQ.front() == nums[l])
          minQ.pop_front();
        if (maxQ.front() == nums[l])
          maxQ.pop_front();
        ++l;
      }
      ans = max(ans, r - l + 1);
    }

    return ans;
  }
};
