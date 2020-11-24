import os
import sys
import datetime

# ===========def: s=============
def deleteEntry(event):
    datememo=DateFild.get()
    blogConfig=[]
    blogConfig.append("---")
    blogConfig.append("title: "+TitleFild.get())
    blogConfig.append("date: "+datememo)
    blogConfig.append("---")
    blogConfig.append("# "+TitleFild.get())
    #print(blogConfig)
    if(os.path.isdir("./templates")):
        #ここに、このディレクトリーにテンプレートを作るかの確認をする。
        os.mkdir("./templates")
    new_dir_path="./templates/"+datememo
    if(os.path.isdir(new_dir_path)):
        files=os.listdir(path='./templates/')
        todayblogs=[]
        for i in files:
            if(i[:10]==datememo):
                todayblogs.append(i)
        newNum=len(todayblogs)+1
        new_dir_path=new_dir_path+"-"+str(newNum)

    os.mkdir(new_dir_path)
    print(new_dir_path)
    new_path=new_dir_path+"/index.md"

    with open(new_path,mode='w')as f:
        f.write('\n'.join(blogConfig))
    TitleFild.delete(0,tk.END)
    tkm.showinfo('info',"テンプレート生成が完了しました。")

def Timer():
    nowtime=str(datetime.datetime.now())
    now_date, now_time = nowtime.split()
    return now_date


