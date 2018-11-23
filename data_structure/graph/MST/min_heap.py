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

        #cur_idx가 루트가 아니고
        #item의 w가 cur_idx 부모의 키보다 작으면
        while cur_idx!=1 and item.w < self.arr[self.__get_parent_idx(cur_idx)].w:
            self.arr[cur_idx]=self.arr[self.__get_parent_idx(cur_idx)]
            cur_idx=self.__get_parent_idx(cur_idx)
        self.arr[cur_idx]=item

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

        #삭제된 후 반환될 원소
        rem_elem=self.arr[1]

        #맨 마지막에 위치한 원소
        temp=self.arr[self.heapsize]

        #루트에서 시작
        cur_idx=1
        smaller_child_idx=self.__get_smaller_child_idx(cur_idx)

        while smaller_child_idx and temp.w > self.arr[smaller_child_idx].w:
            self.arr[cur_idx]=self.arr[smaller_child_idx]
            cur_idx=smaller_child_idx
            smaller_child_idx=self.__get_smaller_child_idx(cur_idx)
        
        self.arr[cur_idx]=temp
        self.heapsize-=1

        return rem_elem

    def top(self):
        if self.is_empty():
            return None

        return self.arr[1]

    #프림 알고리즘을 위해 추가된 함수
    def decrease_weight(self, new_elem):
        for i in range(1, self.heapsize+1):
            if self.arr[i].v==new_elem.v:
                cur=i
                break

        while cur!= 1 and new_elem.w < self.arr[self.__get_parent_idx(cur)].w:
            self.arr[cur]=self.arr[self.__get_parent_idx(cur)]
            cur=self.__get_parent_idx(cur)
        self.arr[cur]=new_elem

def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].w), end="  ")
    print()

