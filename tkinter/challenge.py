import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480+8+200')

for i in range(0, 4):
    mainWindow.columnconfigure(i, weight=1)

for i in range(0, 5):
    if i == 1:
        mainWindow.rowconfigure(1, weight=100)
    else:
        mainWindow.rowconfigure(i, weight=1)


result = tkinter.Entry(mainWindow)
result.grid(row=0, column=2, columnspan=1, sticky='nsew')

btn = ["C", "CE", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", "=", "/"]

for i in btn:
    button = tkinter.Button(mainWindow, text=i)
    # for m in len(btn):
    #     button.grid(row=1, column=2, columnspan=1, sticky='w')

mainWindow.mainloop()
