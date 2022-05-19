import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
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

    queue = []
    queue.append(str(start))
    visited = set()
    visited.add(start)
    num_visited=0
    tem=0
    lastnode = {}
    while ( len(queue)!=0 ) :
        if queue[0] in roaddict:
            for nearnodestr in roaddict[queue[0]]:
                nearnode=int(nearnodestr[0])
                if nearnode not in visited:
                    num_visited+=1
                    visited.add(nearnode)
                    if nearnode!= end:
                        queue.append(nearnodestr[0])
                        lastnode[nearnode] = (int(queue[0]),float(nearnodestr[1]))
                    else:
                        lastnode[nearnode] = (int(queue[0]),float(nearnodestr[1]))
                        tem=1
                        break
                else :
                    continue
        queue.pop(0)
        if(tem==1):
            break
    path = []
    path.append(end)
    dist = 0
    while (path[-1]!= start) :
        dist += lastnode[path[-1]][1]
        path.append(lastnode[path[-1]][0])
    return path,dist,num_visited
    raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
