class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m=len(isConnected)
        visited=[False]*m
        provinceCount=0

        def dfs(city):
            visited[city]=True

            for neighbour in range(m):
                if isConnected[city][neighbour]==1 and not visited[neighbour]:
                    dfs(neighbour)

        for i in range(m):
            if not visited[i]:
                provinceCount+=1
                dfs(i)
        return provinceCount