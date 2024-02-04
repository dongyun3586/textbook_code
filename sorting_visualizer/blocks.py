from tkinter import *
from collections import UserList


class Block:
    """각 정렬 요소를 나타내는 블록 표현한다"""
    def __init__(self, height: int, canvas: Canvas, index: int):
        self.height = height
        self.canvas = canvas
        self.index = index
        self.block = None

    def draw(self, x1, y, x2, color):
        """캔버스에 블록을 그린다"""
        if self.block:
            self.canvas.delete(self.block)
        self.block = self.canvas.create_rectangle(x1, y, x2, 330, fill=color)


class BlockList(UserList):
    """정렬될 블록들의 리스트를 관리한다
    UserList를 상속받아 정렬 중 블록들의 위치 변경, 추가 등의 기능을 수행한다"""
    def __init__(self, data, canvas):
        super().__init__(data)
        self.canvas = canvas
        self.blocks = []
        self.draw()

    def draw(self):
        self.canvas.delete('all')
        self.blocks = []
        for i, height in enumerate(self):
            block = Block(height, self.canvas, i)
            self.blocks.append(block)
            x1, y, x2 = self.get_coordinates(block)
            block.draw(x1, y, x2, 'blue')

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]
        self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]
        self.draw()

    def add(self, x):
        self.append(x)
        self.draw()

    def get_coordinates(self, block: Block):
        x1 = 1080 / len(self) * block.index
        x2 = 1080 / len(self) * (block.index + 1)
        y = 330 - block.height
        return x1, y, x2