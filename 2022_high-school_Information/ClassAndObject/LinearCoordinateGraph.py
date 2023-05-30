import math
import matplotlib.pyplot as plt


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LinearGraph:
    def __init__(self):
        self.points = []
        self.length = 0.0

    def draw_linear_graph(self):
        x, y = [], []
        for i in self.points:
            x.append(i.x)
            y.append(i.y)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def calculate_distance(self):
        for i in range(len(self.points) - 1):
            a = abs(self.points[i].x - self.points[i + 1].x)
            b = abs(self.points[i].y - self.points[i + 1].y)
            c = math.sqrt((a * a) + (b * b))
            self.length += c
        print('모든 좌표간의 거리: ', self.length)


if __name__ == '__main__':
    graph = LinearGraph()
    n = int(input("2차원 좌표의 개수 입력: "))

    for i in range(n):
        x, y = map(int, input("x y 좌표 입력: ").split())
        graph.points.append(Point2D(x, y))

    # 모든 좌표를 연결하는 그래프 출력
    graph.draw_linear_graph()

    # 모든 좌표의 거리 계산
    graph.calculate_distance()