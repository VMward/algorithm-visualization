class Queue:
    # base structure is list
    def __init__(self):
        self.__struct = []

    def is_empty(self) -> bool:
        return len(self.__struct) > 0

    def front(self):
        return (None, self.__struct[0])[self.is_empty()]

    def rear(self):
        return (None, self.__struct[-1])[self.is_empty()]

    def enqueue(self, ele):
        self.__struct.append(ele)

    def dequeue(self):
        return (None, self.__struct.pop(0))[self.is_empty()]

    def clear(self):
        self.__struct = []



