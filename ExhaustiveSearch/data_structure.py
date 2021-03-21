from abc import ABC
class fringe(ABC):
    def push(self,value):
        pass
    def pop(self):
        pass

class general_queue(fringe):
    def __init__(self,*args, **kwargs):
        self._fringe = []
        if len(args) ==1:
            if isinstance(args[0],queue):
                self._fringe = args[0].get_fringe()
            elif isinstance(args[0],list):
                self._fringe = [x for x in args[0]]
            else:
                self.push(args[0])
        else:
            raise TypeError('Too much arguments')
    def get_fringe(self):
        return [x for x in self._fringe]
    def display(self):
        print(self._fringe)

class queue(general_queue):
    def push(self,value):
        self._fringe.append(value)
    def pop(self):
        if len(self._fringe)==0:
            raise IndexError('queue is empty')
        return self._fringe.pop(0)

class stack(general_queue):
    def push(self,value):
        self._fringe.append(value)
    def pop(self):
        if len(self._fringe)==0:
            raise IndexError('stack is empty')
        return self._fringe.pop(len(self._fringe)-1)


