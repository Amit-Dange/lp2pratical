# 1. sort all edges in non decreasing order of wt
# 2. i)pick the smallest edge
#    ii)check if adding the edge form cycle
#    iii)if cycle not formed -> INCLUDE ; else -> EXCLUDE
# 3. repeat step2 unless v-1 edges are included
class Node:
    def __init__(self, parent, rank):
        self.parent = parent  # Parent node index in the disjoint set forest
        self.rank = rank      # Rank of the node for union-by-rank

class Edge:
    def __init__(self, src, dest, wt):
        self.src = src    # Source vertex of the edge
        self.dest = dest  # Destination vertex of the edge
        self.wt = wt      # Weight of the edge

def find(dsuf, v):
    """Find operation in disjoint set."""
    # If the node is the representative (parent), return its index
    if dsuf[v - 1].parent == -1:
        return v - 1
    # Path compression: Update parent of all nodes in the path to root
    dsuf[v - 1].parent = find(dsuf, dsuf[v - 1].parent + 1)
    return dsuf[v - 1].parent

def union_op(dsuf, fromP, toP):
    """Union operation in disjoint set."""
    # Attach smaller rank tree under root of higher rank tree
    if dsuf[fromP].rank > dsuf[toP].rank:
        dsuf[toP].parent = fromP
        dsuf[fromP].rank += 1
    elif dsuf[fromP].rank < dsuf[toP].rank:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1
    else:  # If ranks are the same, make one as root and increment its rank
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1

def kruskals(edge_list, V, E):
    """Kruskal's algorithm to find MST."""
    # Sort edges by weight in non-decreasing order
    edge_list.sort(key=lambda x: x.wt)
    mst = []
    # Initialize disjoint set forest
    dsuf = [Node(-1, 0) for _ in range(V)]
    i = 0
    j = 0
    # Repeat until V-1 edges are included in MST or all edges are considered
    while i < (V - 1) and j < E:
        fromP = find(dsuf, edge_list[j].src)
        toP = find(dsuf, edge_list[j].dest)
        # Check if adding the edge forms a cycle
        if fromP == toP:
            j += 1
            continue
        # Union the sets if adding the edge doesn't form a cycle
        union_op(dsuf, fromP, toP)
        # Include the edge in MST
        mst.append(edge_list[j])
        i += 1
    return mst

def printMST(mst):
    """Print the edges of MST."""
    for edge in mst:
        print("\nsrc :", edge.src)
        print("dest :", edge.dest)
        print("wt :", edge.wt, "\n")

if __name__ == "__main__":
    # Input the number of edges and vertices
    E, V = map(int, input("Enter the number of edges and vertices: ").split())
    edge_list = []

    # Input the edges: source, destination, weight
    for _ in range(E):
        s, d, w = map(int, input().split())
        edge_list.append(Edge(s, d, w))

    # Find MST using Kruskal's algorithm
    mst = kruskals(edge_list, V, E)
    # Print the edges of MST
    printMST(mst)
