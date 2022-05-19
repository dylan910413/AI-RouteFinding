import csv
edgeFile = 'edges.csv'


def dfs(start, end):
    # Begin your code (Part 2)
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

    stack = []
    stack.append(str(start))
    visited = set()
    visited.add(start)
    num_visited=0
    lastnode = {}
    tem = 0
    while ( len(stack) != 0 ) :
        t = stack.pop()
        if t in roaddict:
            for nearnodestr in roaddict[t]:
                nearnode = int(nearnodestr[0])
                if nearnode not in visited:
                    num_visited += 1
                    visited.add(nearnode)
                    if nearnode == end:
                        tem = 1
                        lastnode[nearnode] = (int(t),float(nearnodestr[1]))
                        break
                    else:
                        stack.append(nearnodestr[0])
                        lastnode[nearnode] = (int(t),float(nearnodestr[1]))
                else :
                    continue
        if(tem == 1):
            break
    path = []
    path.append(end)
    dist = 0
    while (path[-1] != start) :
        dist += lastnode[path[-1]][1]
        path.append(lastnode[path[-1]][0])
    return path,dist,num_visited

    raise NotImplementedError("To be implemented")
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
