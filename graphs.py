graph = {}
graph['me'] = ['serg', 'regina', 'irina'] 
graph['serg'] = ['sergei', 'anna']
graph['regina'] = ['ilya', 'nachalnik']
graph['ilya'] = []
graph['anna'] = ['husband']
#print(graph)
from collections import deque
from re import search
search_que = deque()
search_que += graph['me']
def person_get_job(name):
    return name[-1] == 'r'
person_get_job('serg')
def find_job():
    while search_que:
        person = search_que.popleft()# из очереди извлекаем первого человека
        if person_get_job:
            print (person + 'He will get a jog')
        return True
    else:
        search_que += graph[person] # не найдет, берем второго
    return False
print ({find_job})