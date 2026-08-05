from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        # Step 2: Find suspicious methods using BFS/DFS
        suspicious = set()
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in graph[node]:
                if nei not in suspicious:
                    queue.append(nei)

        # Step 3: Check if any outside method calls into suspicious
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # Outside method calls suspicious → cannot remove
                return list(range(n))

        # Step 4: Return remaining methods
        return [i for i in range(n) if i not in suspicious]
