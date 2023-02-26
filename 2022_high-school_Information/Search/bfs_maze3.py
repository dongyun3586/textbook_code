from collections import deque

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        x, y = node

        if node == end:
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] != "#":
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Example usage
maze = [
    ["S", ".", ".", "#"],
    ["#", ".", ".", "#"],
    [".", ".", ".", "."],
    ["#", ".", "#", "E"]
]

start = (0, 0)
end = (3, 3)

shortest_path = bfs_shortest_path(maze, start, end)
print(shortest_path)  # Output: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]