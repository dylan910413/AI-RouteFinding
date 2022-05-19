import csv
from pickle import GLOBAL
from queue import PriorityQueue
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    file = open(edgeFile,mode="r")
    lines = csv.reader(file)
    roaddict = {}
    for line in lines :
        if line[0] not in roaddict:
            road = []
            road.append((line[1],line[2]))
            roaddict[line[0]] = road
        else :
            road = roaddict[line[0]]
            road.append((line[1],line[2]))
    
    cost = {str(start) : 0}
    parent = {str(start) : None}
    visited = set()
    find = PriorityQueue()
    find.put((0,str(start)))
    path = []
    num_visited = 0
    while not find.empty() :
        while not find.empty() :
            _,vertex = find.get()
            if vertex not in visited :
                break
        if vertex in roaddict :
            visited.add(vertex)
            num_visited+=1
            if int(vertex) == end : break 
            for neighbor, distance in roaddict[vertex] :
                if neighbor in visited : 
                    continue
                if neighbor not in cost : 
                    cost[neighbor] = 999999999 
                old_cost = cost[neighbor]
                new_cost = cost[vertex] + float(distance)
                if new_cost < old_cost :
                    find.put((new_cost,neighbor))
                    cost[neighbor] = new_cost
                    parent[neighbor] = vertex
    e = str(end)
    dist = cost[str(end)]
    while e is not None :
        path.append(int(e))
        e = parent[e]
    return path, dist, num_visited
    


        



    raise NotImplementedError("To be implemented")
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')

