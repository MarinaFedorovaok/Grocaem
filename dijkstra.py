from concurrent.futures import process
from json import load
from tracemalloc import start


graph ={}
graph[start] = {}
graph[start]['a'] = 6
graph[start]['b'] = 2
#print(graph[start].keys())
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
# print(graph)
infinity = float('inf')# бесконечность 
#веса
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
#родители
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None
#массив для отбработанных узлов
processed = []
#подготовка завершена, алгоритм:
    # пока остаются узлы
    # взять узел, ближайший к началу
    # обновить стоимости соседей
    # если стоимости были обновлены, обновить и родителей
    # пометить узел как обработанный
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        print(cost)
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            print(lowest_cost)
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neibours = graph[node]
    for n in neibours.keys():
        new_cost = cost+neibours[n]
        if costs[n]>new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)



