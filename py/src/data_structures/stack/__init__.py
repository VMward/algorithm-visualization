class Stack:
    # base structure is list
    def __init__(self):
        self.__struct = []

    def is_empty(self) -> bool:
        return len(self.__struct) > 0

    def push(self, ele):
        self.__struct.append(ele)

    def clear(self):
        self.__struct = []

    def peek(self):
        return (None, self.__struct[-1])[self.is_empty()]

    def pop(self):
        return (None, self.__struct.pop())[self.is_empty()]