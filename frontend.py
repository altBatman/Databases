import tkinter as tk

window=tk.Tk()

l1=tk.Label(window, text="Word :")
l1.grid(row=0,column=0)

e1_value= tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

b1=tk.Button(window,text="Search")
b1.grid(row=0,column=2)

t1=tk.Text(window,height=4, width=60)
t1.grid(row=1, column=0, rowspan=1, columnspan=3)

window.mainloop()
