class Element:
    def __init__(self, v, w, _from):
        self.w=w
        self.v=v
        self._from=_from

class MinHeap:
    MAX_ELEMENTS=200
    def __init__(self):
        self.arr=[None for i in range(self.MAX_ELEMENTS)]
        self.heapsize=0
        self.pos=[None for i in range(self.MAX_ELEMENTS)]

    def is_empty(self):
        if self.heapsize==0:
            return True
        return False

    def is_full(self):
        if self.heapsize>=self.MAX_ELEMENTS:
            return True
        return False

    def __get_parent_idx(self, idx):
        return idx // 2

    def __get_left_child_idx(self, idx):
        return idx * 2

    def __get_right_child_idx(self, idx):
        return idx * 2 + 1

    def push(self, item):
        if self.is_full():
            raise IndexError("the heap is full!!")

        self.heapsize+=1
        cur_idx=self.heapsize

        while cur_idx!=1 and item.w < self.arr[self.__get_parent_idx(cur_idx)].w:
            self.arr[cur_idx]=self.arr[self.__get_parent_idx(cur_idx)]
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=self.__get_parent_idx(cur_idx)

        self.arr[cur_idx]=item
        self.pos[item.v]=cur_idx

    def __get_smaller_child_idx(self, idx):
        if self.heapsize < self.__get_left_child_idx(idx):
            return None
        elif self.heapsize==self.__get_left_child_idx(idx):
            return self.__get_left_child_idx(idx)
        else:
            left_child=self.__get_left_child_idx(idx)
            right_child=self.__get_right_child_idx(idx)
            if self.arr[left_child].w < self.arr[right_child].w:
                return left_child
            else:
                return right_child

    def pop(self):
        if self.is_empty():
            return None

        rem_elem=self.arr[1]

        temp=self.arr[self.heapsize]

        cur_idx=1
        smaller_child_idx=self.__get_smaller_child_idx(cur_idx)

        while smaller_child_idx and temp.w > self.arr[smaller_child_idx].w:
            self.arr[cur_idx]=self.arr[smaller_child_idx]
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=smaller_child_idx
            smaller_child_idx=self.__get_smaller_child_idx(cur_idx)
        
        self.arr[cur_idx]=temp
        self.pos[temp.v]=cur_idx

        self.heapsize-=1

        return rem_elem

    def top(self):
        if self.is_empty():
            return None

        return self.arr[1]

    def decrease_weight(self, new_elem):
        cur=self.pos[new_elem.v]

        while cur!= 1 and new_elem.w < self.arr[self.__get_parent_idx(cur)].w: 
            self.arr[cur]=self.arr[self.__get_parent_idx(cur)]
            self.pos[self.arr[cur].v]=cur    

            cur=self.__get_parent_idx(cur)

        self.arr[cur]=new_elem
        self.pos[new_elem.v]=cur

def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].w), end="  ")
    print()

