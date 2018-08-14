class Node:
    def __init__(self, data=None):
        self.__data=data
        self.__before=None
        self.__next=None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data=data
    
    @property
    def before(self):
        return self.__before

    @before.setter
    def before(self, b):
        self.__before=b

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.before=self.head
        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node=Node(data)
        
        new_node.next=self.head.next
        new_node.before=self.head

        self.head.next.before=new_node
        self.head.next=new_node

        self.d_size+=1

    def add_last(self, data):
        new_node=Node(data)

        new_node.before=self.tail.before
        new_node.next=self.tail

        self.tail.before.next=new_node
        self.tail.before=new_node

        self.d_size+=1

    def insert_after(self, data, node):
        new_node=Node(data)

        new_node.next=node.next
        new_node.before=node

        node.next.before=new_node
        node.next=new_node

        self.d_size+=1

    def insert_before(self, data, node):
        new_node=Node(data)

        new_node.before=node.before
        new_node.next=node

        node.before.next=new_node
        node.before=new_node

        self.d_size+=1

    def search_forward(self, data):
        cur=self.head.next
        while cur is not self.tail:
            if cur.data==data:
                return cur
            cur=cur.next
        return None

    def search_backward(self, data):
        cur=self.tail.before
        while cur is not self.head:
            if cur.data==data:
                return cur
            cur=cur.before
        return None
        
    def delete_first(self):
        self.head.next=self.head.next.next
        self.head.next.before=self.head

        self.d_size-=1

    def delete_last(self):
        self.tail.before=self.tail.before.before
        self.tail.before.next=self.tail

        self.d_size-=1

    def delete_node(self, node):
        del_node=node
        node.before.next=node.next
        node.next.before=node.before

        self.d_size-=1
        return del_node

    def traverse(self, start=True):
        """
        start=True --> from head
        start=False --> from tail
        """
        if start:
            cur=self.head.next
            while cur is not self.tail:
                yield cur
                cur=cur.next
        else:
            cur=self.tail.before
            while cur is not self.head:
                yield cur
                cur=cur.before
        

def show_list(dlist, start=True):
    print('data size : {}'.format(dlist.size()))
    g=dlist.traverse(start)
    for node in g:
        print(node.data, end='  ')
    print()

if __name__=="__main__":
    dlist=DoubleLinkedList()
    print('*'*100)
    #print('데이터 삽입 -add_first')
    # dlist.add_first(1)
    # dlist.add_first(2)
    # dlist.add_first(3)
    # dlist.add_first(5)

    print('데이터 삽입 -add_last')
    dlist.add_last(1)
    dlist.add_last(2)
    dlist.add_last(3)
    dlist.add_last(5)
    show_list(dlist, start=True)

    print('데이터 삽입 - insert_after')
    dlist.insert_after(4, dlist.search_forward(3))
    show_list(dlist, start=True)

    # print('데이터 삽입 - insert_before')
    # dlist.insert_before(4, dlist.search_forward(5))
    # show_list(dlist, start=True)

    print('데이터 탐색')
    target=3
    #res=dlist.search_forward(target)
    res=dlist.search_backward(target)
    if res:
        print('데이터 {} 탐색 성공'.format(res.data))
    else:
        print('데이터 {} 탐색 실패'.format(target))
    res=None

    # print('데이터 삭제-delete_first')
    # dlist.delete_first()
    # dlist.delete_first()

    # print('데이터 삭제-delete_last')
    # dlist.delete_last()
    # dlist.delete_last()

    print('데이터 삭제-delete_node')
    dlist.delete_node(dlist.search_backward(5))

    show_list(dlist, start=True)

    print('*'*100)