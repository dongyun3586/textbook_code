from collections import deque

def bfs(maze):
    n, m = len(maze), len(maze[0])
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * n for i in range(m)]
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            # 미로를 벗어나지 않았고, 벽이 아닌 경우
            if (0 <= dx < n) and (0 <= dy < m) and maze[dx][dy] == 1 and visited[dx][dy] == 0:
                visited[dx][dy] = 1                 # 현재 좌표(dx, dy) 방문 처리
                maze[dx][dy] = maze[x][y] + 1       # 이전 칸의 값 + 1
                queue.append((dx, dy))              # 현재 좌표(dx, dy)를 큐에 삽입

    # 우측 하단의 칸에 저장된 값 반환
    return maze[n - 1][m - 1]

# 이동할 수 있는 칸은 1, 벽은 0으로 표기한다.
maze = [[1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1]]

total_count = bfs(maze)
print(f'미로 탈출 최단 거리: {total_count}')
print()

# stack = []
# stack.push((len(maze), len(maze[0])))
#
# for i in range(total_count-1, 1, -1):
