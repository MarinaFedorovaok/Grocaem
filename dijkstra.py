from tracemalloc import start


graph ={}
graph[start] = {}
graph[start]['a'] = 6
graph[start]['b'] = 2
print(graph)