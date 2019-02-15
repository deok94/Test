graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []
    # print(path)
    while queue:
        n, path = queue.pop(0)
        print(n,path)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result

def bfs(graph, start):
    visited = []
    queue = [start]
    count = 0
    while queue:
        count +=1
        print('q : '+ str(queue), 'v : '+str(visited))
        n = queue.pop(0)
        if n not in visited:
            print('===================================')
            print(n)
            visited.append(n)
            print(queue)
            print(graph[n])
            print(set(visited))

            print('===================================')
            print(graph[n] - set(visited))
            print()
            queue += graph[n] - set(visited)

    print(count)
    return visited


# print(bfs(graph, 'A'))
# print(bfs_paths(graph,'A', 'F'))
# print(bfs_paths(graph, 'D', 'F'))
# print()

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        print('s : ' + str(stack),'v : ' + str(visited))
        n = stack.pop()
        if n not in visited:
            print('===================================')
            print(n)
            visited.append(n)
            print(stack)
            print(graph[n])
            print(set(visited))
            print('===================================')
            print(graph[n] - set(visited))
            print()
            stack += graph[n] - set(visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return result

print(dfs(graph, 'A'))
# print(dfs_paths(graph, 'A', 'F'))
# print(dfs_paths(graph, 'D', 'F'))
