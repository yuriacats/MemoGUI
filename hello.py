from zipfile import Path

import eel
import os
from tkinter import filedialog, Tk
import datetime
import platform

eel.init('web', allowed_extensions=['.js', '.html'])
@eel.expose
def sey_hello_py(x):
    print('Hello form %s' %x)

root = Tk()
root.geometry("0x0")
root.overrideredirect(1)
root.withdraw()
system = platform.system()

def select_file():
    if system == "Windows":
        root.deiconify()
    root.update()
    root.lift()
    root.focus_force()
    path_str = filedialog.askdirectory()
    #ここに原因がありそう。明日までに調べる。
    root.update()
    if system == "Windows":
        root.withdraw()
    path = Path(path_str)
    print(os.access(path_str, os.W_OK))
    return path_str

@eel.expose
def Timer():
    nowtime=str(datetime.datetime.now())
    now_date, now_time = nowtime.split()
    now_date=str(now_date)
    #print(now_date)
    return now_date

@eel.expose
def outputTemplates(title,date,markdown):
    blogConfig=[]
    blogConfig.append("---")
    blogConfig.append("title: "+title)
    blogConfig.append("date: "+date)
    blogConfig.append("---")
    blogConfig.append("# "+title)
    blogConfig.append(markdown)
    #print(blogConfig)
        #ここに、このディレクトリーにテンプレートを作るかの確認をする。

    base_dir_path= select_file()

    new_dir_path=base_dir_path+"templates/"+date
    if(os.path.isdir(new_dir_path)):
        files=os.listdir(path=base_dir_path+"templates/")
        todayblogs=[]
        for i in files:
            if(i[:10]==date):
                todayblogs.append(i)
        newNum=len(todayblogs)+1
        print(newNum)
        new_dir_path=new_dir_path+"-"+str(newNum)

    print(os.path.isdir(base_dir_path))
    os.mkdir(new_dir_path)
    print(new_dir_path)
    new_path=new_dir_path+"/index.md"

    with open(new_path,mode='w')as f:
        f.write('\n'.join(blogConfig))
    return 0



eel.start('html/index.html')
