class Solution:
    def calcEquation(self, equations, values, queries):
        # Build the graph using a standard dictionary
        G = {}
        for (x, y), v in zip(equations, values):
            # Manually initialize empty dictionaries for new nodes
            if x not in G: G[x] = {}
            if y not in G: G[y] = {}
            
            # Add the directional weights (ensure floats for Python 2)
            G[x][y] = float(v)
            G[y][x] = 1.0 / v
            
        def bfs(src, dst):
            # If either variable doesn't exist in our graph, division is impossible
            if src not in G or dst not in G:
                return -1.0
                
            # Queue stores elements as a list of pairs: (current_node, cumulative_product)
            q = [(src, 1.0)]
            seen = set()
            
            for x, v in q:
                if x == dst:
                    return v
                seen.add(x)
                
                for y in G[x]:
                    if y not in seen:
                        # Multiply the current value by the edge weight to the neighbor
                        q.append((y, v * G[x][y]))
                        
            return -1.0
            
        # Run BFS for each individual query
        return [bfs(s, d) for s, d in queries]