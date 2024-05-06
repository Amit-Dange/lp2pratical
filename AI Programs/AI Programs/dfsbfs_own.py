graph1 = {
    'A' :['D','C','B'] ,'B':['E'],'C': ['D' , 'E'] , 'D' :[], 'E':[]
}

visited = set()

def dfs (visited , graph , root):
    if root not in visited :
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited , graph , neighbour)

# dfs(visited ,graph1 , 'A' )

# ................................................
import collections

graph2 = {
    0:[1,2,3],1:[0,2],2:[0,4],3:[0],4:[2]
}

def bfs(graph , root):
    visited = set()
    queue = collections.deque([root])
    
    while queue :
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)



bfs(graph2 ,0)    