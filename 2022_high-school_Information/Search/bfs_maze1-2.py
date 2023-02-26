from collections import deque

def bfs(maze):
    n, m = len(maze), len(maze[0])
    start = (0, 0)
    target = (n-1, m-1)
    queue = deque([(start, [start])])
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = 1

    while queue:
        node, path = queue.popleft()
        x, y = node

        if node == target:
            return path

        # 현재 위치에서 네 방향으로 위치 확인
        for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            # 미로를 벗어나지 않았고, 벽이 아니고, 방문한 적이 없으면
            if (0 <= dx < n) and (0 <= dy < m) and maze[dx][dy] == 1 and not visited[dx][dy]:
                visited[dx][dy] = True                          # 현재 좌표(dx, dy) 방문 처리
                maze[dx][dy] = maze[x][y] + 1                   # 이전 칸의 값 + 1
                queue.append(((dx, dy), path + [(dx, dy)]))     # 현재 좌표(dx, dy)를 큐에 삽입

    # 우측 하단의 칸에 저장된 값 반환
    return None

# 이동할 수 있는 칸은 1, 벽은 0으로 표기한다.
maze = [[1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1]]

shortest_path = bfs(maze)

if shortest_path:
    # 미로를 탈출하는 최소한의 칸 수 출력
    print(f'미로를 탈출하는 최소의 칸 수: {maze[6][6]}')
    print('*** 미로 탈출 경로 ***')
    for i in shortest_path:
        print(i)
else:
    print("최단 경로 없음")
