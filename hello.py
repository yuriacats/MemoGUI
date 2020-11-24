import eel
import makeFiles
import os
import io
import datetime

eel.init('web', allowed_extensions=['.js', '.html'])
@eel.expose
def sey_hello_py(x):
    print('Hello form %s' %x)


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
    base_dir_path="/Users/tsuchitahika/project/MemoGUI/"
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
