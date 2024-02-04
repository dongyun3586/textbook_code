import time
import random
from tkinter import *
from tkinter.font import Font
from blocks import Block, BlockList


class SortingVisualizer():
    """정렬 알고리즘 시각화를 위한 메인 클래스
    각 정렬 알고리즘은 새로운 Tkinter 윈도우에서 시각화된다"""
    def __init__(self, sort_name):
        self.arr = None
        sort_window = Tk()
        sort_window.title(sort_name + '_sort')
        sort_window.geometry('1080x540+100+100')
        sort_window.resizable(False, False)

        self.canvas = Canvas(sort_window, width=1080, height=380)
        self.canvas.pack()
        self.canvas.create_line(0, 330, 1080, 330)

        # 정렬할 숫자 개수
        numberScale = Scale(sort_window, from_=1, to=300, orient=HORIZONTAL, label='숫자 개수', length=180, command=self.reset_array)
        numberScale.place(x=70, y=420)
        numberScale.set(20)

        # 정렬 속도(ms)
        speedScale = Scale(sort_window, from_=1, to=1000, orient=HORIZONTAL, label='속도 조절(ms)', length=180, command=self.set_speed)
        speedScale.place(x=320, y=420)
        speedScale.set(50)

        # [정렬 시작] 버튼
        sortButton = Button(sort_window, text='정렬 시작', command=lambda: getattr(self, sort_name + '_sort')())
        sortButton.place(x=580, y=420, width=180, height=30)

        # 리셋 버튼
        resetButton = Button(sort_window, text='reset', command=lambda: self.reset_array(50))
        resetButton.place(x=580, y=470, width=180, height=30)

        # 종료 버튼
        homeButton = Button(sort_window, text='exit', command=lambda: sort_window.destroy())
        homeButton.place(x=830, y=420, width=180, height=30)

        self.delay = 0.001
        self.time = None

    def reset_array(self, number):
        """정렬 숫자의 개수 변경"""
        self.arr = BlockList(random.sample(range(11, 311, 300 // int(number)), int(number)), self.canvas)
        self.canvas.delete(self.time)

    def set_speed(self, speed):
        """정렬 실행 속도 변경"""
        self.delay = 0.001 * int(speed)

    def bubble_sort(self):
        start_time = time.time()
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'red')
                self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'red')
                self.canvas.update()
                time.sleep(self.delay)

                if self.arr.data[j] > self.arr.data[j + 1]:
                    self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'yellow')
                    self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'yellow')
                    self.canvas.update()
                    time.sleep(self.delay)
                    self.arr.swap(j, j + 1)
                    self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'yellow')
                    self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'yellow')
                    self.canvas.update()
                    time.sleep(self.delay)

                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'blue')
                self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'blue')
        total_time = time.time() - start_time
        self.time = self.canvas.create_text(1030, 350, text='time: ' + str(total_time))

        for i in range(n):
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
            self.canvas.update()
            time.sleep(0.03)
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.canvas.update()

    def selection_sort(self):
        start_time = time.time()
        n = len(self.arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'red')
                self.arr.blocks[min_idx].draw(*self.arr.get_coordinates(self.arr.blocks[min_idx]), 'yellow')
                self.arr.canvas.update()
                time.sleep(self.delay)

                if self.arr.data[j] < self.arr.data[min_idx]:
                    self.arr.blocks[min_idx].draw(*self.arr.get_coordinates(self.arr.blocks[min_idx]), 'blue')
                    if min_idx == i:
                        self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
                    min_idx = j

                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'blue')
                self.arr.blocks[min_idx].draw(*self.arr.get_coordinates(self.arr.blocks[min_idx]), 'blue')

            self.arr.swap(i, min_idx)
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
            self.arr.blocks[min_idx].draw(*self.arr.get_coordinates(self.arr.blocks[min_idx]), 'yellow')
            self.arr.canvas.update()
            time.sleep(self.delay)

            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.arr.blocks[min_idx].draw(*self.arr.get_coordinates(self.arr.blocks[min_idx]), 'blue')

        total_time = time.time() - start_time
        self.time = self.canvas.create_text(1030, 350, text='time: ' + str(total_time))

        for i in range(n):
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
            self.canvas.update()
            time.sleep(0.03)
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.canvas.update()

    def insertion_sort(self):
        start_time = time.time()
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr.data[i]
            j = i - 1
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'red')
            self.arr.canvas.update()
            time.sleep(self.delay)

            while j >= 0 and self.arr.data[j] > key:
                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'red')
                self.arr.canvas.update()
                time.sleep(self.delay)

                self.arr.swap(j, j + 1)
                j -= 1

                self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'blue')
                self.arr.blocks[j].draw(*self.arr.get_coordinates(self.arr.blocks[j]), 'blue')
                self.arr.canvas.update()
                time.sleep(self.delay)

            self.arr.data[j + 1] = key

            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.arr.blocks[j + 1].draw(*self.arr.get_coordinates(self.arr.blocks[j + 1]), 'blue')
            self.arr.canvas.update()
            time.sleep(self.delay)

        total_time = time.time() - start_time
        self.time = self.canvas.create_text(1030, 350, text='time: ' + str(total_time))

        for i in range(n):
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
            self.canvas.update()
            time.sleep(0.03)
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.canvas.update()

    def quick_sort(self):
        n = len(self.arr)
        start_time = time.time()
        self.quick_sort_recursion(0, n - 1)
        total_time = time.time() - start_time
        self.time = self.canvas.create_text(1030, 350, text='time: ' + str(total_time))

        for i in range(len(self.arr)):
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'yellow')
            self.canvas.update()
            time.sleep(0.03)
            self.arr.blocks[i].draw(*self.arr.get_coordinates(self.arr.blocks[i]), 'blue')
            self.canvas.update()

    def quick_sort_recursion(self, start, end):
        if start >= end:
            return

        pivot = start
        left, right = start + 1, end

        while left <= right:
            while left <= right and self.arr.data[left] <= self.arr.data[pivot]:
                self.arr.blocks[left].draw(*self.arr.get_coordinates(self.arr.blocks[left]), 'blue')
                left += 1
                if left < len(self.arr.data):
                    self.arr.blocks[left].draw(*self.arr.get_coordinates(self.arr.blocks[left]), 'red')
                self.arr.canvas.update()
                time.sleep(self.delay)

            while left <= right and self.arr.data[right] >= self.arr.data[pivot]:
                self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'blue')
                right -= 1
                if right > 0:
                    self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'red')
                self.arr.canvas.update()
                time.sleep(self.delay)

            if left < right:
                self.arr.blocks[left].draw(*self.arr.get_coordinates(self.arr.blocks[left]), 'yellow')
                self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'yellow')
                self.arr.canvas.update()
                time.sleep(self.delay)
                self.arr.swap(left, right)
                self.arr.blocks[left].draw(*self.arr.get_coordinates(self.arr.blocks[left]), 'yellow')
                self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'yellow')
                self.arr.canvas.update()
                time.sleep(self.delay)

                self.arr.blocks[left].draw(*self.arr.get_coordinates(self.arr.blocks[left]), 'blue')
                self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'blue')

        self.arr.blocks[pivot].draw(*self.arr.get_coordinates(self.arr.blocks[pivot]), 'yellow')
        self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'yellow')
        self.arr.canvas.update()
        time.sleep(self.delay)
        self.arr.swap(pivot, right)
        self.arr.blocks[pivot].draw(*self.arr.get_coordinates(self.arr.blocks[pivot]), 'yellow')
        self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'yellow')
        self.arr.canvas.update()
        time.sleep(self.delay)

        self.arr.blocks[pivot].draw(*self.arr.get_coordinates(self.arr.blocks[pivot]), 'blue')
        self.arr.blocks[right].draw(*self.arr.get_coordinates(self.arr.blocks[right]), 'blue')

        self.quick_sort_recursion(start, right - 1)
        self.quick_sort_recursion(right + 1, end)


def set_root():
    root.title("정렬 알고리즘 시각화 프로그램")
    root.resizable(False, False)
    custom_font = Font(size=20)  # 사용자 정의 글꼴과 크기를 설정

    # 창의 크기 설정
    window_width = 500
    window_height = 300

    # 화면의 중앙 좌표 계산
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # 창의 위치와 크기 설정
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    btn1_bubbleSort = Button(root, text='버블 정렬(Bubble sort)', font=custom_font, command=lambda: SortingVisualizer('bubble'))
    btn1_bubbleSort.pack(fill='both', expand=True)  # fill='both'와 expand=True 옵션을 사용하여 버튼이 창의 세로 방향으로 균등하게 배치되도록 설정

    btn2_insertionSort = Button(root, text='삽입 정렬(Insertion sort)', font=custom_font, command=lambda: SortingVisualizer('insertion'))
    btn2_insertionSort.pack(fill='both', expand=True)

    btn3_quickSort = Button(root, text='퀵 정렬(Quick sort)', font=custom_font, command=lambda: SortingVisualizer('quick'))
    btn3_quickSort.pack(fill='both', expand=True)


root = Tk()
set_root()
root.mainloop()