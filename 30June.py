# Time complexity: O(sort)
# Space complexity: O(n)

# LeetCode Question Link: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/?envType=daily-question&envId=2024-06-30

# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable (Hard)

#Alice and Bob have an undirected graph of n nodes and three types of edges:
#Type 1: Can be traversed by Alice only.
#Type 2: Can be traversed by Bob only.
#Type 3: Can be traversed by both Alice and Bob.
#Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
#Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

class UnionFind:
  def __init__(self, n: int):
    self.count = n
    self.id = list(range(n))
    self.rank = [0] * n

  def unionByRank(self, u: int, v: int) -> bool:
    i = self._find(u)
    j = self._find(v)
    if i == j:
      return False
    if self.rank[i] < self.rank[j]:
      self.id[i] = j
    elif self.rank[i] > self.rank[j]:
      self.id[j] = i
    else:
      self.id[i] = j
      self.rank[j] += 1
    self.count -= 1
    return True

  def _find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self._find(self.id[u])
    return self.id[u]


class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    alice = UnionFind(n)
    bob = UnionFind(n)
    requiredEdges = 0

    for type, u, v in sorted(edges, reverse=True):
      u -= 1
      v -= 1
      if type == 3:  # Can be traversed by Alice and Bob.
        if alice.unionByRank(u, v) | bob.unionByRank(u, v):
          requiredEdges += 1
      elif type == 2:  # Can be traversed by Bob.
        if bob.unionByRank(u, v):
          requiredEdges += 1
      else:  # type == 1 Can be traversed by Alice.
        if alice.unionByRank(u, v):
          requiredEdges += 1

    return len(edges) - requiredEdges \
        if alice.count == 1 and bob.count == 1 \
        else -1
