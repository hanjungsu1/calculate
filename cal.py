import tkinter as tk
import math

# 계산 로직
def calculate():
    try:
        # 사용자가 '√' 기호를 사용할 수 있도록 변환
        expression = entry.get().replace('√', 'math.sqrt')
        result = eval(expression, {'__builtins__': None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"오류: {e}")

# 입력 필드 초기화
def clear_entry():
    entry.delete(0, tk.END)

# 오류 메시지를 지우는 함수
def clear_error(event):
    if "오류:" in entry.get():
        entry.delete(0, tk.END)

# UI 설정
root = tk.Tk()
root.title("계산기")

entry = tk.Entry(root, width=40, borderwidth=5) # entry : 계산 입력칸
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
entry.bind("<Key>", clear_error) # 키보드 입력 이벤트 바인딩

# 숫자 버튼
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '√', '0', '.', '+',
    'C', '(', ')', '='
]

row_val = 1
col_val = 0

for button in buttons:
    def cmd(x=button):
        if x == '=':
            calculate()
        else:
            entry.insert(tk.END, x)
    tk.Button(root, text=button, width=9, height=3, command=cmd).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# '=' 버튼
equal_button = tk.Button(root, text='=', width=9, height=3, command=calculate)
equal_button.grid(row=5, column=3)

# 'C' 버튼 (초기화 버튼)
clear_button = tk.Button(root, text='C', width=9, height=3, command=clear_entry)
clear_button.grid(row=5, column=0)

root.mainloop()
