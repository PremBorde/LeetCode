from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = defaultdict(list)
        maxCost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            maxCost = max(maxCost, c)

        def check(limit):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]

            while pq:
                cost, u = heapq.heappop(pq)

                if cost > dist[u]:
                    continue

                if u == n - 1:
                    return cost <= k

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    nc = cost + w

                    if nc < dist[v]:
                        dist[v] = nc
                        heapq.heappush(pq, (nc, v))

            return False

        lo = 0
        hi = maxCost
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans