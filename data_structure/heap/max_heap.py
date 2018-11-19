class Element:
    def __init__(self, key):
        self.key=key

class MaxHeap:
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
        #item의 key가 cur_idx 부모의 키보다 크면
        while cur_idx!=1 and item.key > self.arr[self.__get_parent_idx(cur_idx)].key:
            self.arr[cur_idx]=self.arr[self.__get_parent_idx(cur_idx)]
            cur_idx=self.__get_parent_idx(cur_idx)
        self.arr[cur_idx]=item


    def __get_bigger_child_idx(self, idx):
        if self.heapsize < self.__get_left_child_idx(idx):
            return None
        elif self.heapsize==self.__get_left_child_idx(idx):
            return self.__get_left_child_idx(idx)
        else:
            left_child=self.__get_left_child_idx(idx)
            right_child=self.__get_right_child_idx(idx)
            if self.arr[left_child].key > self.arr[right_child].key:
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
        bigger_child_idx=self.__get_bigger_child_idx(cur_idx)

        while bigger_child_idx and temp.key < self.arr[bigger_child_idx].key:
            self.arr[cur_idx]=self.arr[bigger_child_idx]
            cur_idx=bigger_child_idx
            bigger_child_idx=self.__get_bigger_child_idx(cur_idx)
        
        self.arr[cur_idx]=temp
        self.heapsize-=1

        return rem_elem

    def top(self):
        if self.is_empty():
            return None

        return self.arr[1]

def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].key), end="  ")
    print()

if __name__=="__main__":
    h=MaxHeap()

    e=Element(2)
    h.push(e)

    e=Element(14)
    h.push(e)

    e=Element(9)
    h.push(e)

    print_heap(h)

    # e=Element(11)
    # h.push(e)

    # e=Element(6)
    # h.push(e)

    # e=Element(8)
    # h.push(e)

    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)

    # rem=h.pop()
    # print("poped item is {}".format(rem.key))
    # print_heap(h)
    