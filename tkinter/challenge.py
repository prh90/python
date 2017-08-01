import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480+8+200')

for i in range(0, 4):
    mainWindow.columnconfigure(i, weight=100)

for i in range(0, 5):
    if i == 1:
        mainWindow.rowconfigure(1, weight=600)
    else:
        mainWindow.rowconfigure(i, weight=1000)


result = tkinter.Entry(mainWindow)
result.grid(row=0, column=2, columnspan=1, sticky='nsew')

cButton = tkinter.Button(mainWindow, text='C')
cButton.grid(row=1, column=0, sticky='e')
#
# btn = ["C", "CE", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", "=", "/"]
#
# for i in btn:
#     button = tkinter.Button(mainWindow, text=i)
#     for m in range(0, len(btn)):
#         button.grid(row=m, column=m, columnspan=1, sticky='w')

mainWindow.mainloop()
