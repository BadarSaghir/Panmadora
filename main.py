from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Time Manager")
window.config(padx=100,pady=50,bg=YELLOW)
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 50))
title_label.grid(row=1, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(200/2, 224/2, image=img)
canvas.create_text(100, 130,text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)
start_btn = Button(text="Start",highlightthickness=0)
end_btn = Button(text="Reset",highlightthickness=0)
start_btn.grid(row=3,column=0)
end_btn.grid(row=3,column=2)




window.mainloop()