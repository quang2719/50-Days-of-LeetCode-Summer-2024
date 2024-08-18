class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def f(cond):
            g = defaultdict(list)
            indeg = [0] * (k + 1)
            for a, b in cond:
                g[a].append(b)
                indeg[b] += 1
            q = deque([i for i, v in enumerate(indeg[1:], 1) if v == 0])
            res = []
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    res.append(i)
                    for j in g[i]:
                        indeg[j] -= 1
                        if indeg[j] == 0:
                            q.append(j)
            return None if len(res) != k else res

        row = f(rowConditions)
        col = f(colConditions)
        if row is None or col is None:
            return []
        ans = [[0] * k for _ in range(k)]
        m = [0] * (k + 1)
        for i, v in enumerate(col):
            m[v] = i
        for i, v in enumerate(row):
            ans[i][m[v]] = v
        return ans

############

# 2392. Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0] * k for _ in range(k)]
        
        def topoSort(A):
            adj = [[] for _ in range(k + 1)] 
            
            for a, b in A:
                adj[a].append(b)
            
            seen = [False] * (k + 1)
            order = []
            
            def dfs(x):
                if seen[x]: return
                
                seen[x] = True
                
                for nei in adj[x]:
                    if not seen[nei]:
                        dfs(nei)
                
                order.append(x)
            
            for x in range(1, k + 1):
                dfs(x)
            
            order.reverse()
            M = {j: i for i, j in enumerate(order)}
            
            if all(M[i] < M[j] for i, j in A):
                return order
            
            return None
        
        R = topoSort(rowConditions)
        C = topoSort(colConditions)
        
        if R is None or C is None:
            return []
        
        RM = {j : i for i, j in enumerate(R)}
        CM = {j : i for i, j in enumerate(C)}
        
        for x in range(1, k + 1):
            res[RM[x]][CM[x]] = x
            
        return res