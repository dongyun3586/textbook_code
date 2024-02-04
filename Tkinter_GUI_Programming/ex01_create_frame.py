from tkinter import *
import tkinter.ttk as ttk   # Combobox, Progressbar

root = Tk()
root.title("GUI Test")
root.geometry("480x640")                        # (가로 * 세로) 크기 + x좌표 + y좌표
root.resizable(False, False)        # 창 크기 변경 설정: 너비, 높이

#region 버튼 위젯
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, text="버튼2", padx=50, pady=10)       # padding 설정
btn2.pack()

btn3 = Button(root, text="버튼3", width=50, height=1)    # 버튼 자체 크기 지정
btn3.pack()

btn4 = Button(root, text="버튼5", fg="red", bg="yellow")  # 버튼 색상 지정
btn4.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")

btn5 = Button(root, text="동작하는 버튼", command=btncmd)
btn5.pack()
#endregion

#region 레이블 위젯
label1 = Label(root, text="Hello World")
label1.pack()

def change_label():
    label1.config(text="안녕 세상아")

btn5 = Button(root, text="레이블 텍스트 변경", command=change_label)
btn5.pack()
#endregion

#region 텍스트 입력: Text(여러 줄), Entry(한 줄)
txt = Text(root, width=30, height=3)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력가능함.")

def get_text():
    print(txt.get("1.0", END))  # 1: 첫 번째 라인, 0: 0번째 column, END: 끝까지
    print(e.get())
    txt.delete("1.0", END)      # Text의 값 지우기
    e.delete(0, END)              # Entry의 값 지우기

btn6 = Button(root, text="글자 가져오기", command=get_text)
btn6.pack()
#endregion

#region 리스트 박스
listbox = Listbox(root, selectmode="extended", height=0)    # height가 0이면 다 보여주고, 1 이상이면 해당 개수 만큼만 보여줌.
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(END, "바나나")
listbox.insert(END, "포도")
listbox.pack()
#endregion

#region 체크 박스
chk_var = IntVar()     # 체크 상태를 int 형으로 저장 0(체크 해제), 1(체크)
chkbox = Checkbutton(root, text="체크해보세요.", variable=chk_var)
chkbox.pack()

def get_checkbox():
    print(chk_var.get())

btn7 = Button(root, text="CheckBox 상태 출력", command=get_checkbox)
btn7.pack()
#endregion

#region 라디오 버튼
Label(root, text="라디오 버튼을 선택해보세요.").pack()

sort_var = IntVar()     # int 형태의 값
radioBtn1 = Radiobutton(root, text="버블 정렬", value=1, variable=sort_var)
radioBtn1.select()  # 미리 선택해두기
radioBtn2 = Radiobutton(root, text="삽입 정렬", value=2, variable=sort_var)
radioBtn3 = Radiobutton(root, text="퀵 정렬", value=3, variable=sort_var)
radioBtn1.pack()
radioBtn2.pack()
radioBtn3.pack()
#endregion

#region 콤보 박스
sorts = ["버블 정렬", "삽입 정렬", "퀵 정렬"]
combobox = ttk.Combobox(root, height=3, values=sorts, state="readonly")  # state: 값을 일력 못하게
combobox.pack()
# combobox.set("정렬 알고리즘")     # 콤보박스의 초기값
combobox.current(0)               # 첫 번째 값 보이기

def get_combobox():
    print(combobox.get())   # 선택된 값 가져오기

btn8 = Button(root, text="콤보박스의 선택값 가져오기", command=get_combobox)
btn8.pack()
#endregion

#region 프로그레스바
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.pack()
#endregion

#region 메뉴
def create_new_file():
    print("새로운 파일을 만듭니다.")

my_menu = Menu(root)
# File 메뉴
menu_file = Menu(my_menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
my_menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴
my_menu.add_cascade(label="Edit")

root.config(menu=my_menu)
#endregion

#region 팝업 메시지 박스 msgbox
#endregion












root.mainloop()