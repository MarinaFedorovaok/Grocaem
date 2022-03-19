graph = {}
graph['me'] = ['serg', 'regina', 'irina'] 
graph['serg'] = ['sergei', 'anna']
graph['regina'] = ['ilya', 'nachalnik']
graph['ilya'] = []
graph['anna'] = ['husband']
#print(graph)
from collections import deque
from re import search
def person_get_job(name):
    return(name[-1]) == 'g'

def search_wide(name):
    search_que = deque()
    search_que += graph[name]
    searched = [] # для уже проверенных 
    while search_que:
        person = search_que.popleft()# из очереди извлекаем первого человека
        if not person in searched:
            if person_get_job(person):
                print (person + 'He will get a jog')
                return True
    else:
        search_que += graph[person] # не найдет, берем второго
        searched.append(person)
    return False
print(person_get_job('serg'))