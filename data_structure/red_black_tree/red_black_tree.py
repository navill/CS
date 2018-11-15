class RBNode:
    def __init__(self, key):
        #트리 내에서 유일한 키
        self.key=key
        #노드의 색 : RED or BLACK
        #트리에 insert 연산을 할 때 먼저 새 노드의 색은 RED로 한다.
        self.color="RED"
        
        self.left_child=None
        self.right_child=None

        #부모
        self.parent=None

class RedBlackTree:
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left_child, func)
        self.preorder_traverse(cur.right_child, func)

    def __left_rotate(self, n):
        #n's right child
        rc=n.right_child
        #rc's left child
        rcl=rc.left_child

        #rcl을 n의 오른쪽 자식으로
        #rcl이 None일 수 있으므로
        if rcl:
            rcl.parent=n
        n.right_child=rcl

        #n.parent를 rc.parent로
        #n이 루트라면, 트리 루트도 업데이트
        if n.parent==None:
            self.root=rc
        elif n.parent.left_child==n:
            n.parent.left_child=rc
        else:
            n.parent.right_child=rc
        rc.parent=n.parent

        #n을 rc의 왼쪽 자식으로
        rc.left_child=n
        n.parent=rc

    def __right_rotate(self, n):
        #n's left child
        lc=n.left_child
        #lc's right child
        lcr=lc.right_child

        #lcr을 n의 왼쪽 자식으로
        #lcr이 None일 수 있으므로
        if lcr:
            lcr.parent=n
        n.left_child=lcr

        #n.parent를 lc.parent로
        #n이 루트라면 트리의 루트도 업데이트
        if n.parent==None:
            self.root=lc
        elif n.parent.left_child==n:
            n.parent.left_child=lc
        else:
            n.parent.right_child=lc
        lc.parent=n.parent

        #n을 lc의 오른쪽 자식으로
        lc.right_child=n
        n.parent=lc

    def __insert_fix(self, n):
        #pn: n's parent
        #gn: n's grand parent
        #un: pn's sibling 
        pn=gn=un=None

        #en: external node
        en=RBNode(None)
        en.color="BLACK"

        pn=n.parent
        #n이 루트가 아니고 
        #n.parent가 RED --> 연속된 RED
        while pn != None and pn.color=="RED":
            #pn이 RED이면 반드시 gn이 존재: 루트는 BLACK이므로 pn은 루트가 될 수 없다
            gn=pn.parent
            #1. pn이 gn의 왼쪽 자식일 때
            if gn.left_child==pn:
                #조부모의 오른쪽 자식이 외부 노드일 때
                #부모 형제를 미리 만들어 둔 en으로 대체
                if gn.right_child==None:
                    un=en
                else:
                    un=gn.right_child
                
                #XYr : 부모 형제가 RED일 때
                if un.color=="RED":
                    #부모, 부모 형제와 조부모의 색을 변경
                    gn.color="RED"
                    pn.color=un.color="BLACK"

                    #gn을 새로운 n으로 만든 후 연속된 레드가 또 일어나는지 확인
                    n=gn
                    pn=n.parent
                    
                #XYb : 부모 형제가 BLACK일 때
                else:
                    #LRb일 때 
                    if pn.right_child==n:
                        #LEFT-ROTATE(pn)
                        self.__left_rotate(pn)
                        n, pn = pn, n
                    #LLb일 때
                    #부모와 조부모의 색을 바꾸고
                    pn.color, gn.color=gn.color, pn.color

                    #RIGHT-ROATE(gn)
                    self.__right_rotate(gn)
            #2. pn이 gn의 오른쪽 자식일 때
            else:
                #조부모의 왼쪽 자식이 외부 노드일 때
                #부모 형제를 en으로 대체
                if gn.left_child==None:
                    un=en
                else:
                    un=gn.left_child
                if un.color=="RED":
                    gn.color="RED"
                    pn.color=un.color="BLACK"

                    n=gn
                    pn=n.parent
                else:
                    if pn.left_child==n:
                        self.__right_rotate(pn)
                        n, pn = pn, n
                    pn.color, gn.color=gn.color, pn.color
                    self.__left_rotate(gn)

        #연속된 레드가 루트까지 올라갔을 경우에는 
        #루트를 BLACK으로 만들어주면 된다
        self.root.color="BLACK"

    def insert(self, key):
        new_node=RBNode(key)

        cur=self.root
        if not cur:
            self.root=new_node
            #루트 노드는 BLACK
            new_node.color="BLACK"
            return

        while True:
            parent=cur
            if key < cur.key:
                cur=cur.left_child
                if not cur:
                    parent.left_child=new_node
                    #노드의 parent 설정
                    new_node.parent=parent
                    break
            else:
                cur=cur.right_child
                if not cur:
                    parent.right_child=new_node
                    #노드의 parent 설정
                    new_node.parent=parent
                    break
        #노드 삽입 후 처리
        self.__insert_fix(new_node)

    def search(self, target):
        cur=self.root
        while cur:
            if cur.key==target:
                return cur
            elif cur.key > target:
                cur=cur.left_child
            elif cur.key < target:
                cur=cur.right_child
        return cur

    def __remove_recursion(self, cur, target):
        if not cur:
            return None, None
        elif target < cur.key:
            cur.left_child, rem_node=self.__remove_recursion(cur.left_child, target)
            #왼쪽 자식 노드의 부모 설정
            if cur.left_child:
                cur.left_child.parent=cur
        elif target > cur.key:
            cur.right_child, rem_node=self.__remove_recursion(cur.right_child, target)
            #오른쪽 자식 노드의 부모 설정
            if cur.right_child:
                cur.right_child.parent=cur
        else:
            if not cur.left_child and not cur.right_child:
                rem_node=cur
                cur=None
            elif not cur.right_child:
                rem_node=cur
                cur=cur.left_child
            elif not cur.left_child:
                rem_node=cur
                cur=cur.right_child
            else:
                replace=cur.left_child
                while replace.right_child:
                    replace=replace.right_child
                cur.key, replace.key=replace.key, cur.key
                cur.left_child, rem_node=self.__remove_recursion(cur.left_child, replace.key)
                #왼쪽 자식 노드의 부모 설정
                if cur.left_child:
                    cur.left_child.parent=cur
        return cur, rem_node

    def __remove_fix(self, c):
        #child.color가 RED일 때
        if c.color=="RED":
            c.color="BLACK"
            return

        #노드 c가 루트가 아니고 : 루트면 extra BLACK 제거 후 종료
        #노드 c가 BLACK이면 : RED이면 BLACK으로 만들고 종료
        while c.parent!=None and c.color=="BLACK":
            #노드 c가 왼쪽 자식 노드일 때
            if c.parent.left_child==c:
                #s: sibling
                s=c.parent.right_child

                print("before balancing")
                self.preorder_traverse(self.root, self.print_node)

                #case 1: s.color = RED
                #case 2로 만든다
                if s.color=="RED":
                    #c.parent와 s의 컬러를 바꾼다
                    c.parent.color, s.color=s.color, c.parent.color
                    #LEFT-ROTATE(c.parent)
                    self.__left_rotate(c.parent)

                    print("after CASE 1")
                    self.preorder_traverse(self.root, self.print_node)
                    print("\n")
                #case 2: s.color = BLACK
                else:
                    #case 2-1: s.left and s.right --> BLACK
                    if s.left_child.color=="BLACK" and s.right_child.color=="BLACK":
                        #tack black from c, s
                        s.color="RED"
                        #give black to p
                        c=c.parent

                        print("after CASE 2-1")
                        self.preorder_traverse(self.root, self.print_node)
                        print("\n")

                    #case 2-2: s.left --> RED
                    elif s.right_child.color=="BLACK":
                        s.color, s.left_child.color=s.left_child.color, s.color
                        self.__right_rotate(s)

                        print("after CASE 2-2")
                        self.preorder_traverse(self.root, self.print_node)
                        print("\n")
                    #case 2-3: s.right --> RED
                    else:
                        s.color=c.parent.color
                        c.parent.color=s.right_child.color="BLACK"
                        self.__left_rotate(c.parent)
                        #while문을 빠져나간다
                        c=self.root
                        print("after CASE 2-3")
                        self.preorder_traverse(self.root, self.print_node)
                        print("\n")
            #노드 c가 오른쪽 자식일 때
            else:
                s=c.parent.left_child
                if s.color=="RED":
                    c.parent.color, s.color=s.color, c.parent.color
                    self.__right_rotate(c.parent)
                else:
                    if s.left_child.color=="BLACK" and s.right_child.color=="BLACK":
                        s.color="RED"
                        c=c.parent
                    elif s.left_child.color=="BLACK":
                        s.color, s.right_child.color=s.right_child, s.color
                        self.__left_rotate(s)
                    else:
                        s.color=c.parent.color
                        c.parent.color=s.left_child.color="BLACK"
                        self.__right_rotate(c.parent)

                        c=self.root        
        c.color="BLACK"
        

    def remove(self, target):
        self.root, removed_node=self.__remove_recursion(self.root, target)

        #삭제된 노드가 블랙 노드인 경우
        #삭제된 노드의 자식 노드를 
        #remove_fix의 인자로 전달
        if removed_node and removed_node.color=="BLACK":
            if removed_node.left_child:
                rem_child=removed_node.left_child
            elif removed_node.right_child:
                rem_child=removed_node.right_child
            else:
                #삭제된 노드가 리프 노드라면
                #삭제된 노드의 자식 노드는 외부 노드
                rem_child=RBNode(None)
                rem_child.parent=removed_node.parent
                rem_child.color="BLACK"
            self.__remove_fix(rem_child)

        if removed_node:
            removed_node.left=removed_node.right=removed_node.parent=None
        return removed_node

    def print_node(self, rbn):
        if rbn:
            print("node : {}, ".format(rbn.key), end="")
            if rbn.color=="RED":
                print("color : RED, ", end="")
            else:
                print("color : BLACK, ", end="")
            if rbn.left_child:
                print("left : {}, ".format(rbn.left_child.key), end="")
            if rbn.right_child:
                print("right : {}, ".format(rbn.right_child.key), end="")
            if rbn.parent:
                print("parent : {}".format(rbn.parent.key), end="")
            print()

