class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv: 
                return False
            
            if rank[pu] >= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]

            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []