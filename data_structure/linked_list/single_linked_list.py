class Node:
    def __init__(self, data=None):
        self.__data=data
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
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

class LinkedList:
    def __init__(self):
        self.head=None
        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False
    
    def size(self):
        return self.d_size

    def add(self, data):
        new_node=Node(data)
        if self.empty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.d_size+=1

    def __insert_after(self, data, bef_node):
        new_node=Node(data)
        new_node.next=bef_node.next
        bef_node.next=new_node
        self.d_size+=1

    def insert_after(self, data, bef_data):
        bef_node=self.search(bef_data)
        self.__insert_after(data, bef_node)

    def __search(self, target):
        """
        search(target)->(before node, current node)
        """
        if self.empty():
            return None, None

        bef=self.head
        cur=self.head
        while cur:
            if cur.data==target:
                return bef, cur
            bef=cur
            cur=cur.next
        return None, None

    def search(self, target):
        return self.__search(target)[1]

    def delete(self):
        self.head=self.head.next
        self.d_size-=1

    def __delete_node(self, bef_node):
        del_node=bef_node.next
        bef_node.next=bef_node.next.next
        self.d_size-=1
        return del_node

    def delete_node(self, target):
        bef, cur = self.__search(target)
        if not cur:
            return None
        return self.__delete_node(bef)

    def traverse(self):
        cur=self.head
        while cur:
            yield cur
            cur=cur.next

def show_list(slist):
    g=slist.traverse()
    for node in g:
        print(node.data, end= '  ')

if __name__=="__main__":
    print('*'*100)
    slist=LinkedList()

    print('데이터 삽입-add')
    slist.add(3)
    slist.add(1)
    slist.add(5)
    slist.add(2)
    slist.add(7)
    slist.add(8)
    slist.add(3)
    print('데이터 개수 : {}'.format(slist.size()))
    show_list(slist)
    print('\n')

    print('데이터 삽입-insert_after')
    slist.insert_after(10, 5)
    print('데이터 개수 : {}'.format(slist.size()))
    show_list(slist)
    print('\n')

    print('데이터 탐색')
    target=5
    res=slist.search(target)
    if res:
        print('데이터 {} 검색 성공'.format(res.data))
    else:
        print('데이터 {} 탐색 실패'.format(target))
    res=None
    print()

    print('데이터 삭제-delete')
    slist.delete()
    slist.delete()
    slist.delete()
    print('데이터 개수 : {}'.format(slist.size()))
    show_list(slist)
    print()

    print('데이터 삭제-delete_node')
    slist.delete_node(5)
    slist.delete_node(1)
    print('데이터 개수 : {}'.format(slist.size()))
    show_list(slist)
    print()
    
    print('*'*100)
