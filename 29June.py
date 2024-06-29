#29 June 20224

# Time complexity: O(∣edges∣)
# Space complexity: O(∣edges∣)

# 2192. All Ancestors of a Node in a Directed Acyclic Graph (Medium)

#LeetCode Question Link: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/?envType=daily-question&envId=2024-06-29

# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.
 

class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    ans = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]

    for u, v in edges:
      graph[u].append(v)

    def dfs(u: int, ancestor: int, seen: Set[int]) -> None:
      seen.add(u)
      for v in graph[u]:
        if v in seen:
          continue
        ans[v].append(ancestor)
        dfs(v, ancestor, seen)

    for i in range(n):
      dfs(i, i, set())

    return ans
