class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indeg[v] += 1
        
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []
        
        while q:
            cur=q.popleft()
            res.append(cur)
            
            for i, j in prerequisites:
                if i==cur:
                    indeg[j]-=1
                    if indeg[j]==0:
                        q.append(j)
        
        return True if len(res)==numCourses else False