class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        dist = [float("inf")] * n
        dist[0] = 0
        queue = deque([0])
        inQueue = [False] * n
        inQueue[0] = True

        while queue:
            u = queue.popleft()
            inQueue[u] = False

            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    if not inQueue[v]:
                        queue.append(v)
                        inQueue[v] = True

        return dist[n - 1] if dist[n - 1] != float("inf") else -1
