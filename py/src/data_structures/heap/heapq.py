from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

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
    def push(self, item):
        pass

    # Pop and return the smallest item from the heap, maintaining the heap invariant.
    # If the heap is empty, IndexError is raised. To access the smallest item without
    # popping it, use heap[0].
    def pushpop(self, item):
        pass

    # Transform list x into a heap, in-place, in linear time.
    def heapify(self, x):
        pass

    '''
    Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the 
    heap is empty, IndexError is raised.

    This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when 
    using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

    The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. 
    Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.
    '''
    def replace(self, item):
        pass