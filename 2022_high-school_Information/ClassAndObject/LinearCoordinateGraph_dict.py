import math
import matplotlib.pyplot as plt


class LinearGraph:
    def __init__(self):
        self.points = []
        self.length = 0.0

    def draw_linear_graph(self):
        # 리스트 내포로 x, y 좌표 리스트 생성
        x = [point['x'] for point in self.points]
        y = [point['y'] for point in self.points]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def calculate_distance(self):
        for i in range(len(self.points) - 1):
            dx = self.points[i + 1]['x'] - self.points[i]['x']
            dy = self.points[i + 1]['y'] - self.points[i]['y']
            self.length += math.sqrt(dx * dx + dy * dy)
        print('모든 좌표간의 거리: ', self.length)


if __name__ == '__main__':
    graph = LinearGraph()
    points = [(0, 0), (1, 2), (2, 0), (3, 2), (4, 0)]
    for point in points:
        x, y = point
        graph.points.append({'x': x, 'y': y})

    # 모든 좌표를 연결하는 그래프 출력
    graph.draw_linear_graph()

    # 모든 좌표의 거리 계산
    graph.calculate_distance()
