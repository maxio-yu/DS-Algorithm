#!/usr/bin/python

class Graph(object):

    def __init__(self, graph = {}):
        self.graph = graph

    def vertices(self):
        return self.graph.keys()

    def edges(self):
        edges = []
        for V in self.graph:
            for neighbour in self.graph[V]:
                edges.append((V,neighbour))
        return edges

    def add_edge(self, edge):
        start,end = edge
        if end not in self.graph[start]:
            self.graph[start].append(end)

    def remove_edge(self, edge):
        start,end = edge
        if self.graph.has_key(start):
            if end in self.graph[start]:
                self.graph[start].remove(end)
                return
        print "No edge", edge

    def bfs(self, start):
        # TODO: use deque from collection
        q = []
        visited = []
        if self.graph.has_key(start):
            q.append(start)
            visited.append(start)
        while(q):
            node = q.pop(0)
            for i in self.graph[node]:
                if i not in visited:
                    q.append(i)
                    visited.append(i)
            print node,
        print 

    def dfs(self, start):
        visited = []
        if self.graph.has_key(start):
            self._dfs(start, visited)
        print 

    def _dfs(self, start, visited):
        visited.append(start)
        print start,
        for i in self.graph[start]:
            if i not in visited:
                self._dfs(i, visited)

    def dfs_stack(self, start):
        visited = []
        q = []
        if self.graph.has_key(start):
            q.append(start)
            visited.append(start)
            while (q):
                node = q.pop()
                print node,
                for i in reversed(self.graph[node]):
                    if i not in visited:
                        q.append(i)
                        visited.append(i)
            print








g = {'a': ['b','c'],
         'b': ['d','e'],
         'c': ['f','g'],
         'd': [],
         'e': [],
         'f': [],
         'g': [],
         }

graph = Graph(g)
print graph.edges()

graph.add_edge(('b','d'))
print graph.edges()

graph.remove_edge(('a','d'))
print graph.edges()

graph.remove_edge(('a','f'))
print graph.edges()

graph.bfs('a')
graph.dfs_stack('a')
graph.dfs('a')





