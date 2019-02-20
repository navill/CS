class TreeNode:
    def __init__(self, key):
        self.__key=key
        self.__left=None
        self.__right=None

    def __del__(self):
        print('key {} is deleted'.format(self.__key))

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key=key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left=left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right=right

class BST:
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def insert(self, key):
        new_node=TreeNode(key)

        cur=self.root
        if not cur:
            self.root=new_node
            return

        while True:
            parent=cur
            if key < cur.key:
                cur=cur.left
                if not cur:
                    parent.left=new_node
                    return
            else:
                cur=cur.right
                if not cur:
                    parent.right=new_node
                    return 

    def search(self, target):
        cur=self.root
        while cur:
            if cur.key==target:
                return cur
            elif cur.key > target:
                cur=cur.left
            elif cur.key < target:
                cur=cur.right
        return cur

    def __remove_recursion(self, cur, target):
        if not cur:
            return None, None
        elif target < cur.key:
            cur.left, rem_node=self.__remove_recursion(cur.left, target)
        elif target > cur.key:
            cur.right, rem_node=self.__remove_recursion(cur.right, target)
        else:
            if not cur.left and not cur.right:
                rem_node=cur
                cur=None
            elif not cur.right:
                rem_node=cur
                cur=cur.left
            elif not cur.left:
                rem_node=cur
                cur=cur.right
            else:
                replace=cur.left
                while replace.right:
                    replace=replace.right
                cur.key, replace.key=replace.key, cur.key
                cur.left, rem_node=self.__remove_recursion(cur.left, replace.key)
        return cur, rem_node

    def remove(self, target):
        self.root, removed_node=self.__remove_recursion(self.root, target)
        if removed_node:
            removed_node.left=removed_node.right=None
        return removed_node

if __name__=="__main__":
    print('*'*100)
    bst=BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f=lambda x: print(x.key, end='  ')

    bst.preorder_traverse(bst.get_root(), f)
    print()

    print('searched key : {}'.format(bst.search(8).key))

    #bst.remove(9)
    #bst.remove(8)
    #bst.remove(6)

    print(bst.remove(15))

    bst.preorder_traverse(bst.get_root(), f)
    print()
    print('*'*100)