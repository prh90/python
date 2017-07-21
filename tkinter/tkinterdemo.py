try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()
