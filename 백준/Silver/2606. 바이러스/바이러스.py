from collections import deque

def bfs(start, graph):
    queue = deque([1])
    visited = set([1])
    count = 0

    while queue:
        curr = queue.popleft()

        for next in graph[curr]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
                count += 1
    return count

vertex = int(input())
edge = int(input())
graph = {i: [] for i in range(1, vertex + 1)}

for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(1, graph))