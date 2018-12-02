from queue1 import Queue
from stack1 import Stack

class GNode:
    def __init__(self, vertex=None):
        self.vertex=vertex
        self.link=None

class Graph:
    def __init__(self):
        #인접 리스트로 구현
        self.adjacency_list=[]
        #방문 여부 체크
        self.visited=[]

    def add_vertex(self, vnum=1):
        self.adjacency_list.extend([None for _ in range(vnum)])
        self.visited.extend([False for _ in range(vnum)])
    
    def __add_node(self, vertex, node):
        cur=self.adjacency_list[vertex]
        #아직 에지가 하나도 없다면
        if not cur:
            self.adjacency_list[vertex]=node
        else:
            while cur.link:
                cur=cur.link
            cur.link=node

    def insert_edge(self, u, v):
        unode=GNode(u)
        vnode=GNode(v)

        self.__add_node(u, vnode)
        self.__add_node(v, unode)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i]=False

    def bfs(self, v):
        q=Queue()
        #방문 체크 리스트를 초기화한다
        #O(v)
        self.init_visited()

        #첫번째 정점을 큐에 넣고
        #방문 체크
        q.enqueue(v)
        self.visited[v]=True

        while not q.empty():
            v=q.dequeue()
            #방문
            print(v, end="  ")
            #인접 리스트를 얻어온다
            u=self.adjacency_list[v]
            while u:
                #아직 방문하지 않은 노드라면
                #큐에 넣고 방문 체크!
                if not self.visited[u.vertex]:
                    q.enqueue(u.vertex)
                    self.visited[u.vertex]=True
                u=u.link

    def __dfs_recursion(self, v):
        #방문
        print(v, end="  ")
        #방문 체크
        self.visited[v]=True

        u=self.adjacency_list[v]
        while u:
            if not self.visited[u.vertex]:
                self.__dfs_recursion(u.vertex)
            u=u.link

    def dfs(self, v):
        self.init_visited()
        self.__dfs_recursion(v)

    def iter_dfs(self, v):
        """
        시작 정점으로 돌아가 
        더 이상 방문할 정점이 없어야 종료
        """
        s=Stack()
        self.init_visited()

        s.push(v)
        #방문 체크 및 방문
        self.visited[v]=True
        print(v, end="  ")

        #아직 방문하지 않은 정점을 방문했는가
        is_visited=False

        while not s.empty():
            is_visited=False
            v=s.peek()
            #인접 리스트를 받아온다.
            u=self.adjacency_list[v]
            while u:
                if not self.visited[u.vertex]:
                    s.push(u.vertex)
                    #방문 체크 및 방문
                    self.visited[u.vertex]=True
                    print(u.vertex, end="  ")
                    #아직 방문하지 않은 정점을 방문했으므로
                    is_visited=True
                    break
                u=u.link
            if not is_visited:
                s.pop()

if __name__=="__main__":
    g=Graph()
    g.add_vertex(6)
    g.insert_edge(1, 0)
    g.insert_edge(0, 3)
    g.insert_edge(3, 4)
    g.insert_edge(4, 2)
    g.insert_edge(2, 5)

    #예상 출력 결과 : 3  0  4  1  2  5
    g.bfs(3)
    print()
    #예상 출력 결과 : 3  0  1  4  2  5
    g.dfs(3)
    print()

    g.iter_dfs(3)
    print()