#genaral data structure
class fringe():
    def __init__(self,*args, **kwargs):
        self._fringe = []
        if len(args) ==1:
            if isinstance(args[0],list):
                for i in range(len(args[0])):
                    self.push(args[0][i])
            else:
                TypeError('Arguments must be a list')
        else:
            raise TypeError('Too much arguments')
    def push(self,value):
        pass
    def pop(self):
        pass
    
    def get_fringe(self):
        return [x for x in self._fringe]
    def display(self):
        print(self._fringe)

class queue(fringe):
    def push(self,value): #enqueue
        self._fringe.append(value)
    def pop(self): #dequeue
        if len(self._fringe)==0:
            raise IndexError('queue is empty')
        return self._fringe.pop(0)

class stack(fringe):
    def push(self,value):
        self._fringe.append(value)
    def pop(self):
        if len(self._fringe)==0:
            raise IndexError('stack is empty')
        return self._fringe.pop(len(self._fringe)-1)

#priority queue
class heap(fringe):
    def push(self,data):
        self._fringe.append(data)
        self.heap_up(len(self._fringe)-1)
    def pop(self):
        if len(self._fringe)==0:
            raise IndexError('heap is empty')
        else:
            self._fringe[0],self._fringe[len(self._fringe)-1] = self._fringe[len(self._fringe)-1],self._fringe[0]
            temp = self._fringe.pop(len(self._fringe)-1)
            self.heap_down(0)
            return temp
    def heap_up(self,index):
        pass
    def heap_down(self,index):
        pass

class min_heap(heap):
    def heap_up(self,index):
        if index <=0:
            return
        else:
            parent_idx = int((index-1)/2)
            if self._fringe[index]<self._fringe[parent_idx]:
                self._fringe[index],self._fringe[parent_idx]= self._fringe[parent_idx],self._fringe[index] #swap
                self.heap_up(parent_idx)
            else:
                return 
    def heap_down(self,index):
        if index >= len(self._fringe)-1:
            return 
        else:
            left_child_index = index*2+1
            right_child_index = index*2+2
            if left_child_index>len(self._fringe)-1 and right_child_index>len(self._fringe)-1: #no child
                return
            elif right_child_index>len(self._fringe)-1: #only left child node
                if self._fringe[index] > self._fringe[left_child_index]:
                    self._fringe[index],self._fringe[left_child_index]= self._fringe[left_child_index],self._fringe[index]
                return
            else:
                if self._fringe[left_child_index] < self._fringe[right_child_index]:
                    if self._fringe[left_child_index] < self._fringe[index]:
                        self._fringe[index],self._fringe[left_child_index]= self._fringe[left_child_index],self._fringe[index]
                        self.heap_down(left_child_index)
                else:
                    if self._fringe[right_child_index]< self._fringe[index]:
                        self._fringe[index],self._fringe[right_child_index]= self._fringe[right_child_index],self._fringe[index]
                        self.heap_down(right_child_index)
            return

class max_heap(heap):
    def heap_up(self,index):
        if index <=0:
            return
        else:
            parent_idx = int((index-1)/2)
            if self._fringe[index]>self._fringe[parent_idx]:
                self._fringe[index],self._fringe[parent_idx]= self._fringe[parent_idx],self._fringe[index] #swap
                self.heap_up(parent_idx)
            else:
                return 
    def heap_down(self,index):
        if index >= len(self._fringe)-1:
            return 
        else:
            left_child_index = index*2+1
            right_child_index = index*2+2
            if left_child_index>len(self._fringe)-1 and right_child_index>len(self._fringe)-1: #no child
                return
            elif right_child_index>len(self._fringe)-1: #only left child node
                if self._fringe[index] < self._fringe[left_child_index]:
                    self._fringe[index],self._fringe[left_child_index]= self._fringe[left_child_index],self._fringe[index]
                return
            else:
                if self._fringe[left_child_index] > self._fringe[right_child_index]:
                    if self._fringe[left_child_index] > self._fringe[index]:
                        self._fringe[index],self._fringe[left_child_index]= self._fringe[left_child_index],self._fringe[index]
                        self.heap_down(left_child_index)
                else:
                    if self._fringe[right_child_index]> self._fringe[index]:
                        self._fringe[index],self._fringe[right_child_index]= self._fringe[right_child_index],self._fringe[index]
                        self.heap_down(right_child_index)
            return


if __name__ == "__main__":
    "Test for any data structures"
    lst = [2,4,6,3,2,6,8,5]
    
    "queue test"
    _queue = queue(lst)
    _queue.display()
    assert _queue.pop()==2,'failed'
    assert _queue.get_fringe()==lst[1:],'failed'

    "stack test"
    _stack = stack(lst)
    assert _stack.pop()==5,'failed'
    _stack.display()

    "min_heap test"
    mh = min_heap(lst)
    mh.display()
    mh.pop()
    mh.display()
    mh.push(1)
    mh.display()