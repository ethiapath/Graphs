"""
Simple graph implementation
"""
from collections import deque
from time import time
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return (len(self.queue))

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id, cb):
        output = []
        # create an empty queue
        q = Queue()
        # create an empty list (set) of visted vertices
        visted = set()
        # put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first node from the queue
            v = q.dequeue()
            # if that node has not been visted
            if v not in visted:
                # mark it as visted 
                visted.add(v)
                output.append(v)
                cb(v)
                print(v)
                # then put all of its children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        print(output)

    def dft(self, starting_vertex_id):
        # create an empty stack
        s = Stack()
        # create an empty list (set) of visted vertices
        visted = set()
        # put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first node from the stack
            v = s.pop()
            # if that node has not been visted
            if v not in visted:
            # mark it as visted 
                visted.add(v)
                print(v)
                # then put all of its children into the stack
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft_recursive(self, starting_vertex_id):
        pass

    def bf_traverse(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print(f'VISITED: {queue[0]}')
            visited.add(queue.pop(0))

    def bfs(self, starting_vertex_id, target=None):

        q = Queue()
        # create an empty list (set) of visted vertices
        # visted = set()

        # list that will record the path taken
        paths = []
        subpath = []
        prev = None
        # put the starting vertex in our Queue
        q.enqueue([starting_vertex_id])
        counter = 0
        depth = 0
        while q.size() > 0:
            # dequeue the first subpath from the queue
            v = q.dequeue()
  
            depth += 1
            # mark it as visted 
            # visted.add(v)
            print(v)
            # then put all of its neighbors into the queue
            for neighbor in self.vertices[v[-1]]:
                subpath = []
                subpath = v.copy()
                if neighbor not in subpath:
                    subpath.append(neighbor)
                    if subpath[-1] == target:
                        print(f'shortest path: {subpath}')
                        return subpath
                    # path.append(v)
                    q.enqueue(subpath)
            # prev = v
            # counter += 1
            
        print(paths)
        return False
# queue = [3, 6, 7]
# visted = {1, 2, 4}

# 1
# 1, 2, 4
