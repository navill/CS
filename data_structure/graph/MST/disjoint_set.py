class DisjointSet:
    def __init__(self, vnum):
        self.parent=[-1 for _ in range(vnum)]

    def simple_find(self, i):
        while self.parent[i] >= 0:
            i=self.parent[i]
        return i

    def simple_union(self, i, j):
        self.parent[j]+=self.parent[i]
        self.parent[i]=j

    def collapsing_find(self, i):
        root=trail=lead=None
        #find the root
        root=i
        while self.parent[root] >= 0:
            root=self.parent[root]

        #make all nodes to children of the root
        trail=i
        while trail != root:
            lead=self.parent[trail]
            self.parent[trail]=root
            trail=lead

        return root

    def weighted_union(self, i, j):
        """
        paremeters i, j must be roots!
        if size[i] < size[j] then parent[i]=j
        """
        #abs(parent[i])=size[i]
        #temp_cnt is negative and the sum of size[i], size[j]
        temp_cnt=self.parent[i]+self.parent[j]

        #size[i] < size[j] : consider signs!!
        if self.parent[i] > self.parent[j]:
            self.parent[i]=j
            self.parent[j]=temp_cnt
        #size[i] > size[j]
        else:
            self.parent[j]=i
            self.parent[i]=temp_cnt

if __name__=="__main__":
    ds=DisjointSet(5)

    # ds.simple_union(4, 2)
    # ds.simple_union(0, 4)
    # ds.simple_union(1, 0)
    # ds.simple_union(3, 1)
    # print(ds.parent)

    # print(ds.simple_find(4), ds.simple_find(0),
    #     ds.simple_find(1), ds.simple_find(3))

    # print(ds.collapsing_find(3))
    # print(ds.parent)

    ds.simple_union(4, 2)
    ds.simple_union(0, 4)
    ds.simple_union(3, 1)
    ds.parent[2]=-3
    ds.parent[1]=-2

    ds.weighted_union(2, 1)
    print(ds.parent)