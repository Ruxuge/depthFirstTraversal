from collections import defaultdict


class Alg:

    # Constructor
    def __init__(self):

        # default dictionary
        self.graph = defaultdict(list)

    # adding edge
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):

        # printing visited
        visited.add(v)
        print(v)

        # for neighbour
        # check if visited
        # if not run again
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self):

        # create set of visited
        visited = set()

        # for vertex
        # check if visited
        # if not run again
        for vertex in list(self.graph):
            if vertex not in visited:
                self.dfs_util(vertex, visited)


# Graph
g = Alg()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Depth First Traversal")
g.dfs()

