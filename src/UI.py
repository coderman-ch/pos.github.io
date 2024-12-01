from tkinter.filedialog import askdirectory
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
response = None
def FileSave():
    r = tk.filedialog.asksaveasfilename(title='Noname',initialfile='.',filetypes=[('HTML', '*.html *.htm'), ('All files', '*')])
    return r
def Save2():
    name=FileSave()
    try:
        if response.status_code == 200:
            try:
                with open(name.get(), 'wb') as file:
                    file.write(response.content)
            except:
                OUTPUT.configure(text="Faild",bg="red")
            else:
                OUTPUT.configure(text="Succeed", bg="green")
        else:
            OUTPUT.configure(text="Faild", bg="red")
    except:
        OUTPUT.configure(text="Faild", bg="red")
    else:
        OUTPUT.configure(text="Succeed", bg="green")    
def Aget():
    try:
        global response
        response = requests.get(url.get())
    except:
        OUTPUT.configure(text="Faild", bg="red")
    else:
        if response.status_code == 200:
            OUTPUT.configure(text="Succeed", bg="green")
        else:
            OUTPUT.configure(text="Faild", bg="red")
def empty():
    Label(Rf,text="").pack()
def clear():
    msg7 = messagebox.askyesno(title="Clear", message="Clear all?")
    if(msg7):
        url.delete(0, len(url.get()))
def selectPath():
    path_ = askdirectory()
    if path_ == "":
        path.get()
    else:
        path_ = path_.replace("/", "\\")
        path.set(path_)
def save_file():
    file_path = filedialog.asksaveasfilename(title=u'保存文件')
    file_text = text1.get('1.0', tk.END)
    if file_path is not None:
        with open(file=file_path, mode='a+', encoding='utf-8') as file:
            file.write(file_text)
        text1.delete('1.0', tk.END)
root = Tk()
root.geometry("500x270")
root.title("Download")
root.iconbitmap("ico.ico")
root.resizable(True,False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
but = Button(root, text="AGet", command=Aget,relief='flat', bg="yellow")
but.pack()
clear = Button(root, text="Clear", command=clear,bg="yellow", relief='flat')
lab=Label(root,text="Output",bg="yellow")
lab.pack();
Rf = LabelFrame(root, labelwidget=clear, bd=12)
Rf.pack(fill="both", padx=5)
empty()
fr1 = LabelFrame(Rf, labelwidget=but, bd=6)
fr1.pack(fill="both", padx=10)
empty()
fr3 = LabelFrame(Rf, labelwidget=lab, bd=6)
fr3.pack(fill="both", padx=10)
empty()
empty()
OUTPUT = Label(fr3, text="None")
OUTPUT.pack();
url = Entry(fr1, width=screen_width)
url.pack()
but2 =Button(fr1, text="Save", command=Save2,relief='flat')
but2.pack()
path = StringVar()
mainloop()