def color_changer(cur):
    if cur.key==5:
        cur.color="RED"
    else:
        cur.color="BLACK"

if __name__=="__main__":
    print('*'*100)
    rbt=RedBlackTree()
    #insert
    rbt.insert(20)
    rbt.insert(10)
    rbt.insert(22)
    #LLr
    rbt.insert(7)
    rbt.insert(15)
    #LRr
    rbt.insert(8)
    rbt.insert(13)
    #LRb
    rbt.insert(14)
    rbt.preorder_traverse(rbt.get_root(), rbt.print_node)

    #delete - case 1, case 2-1
    # rbt.insert(3)
    # rbt.insert(2)
    # rbt.insert(1)
    # rbt.insert(7)
    # rbt.insert(5)
    # rbt.insert(4)
    # rbt.insert(6)
    # rbt.insert(9)
    # rbt.insert(8)
    # rbt.insert(10)
    # rbt.preorder_traverse(rbt.get_root(), color_changer)
    #rbt.preorder_traverse(rbt.get_root(), rbt.print_node)

    #delete - case 2-2, case 2-3
    # rbt.insert(3)
    # rbt.insert(2)
    # rbt.insert(1)
    # rbt.insert(7)
    # rbt.insert(5)
    # rbt.insert(4)
    # rbt.insert(6)
    # rbt.insert(8)
    # rbt.preorder_traverse(rbt.get_root(), color_changer)

    # rbt.remove(2)
    # print("result")
    # rbt.preorder_traverse(rbt.get_root(), rbt.print_node)
    
    print('*'*100)
