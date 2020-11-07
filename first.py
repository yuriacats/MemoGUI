#!/usr/vin/env/python

#-*- coding:utf-8 -*-

import os
import sys
import tkinter as tk
import tkinter.messagebox as tkm
import datetime
import tkinter.filedialog
import makeFiles


root= tk.Tk()

# ----------Code Start-----------

def showMesseage(text):
    tkm.showinfo('info',text)

def Timer():
    nowtime=str(datetime.datetime.now())
    now_date, now_time = nowtime.split()
    return now_date
def openFiles(event):
    fTyp =[("","*")]
    iDir=os.path.abspath(os.path.dirname(__file__))
    file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)



# ----------Head Config--------
root.title(u'Blog Edit Maker')
root.geometry('400x300')

# ----------edter---------------

LabelTitle = tk.Label(text=u'Hello,World', foreground='#ff0000',background='#fef9fb')
LabelTitle.pack()
TitleFild=tk.Entry(width=50)
TitleFild.insert(tk.END,u' ')
TitleFild.pack()

DateFild = tk.Entry()
DateFild.insert(tk.END, Timer())
DateFild.pack()

ImageFildButton =tk.Button(text=u'画像選択')
ImageFildButton.bind("<Button-1>",openFiles)
ImageFildButton.pack()


TitleFildButton = tk.Button(text=u'送信')
TitleFildButton.bind("<Button-1>",mekeFiles.deleteEntry)
TitleFildButton.pack()

# LambdaButton = tk.Button(text=u'messagebox',command=lambda: showMesseage(DateFild.get()))
# LambdaButton.pack()


# ---------- View --------------



# ----------  end  ---------------
root.mainloop()

