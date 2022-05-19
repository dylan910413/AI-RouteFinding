import csv
from queue import PriorityQueue
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
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

    f = open( heuristicFile , mode = "r" )
    l = csv.reader(f)
    heuristic = {}
    for line in l :
        if line[0] == 'node' :
            continue
        heuristic[line[0]] = float(line[3])

    cost = {str(start) : 0}
    parent = {str(start) : None}
    visited = set()
    find = PriorityQueue()
    find.put((heuristic[str(start)], str(start)))
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
                    cost[neighbor] = 999999999999999 
                old_cost = cost[neighbor]
                new_cost = cost[vertex] + float(distance)
                if new_cost < old_cost :
                    find.put((new_cost + heuristic[neighbor],neighbor))
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
    path, dist, num_visited = astar(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')


