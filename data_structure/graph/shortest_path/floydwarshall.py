from copy import deepcopy
class ShortestPath:
    def __init__(self, A, path):
        #2차원 배열 A
        self.A=A
        #2차원 배열 path
        self.path=path

class Graph:
    #모든 가중치보다 충분히 큰 수(inf 대신 사용)
    BIG_NUMBER=2000
    @staticmethod
    def print_shortest_path(sp, source, dest):
        #경로 중 source와 dest를 제외하고 출력한다
        if not sp.path[source][dest]:
            return
        
        # i~k까지 출력
        Graph.print_shortest_path(sp, source, sp.path[source][dest])
        # k 출력
        print(sp.path[source][dest], end="  ")
        # k~j까지 출력
        Graph.print_shortest_path(sp, sp.path[source][dest], dest)

    def __init__(self, vnum):
        #A^-1 mat을 만들 때 if <u, v> not in E(G) then inf
        #inf 대신에 모든 가중치보다 충분히 큰 수를 사용
        self.adjacency_matrix=[[self.BIG_NUMBER for _ in range(vnum)] for _ in range(vnum)]

        for i in range(vnum):
            self.adjacency_matrix[i][i]=0
        self.vertex_num=vnum

    def insert_edge(self, u, v, w):
        self.adjacency_matrix[u][v]=w

    def floyd_warshall(self):
        #A^-1 mat
        A=deepcopy(self.adjacency_matrix)
        #경로 기록을 위한 2차원 배열
        path=[[None for _ in range(self.vertex_num)] for _ in range(self.vertex_num)]

        for k in range(self.vertex_num):
            for i in range(self.vertex_num):
                for j in range(self.vertex_num):
                    #A^k[i][j]=min{A^(k-1)[i][j], A^(k-1)[i][k]+A^(k-1)[k][j]}
                    if A[i][j] > A[i][k] + A[k][j]:
                        A[i][j]=A[i][k]+A[k][j]
                        path[i][j]=k
        
        sp=ShortestPath(A, path)
        return sp

if __name__=="__main__":
    g=Graph(4)
    g.insert_edge(0, 1, 12)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 3, 15)
    g.insert_edge(1, 2, 5)
    g.insert_edge(2, 0, 7)
    g.insert_edge(2, 1, 6)
    g.insert_edge(2, 3, 2)
    g.insert_edge(3, 1, 13)
    g.insert_edge(3, 2, 6)

    sp=g.floyd_warshall()

    for i in range(g.vertex_num):
        for j in range(g.vertex_num):
            print("{:3}".format(sp.A[i][j]), end="")
        print()

    source=0
    dest=3

    print("path from {} to {}".format(source, dest))
    print("{}".format(source), end="  ")
    g.print_shortest_path(sp, source, dest)
    print("{}".format(dest), end="  ")





