from disjoint_set import DisjointSet

class GNode:
    def __init__(self, vertex=None, weight=None):
        self.vertex=vertex
        self.weight=weight
        self.link=None

class Edge:
    def __init__(self, v1, v2, weight):
        self.v1=v1
        self.v2=v2
        self.weight=weight

class Graph:
    def __init__(self):
        self.adjacency_list=[]
        self.edge_list=[]

        self.vertex_num=0

    def add_vertex(self, vnum=1):
        self.adjacency_list.extend([None for _ in range(vnum)])
        self.vertex_num+=vnum
    
    def __add_node(self, vertex, node):
        cur=self.adjacency_list[vertex]
        if not cur:
            self.adjacency_list[vertex]=node
        else:
            while cur.link:
                cur=cur.link
            cur.link=node

    def insert_edge(self, u, v, weight):
        unode=GNode(u, weight)
        vnode=GNode(v, weight)

        self.__add_node(u, vnode)
        self.__add_node(v, unode)

        self.edge_list.append(Edge(u, v, weight))

    def MST_kruskal(self):
        #최종적으로 만들어질 MST
        mst=Graph(); mst.add_vertex(self.vertex_num)        
        #분리집합 : 사이클 형성 검사를 할 정점 집합
        ds=DisjointSet(self.vertex_num)
        #가중치에 따라 에지를 정렬
        self.edge_list.sort(key=lambda e: e.weight)
        #mst에 속하는 에지의 수
        mst_edge_num=0
        #정렬된 에지 리스트에서 인덱스
        edge_idx=0
        #|TE| = |TV|-1이면 종료
        while mst_edge_num < self.vertex_num-1:
            #가중치가 작은 순서대로 에지를 가져온다
            edge=self.edge_list[edge_idx]
            #FIND(u) != FIND(v)이면 사이클을 형성하지 않는다
            if ds.collapsing_find(edge.v1) != ds.collapsing_find(edge.v2):
                #TE=TE U {(u, v)}
                mst.insert_edge(edge.v1, edge.v2, edge.weight)
                #UNION(u, v)
                ds.weighted_union(ds.collapsing_find(edge.v1), ds.collapsing_find(edge.v2))
                mst_edge_num+=1
            edge_idx+=1

        return mst

    def print_edges(self):
        for edge in self.edge_list:
            print("({}, {}) : {}".format(edge.v1, edge.v2, edge.weight))

if __name__=="__main__":
    g=Graph()
    g.add_vertex(6)

    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 2)
    g.insert_edge(0, 3, 8)
    g.insert_edge(1, 2, 5)
    g.insert_edge(1, 4, 12)
    g.insert_edge(2, 3, 7)
    g.insert_edge(2, 4, 17)
    g.insert_edge(3, 4, 4)
    g.insert_edge(3, 5, 14)

    mst=g.MST_kruskal()

    mst.print_edges()
    
