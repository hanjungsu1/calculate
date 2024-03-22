import tkinter as tk

# 계산 로직
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "오류")

# UI 설정
root = tk.Tk()
root.title("간단한 계산기")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 숫자 버튼
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
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

root.mainloop()
