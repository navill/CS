from double_linked_list import DoubleLinkedList

class PseudoList(DoubleLinkedList):
    def __init__(self, *args):
        super().__init__()
        for elem in args:
            self.add_last(elem)

    def __len__(self):
        return self.size()

    def append(self, data):
        self.add_last(data)

    def __find_position(self, pos):
        if pos >=self.size():
            raise IndexError('list index out of range')
        cur = self.head.next
        for _ in range(pos):
            cur = cur.next
        return cur

    def insert(self, pos, data):
        cur = self.__find_position(pos)
        self.insert_before(data, cur)

    def count(self, data):
        cnt = 0
        cur = self.head.next
        while cur:
            if cur.data == data:
                cnt+=1
            cur=cur.next
        return cnt

    def index(self, data, start=0):
        cur = self.__find_position(start)
        index = start
        while cur:
            if cur.data == data:
                return index
            cur = cur.next; index+=1
        raise IndexError('{} is not in list'.format(data))

    def __getitem__(self, index):
        if index >= self.size():
            raise IndexError('list index out of range')
        cur = self.__find_position(index)
        return cur.data

    def __setitem__(self, index, data):
        if index >= self.size():
            raise IndexError('list index out of range')
        cur = self.__find_position(index)
        cur.data = data

    def pop(self, pos=None):
        if pos is not None:
            cur = self.__find_position(pos)    
        else:
            cur = self.tail.before
        
        self.delete_node(cur)
        return cur.data

    def remove(self, data):
        self.delete_node(self.search_forward(data))

    def __str__(self):
        string = '['
        cur = self.head.next
        while cur is not self.tail:
            string+=str(cur.data)
            if cur.next is not self.tail:
                string+=', '
            cur= cur.next

        string+=']'
        return string

if __name__=="__main__":
    print("*"*50)
    initial = [1, 2, 3, 4]
    li = PseudoList(*initial)
    #li=initial

    print(li)
    print()

    print('append')
    li.append(2)
    li.append(1)
    li.append(2)
    li.append(7)
    li.append(2)
    print(li)
    print()

    print('count')
    target = 2
    print('count of {} is {}'.format(target, li.count(target)))
    print()

    print('remove')
    target = 2
    li.remove(target)
    print(li)
    print()

    print('insert')
    li2 = PseudoList(*[1, 2, 5, 6])
    print(li2)
    li2.insert(2, 3)
    print(li2)
    li2.insert(3, 4)
    li2.insert(4, 10)
    print(li2)
    print()

    print('index')
    target = 10
    print('index of {} is {}'.format(target, li2.index(target)))
    print()

    print('indexing')
    index = 3
    print('li2[{}]={}'.format(index, li2[index]))
    li2[1]='a'
    print(li2)
    li2[2]='b'
    print(li2)
    li2[3]='c'
    print(li2)
    print()

    print('pop')
    print(li2)
    print("poped item : {}".format(li2.pop(0).data))
    print(li2)
    print("poped item : {}".format(li2.pop(0).data))
    print(li2)
    print("poped item : {}".format(li2.pop(0).data))
    print(li2)
    print("poped item : {}".format(li2.pop(0).data))
    print(li2)
    print()

    print("*"*50)