class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Build adjacency list
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete = 0

        # DFS to explore one connected component
        def dfs(node):

            visited.add(node)

            nodes = 1                     # Number of nodes in this component
            edge_count = len(graph[node]) # Degree of current node

            for nei in graph[node]:

                if nei not in visited:
                    n_nodes, n_edges = dfs(nei)
                    nodes += n_nodes
                    edge_count += n_edges

            return nodes, edge_count

        # Visit every component
        for i in range(n):

            if i not in visited:

                nodes, edge_count = dfs(i)

                # Every edge counted twice (u->v and v->u)
                edge_count //= 2

                # Expected edges in a complete graph
                if edge_count == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete