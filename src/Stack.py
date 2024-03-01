class Stack:
    def __init__(self):
        self.__item = []
        self.__top = -1

    def pop(self):
        self.__top -= 1
        if len(self.__item) >= 1:
            element = self.__item.pop()
            return element
        else:
            raise IndexError('List is Empty')
            
    def push(self, item):
        self.__top += 1
        self.__item.append(item)

    def is_empty(self):
        if not self.__item:
            return True
        else:
            return False

    def head(self):
        if self.__top != -1:
            return self.__item[self.__top]
        else:
            return None