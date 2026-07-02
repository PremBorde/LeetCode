from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # dist[i][j] = minimum health lost to reach (i,j)
        dist = [[float('inf')] * n for _ in range(m)]

        # Starting cost (starting cell also counts if it is unsafe)
        dist[0][0] = grid[0][0]

        pq = [(dist[0][0], 0, 0)]  # (cost, row, col)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, r, c = heappop(pq)

            # Ignore outdated entries
            if cost > dist[r][c]:
                continue

            # Reached destination
            if r == m - 1 and c == n - 1:
                return cost < health

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heappush(pq, (new_cost, nr, nc))

        return False