graph = {
  'a' : ['b','c'],
  'b' : ['d', 'e'],
  'c' : ['f'],
  'f' : [],
  'd' : [],
  'e' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, 'a')