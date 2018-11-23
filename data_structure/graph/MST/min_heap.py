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
        #정점이 arr에 위치한 현재 인덱스
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

        #cur_idx가 루트가 아니고
        #item의 w가 cur_idx 부모의 키보다 작으면
        while cur_idx!=1 and item.w < self.arr[self.__get_parent_idx(cur_idx)].w:
            #리프 노드로 추가된 새로운 원소의 weight가 부모의 원소의 weight보다 
            #더 작으면 부모 원소를 한 칸 내린다 
            self.arr[cur_idx]=self.arr[self.__get_parent_idx(cur_idx)]
            #아래로 내려오는 부모 원소의 위치 인덱스 업데이트
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

        #삭제된 후 반환될 원소
        rem_elem=self.arr[1]

        #맨 마지막에 위치한 원소
        temp=self.arr[self.heapsize]

        #루트에서 시작
        cur_idx=1
        smaller_child_idx=self.__get_smaller_child_idx(cur_idx)

        while smaller_child_idx and temp.w > self.arr[smaller_child_idx].w:
            #마지막 원소보다 weight가 큰 정점은 루트쪽으로 한칸 올라간다
            self.arr[cur_idx]=self.arr[smaller_child_idx]
            
            #이와 함께 루트쪽으로 올라간 정점의 현재 인덱스도 업데이트한다
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

    #프림 알고리즘을 위해 추가된 함수
    def decrease_weight(self, new_elem):
        #업데이트될 정점의 현재 인덱스
        cur=self.pos[new_elem.v]

        #cur가 루트가 아니고 업데이트 될 원소의 weight가
        #부모 원소의 weight보다 작다면 부모 원소를 아래로 내리고
        #cur가 루트 쪽으로 올라간다
        while cur!= 1 and new_elem.w < self.arr[self.__get_parent_idx(cur)].w:
            #업데이트 될 원소의 weight가 부모 원소의 weight보다 작다면
            #부모 원소를 한 칸 아래로 내린다 
            self.arr[cur]=self.arr[self.__get_parent_idx(cur)]

            #내려온 원소의 위치 인덱스 업데이트
            self.pos[self.arr[cur].v]=cur    

            cur=self.__get_parent_idx(cur)

        self.arr[cur]=new_elem
        self.pos[new_elem.v]=cur

def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].w), end="  ")
    print()

