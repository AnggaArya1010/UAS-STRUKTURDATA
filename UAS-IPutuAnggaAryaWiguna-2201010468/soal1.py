def semua_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if not node in path:
            newpaths = semua_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def terpendek_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = terpendek_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def mencariDalam_path(Allpaths, ShortestPath):
    ListShortest = []
    for path in Allpaths:
        if len(path) == len(ShortPath):
            ListShortest.append(path)
    return ListShortest


def tampilanBlock(Paths):
    for i in range(len(Paths)):
        print('Path', i+1, '=', Paths[i])


def dapatkanSemua_Edge(graphs):
    ListEdge = []
    for keys in graphs.keys():
        if graphs[keys] != []:
            for value in graphs[keys]:
                temp = keys+' => '+value,
                ListEdge.append(temp)
    return ListEdge


data_graphSembarang = {
    'A': ['C', 'D', 'B'],
    'B': ['C', 'F', 'E'],
    'C': ['F'],
    'D': ['C', 'T', 'G'],
    'E': ['T'],
    'F': ['T'],
    'G': ['T'],
    'T': []
}

Listsemua_path = semua_path(data_graphSembarang, 'A', 'T')
print('\nSemua Path : ')

tampilanBlock(Listsemua_path)
ShortPath = terpendek_path(data_graphSembarang, 'A', 'T')

ListShortestPath = mencariDalam_path(Listsemua_path, ShortPath)
print('\nPath terpendek : ')
tampilanBlock(ListShortestPath)

SemuaEdge = dapatkanSemua_Edge(data_graphSembarang)
print('\nSemua Edge : ')

tampilanBlock(SemuaEdge)