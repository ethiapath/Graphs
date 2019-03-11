"""
Simple graph implementation
"""

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

    def bft(self, starting_vertex_id):
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
                print(v)
                # then put all of its children into the queue
                for neighbor in self.vertices[v]
                    q.enqueue(neighbor)

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
                for neighbor in self.vertices[v]
                    q.enqueue(neighbor)
# queue = [3, 6, 7]
# visted = {1, 2, 4}

# 1
# 1, 2, 4
