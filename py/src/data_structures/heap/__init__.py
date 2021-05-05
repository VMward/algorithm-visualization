"""
I'm not arrogant enough to think this will compete with the official heapq library,
but this is an simplified exercise to demonstrate how to implement heaps in python3.
https://docs.python.org/3/library/heapq.html

The functions will still mirror the official heapq documentation.

"""

from .. import queue

class Heapq:
    # base structure is a queue
    def __init__(self):
        self.__struct = queue

    # Push the value item onto the heap, maintaining the heap invariant.
    def heappush(self, item):
        pass

    # Pop and return the smallest item from the heap, maintaining the heap invariant.
    # If the heap is empty, IndexError is raised. To access the smallest item without
    # popping it, use heap[0].
    def heappushpop(self, item):
        pass

    # Transform list x into a heap, in-place, in linear time.
    def heapify(self, x):
        pass