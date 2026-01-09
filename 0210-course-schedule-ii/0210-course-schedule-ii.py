class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u) 
            indeg[u] += 1
        
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []
        
        while q:
            cur=q.popleft()
            res.append(cur)
            
            for neighbor in adj[cur]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
        
        return res if len(res)==numCourses else []