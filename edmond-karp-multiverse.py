import collections

'''
Algorithm Idea:

This is a Max Flow problem, where we want to find the most optimised paths to travel across the space station.
Each path has a certain capacity - how many bunnies can travel through it. However, in this problem we are dealing
with multiple 'sources' (=entrances) and 'sinks' (=ends) in the graph. There are known algorithms for solving the 
Max Flow problems with single source and sink, such as Ford-Fulkerson and Edmond-Karp algorithms.

So in order to solve this problem and ensure the safety of the bunnies, I will implement the Edmond-Karp algorithm.
However, before I can do that, I must first translate this problem from multiple to single 'source' and 'sink' problem.

1. Create a single source/sink problem
Let's first create an artificial source that connects to all our entrances (=sources) with the capacity of the number of 
bunnies.
Let's also create an artificial sink to which all our ends (=sinks) are connected to with the capacities of the number
of bunnies.
Now we can create a new graph to which we add these two newly created; artificial sink and source.

2. Implement the Edmond-Karp algorithm. A more detailed explanation of the algorithm can be found here:
https://en.m.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

3. Integrate both steps into a class, where the new_graph (=graph) can be created and on which the Edmond-Karp algorithm 
can be called on! Return the max_flow :) -> bunnies are saved!
'''

def solution(entrances, exits, path):
    class Graph:
        '''
        This class represents a directed graph using
        adjacency matrix representation.
        '''

        def create_single_source_n_sink(self, old_graph, sources, sinks):
            '''Create new graph'''
            art_graph = [[0] * (len(old_graph) + 1 + 1) for _ in range(len(old_graph) + 1 + 1)]

            '''Creating an artificial source'''
            art_source = [0] * (len(old_graph) + 1 + 1)
            for source in sources:
                art_source[source + 1] = sum(old_graph[source])
            art_graph[0] = art_source

            '''Creating an artificial sink'''
            sinks_flow_dict = collections.defaultdict(int)
            for i, row in enumerate(old_graph):
                for node, bunnies in enumerate(old_graph[i]):
                    sinks_flow_dict[node] += bunnies
            for sink in sinks:
                art_graph[sink + 1][-1] = sinks_flow_dict[sink]

            '''Filling the new graph from previous'''
            for i, row in enumerate(old_graph):
                art_graph[i + 1] = [art_graph[i + 1][0]] + row + [art_graph[i + 1][-1]]

            return art_graph

        def __init__(self, graph, sources, sinks):
            self.graph = self.create_single_source_n_sink(graph, sources, sinks)
            self.row = len(self.graph)
            self.source = 0
            self.sink = len(self.graph) - 1

        def bfs(self, parent):
            '''
            Returns true if there is a path from source 'self.source' to sink 'self.sink' in our newly
            created residual graph.
            The path is stored by filling up the parent[].
            '''

            '''Initiate all the vertices as not visited'''
            visited = [False] * self.row
            queue = collections.deque()

            '''Initiate the source node as visited and enqueue it'''
            queue.append(self.source)
            visited[self.source] = True

            while queue:
                u = queue.popleft()

                '''
                Get all adjacent vertices of the dequeued vertex u
                If an adjacent has not been visited, then mark it
                visited and enqueue it
                 '''
                for ind, val in enumerate(self.graph[u]):
                    if (visited[ind] == False) and (val > 0):
                        queue.append(ind)
                        visited[ind] = True
                        parent[ind] = u

            '''
            If we reached sink in BFS starting from source, then return
            true, else false
            '''
            return visited[self.sink]

        def edmonds_karp(self):

            '''This array is filled by BFS and to store path'''
            parent = [-1] * self.row

            max_flow = 0

            '''Augment the flow while there is path from source to sink'''
            while self.bfs(parent):

                '''
                Find minimum residual capacity of the edges along the
                path filled by BFS. Or we can say find the maximum flow
                through the path found.
                '''
                path_flow = float("Inf")
                s = self.sink
                while s != self.source:
                    path_flow = min(path_flow, self.graph[parent[s]][s])
                    s = parent[s]

                '''Add path flow to overall flow'''
                max_flow += path_flow

                '''
                Update residual capacities of the edges and reverse edges
                along the path
                '''
                v = self.sink
                while v != self.source:
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = parent[v]

            return max_flow

    graph = Graph(path,entrances,exits)
    return graph.edmonds_karp()


sol = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print(sol)