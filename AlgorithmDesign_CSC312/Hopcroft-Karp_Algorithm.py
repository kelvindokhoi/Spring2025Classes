# Hopcroft-Karp Algorithm (Maximum Matching Algorithm for Bipartite Graph):

from collections import defaultdict, deque
import math

class BipartiteMatching:
    def __init__(self, u, v, edges):
        # u: number of vertices in set U (Set 1)
        # v: number of vertices in set V (Set 2)
        # edges: list of tuples (u_idx, v_idx) representing edges from U to V
        self.u = u
        self.v = v
        self.graph = defaultdict(list)  # Directed adjacency list (U -> V)
        self.pair_u = [None] * u  # Matching for U
        self.pair_v = [None] * v  # Matching for V
        self.dist = []  # Distance labels for BFS
        for u_idx, v_idx in edges:
            self.graph[u_idx].append(v_idx)

    def bfs(self):
        self.dist = [float('inf')] * (self.u + self.v + 1)
        queue = deque()
        for u in range(self.u):
            if self.pair_u[u] is None:
                self.dist[u] = 0
                queue.append(u)
        found = False
        while queue:
            u = queue.popleft()
            if u < self.u:  # Vertex in U
                for v in self.graph[u]:
                    if self.pair_v[v] is None:
                        if self.dist[self.u + v] == float('inf'):
                            self.dist[self.u + v] = self.dist[u] + 1
                            queue.append(self.u + v)
                    else:
                        u2 = self.pair_v[v]
                        if self.dist[u2] == float('inf'):
                            self.dist[u2] = self.dist[u] + 1
                            queue.append(u2)
            else:  # Vertex in V
                v = u - self.u
                if self.pair_v[v] is not None:
                    u2 = self.pair_v[v]
                    if self.dist[u2] == float('inf'):
                        self.dist[u2] = self.dist[u] + 1
                        queue.append(u2)
                else:
                    found = True
        return found

    def dfs(self, u):
        if u >= self.u:  # Vertex in V
            return True
        for v in self.graph[u]:
            if self.dist[self.u + v] == self.dist[u] + 1:
                if self.dfs(self.u + v):
                    self.pair_u[u] = v
                    self.pair_v[v] = u
                    return True
        self.dist[u] = float('inf')
        return False

    def hopcroft_karp(self):
        matching = 0
        matching_pairs = []
        while self.bfs():
            for u in range(self.u):
                if self.pair_u[u] is None and self.dfs(u):
                    matching += 1
        for u in range(self.u):
            if self.pair_u[u] is not None:
                matching_pairs.append((u, self.pair_u[u]))
        return matching, matching_pairs

def find_maximum_matching(set1, set2, threshold):
    # set1: list of (x, y) points for Set 1 (U)
    # set2: list of (x, y) points for Set 2 (V)
    # threshold: minimum distance for an edge
    u = len(set1)  # Size of U
    v = len(set2)  # Size of V
    edges = []

    # Construct bipartite graph: edge exists if distance > threshold
    for i, p1 in enumerate(set1):
        for j, p2 in enumerate(set2):
            if math.dist(p1,p2) >= threshold:
                edges.append((i, j))  # Directed edge from U to V

    # Run Hopcroft-Karp
    bm = BipartiteMatching(u, v, edges)
    matching_size, matching_pairs = bm.hopcroft_karp()

    return matching_size, matching_pairs

# Example usage
if __name__ == "__main__":
    # Set 1 and Set 2 points
    set1 = [(0, 0), (1, 2), (-1, 2)]  # U vertices
    set2 = [(0, 1), (-1, -1), (1, -1)]  # V vertices
    threshold = 3.1

    # Find maximum matching
    matching_size, matching_pairs = find_maximum_matching(set1, set2, threshold)

    # Output results
    print(f"Maximum matching size: {matching_size}")
    print("Matching pairs (Set 1 point -> Set 2 point):")
    for u_idx, v_idx in matching_pairs:
        print(f"{set1[u_idx]} -> {set2[v_idx]}")