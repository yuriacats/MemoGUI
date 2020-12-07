import eel
import os
from tkinter import filedialog, Tk
import datetime
import platform
import sqlite3

eel.init('web', allowed_extensions=['.js', '.html'])
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
    # ここに原因がありそう。明日までに調べる。
    root.update()
    if system == "Windows":
        root.withdraw()
    # path = Path(path_str)
    print(os.access(path_str, os.W_OK))
    return path_str


@eel.expose
def edit_date():
    now_time = str(datetime.datetime.now())
    now_date, now_time = now_time.split()
    now_date = str(now_date)
    # print(now_date)
    return now_date


@eel.expose
def output_templates(title, date, markdown):
    blog_config = []
    blog_config.append("---")
    blog_config.append("title: " + title)
    blog_config.append("date: " + date)
    blog_config.append("---")
    blog_config.append("# " + title)
    blog_config.append(markdown)
    # print(blogConfig)
    # ここに、このディレクトリーにテンプレートを作るかの確認をする。

    base_dir_path = select_file()

    new_dir_path = base_dir_path + "/" + date
    if (os.path.isdir(new_dir_path)):
        files = os.listdir(path=base_dir_path + "/")
        today_blogs = []
        for i in files:
            if (i[:10] == date):
                today_blogs.append(i)
        new_num = len(today_blogs) + 1
        print(new_num)
        new_dir_path = new_dir_path + "-" + str(new_num)

    print(os.path.isdir(base_dir_path))
    os.mkdir(new_dir_path)
    print(new_dir_path)
    new_path = new_dir_path + "/index.md"

    with open(new_path, mode='w')as f:
        f.write('\n'.join(blog_config))
    return 0


@eel.expose
def input_memos(memo_title, memo_text):
    print(memo_title)
    print(memo_text)
    conn = sqlite3.connect('memo.db', isolation_level=None)
    # auto-commit有効。パフォーマンス的には手動のほうがいい説
    # https://glorificatio.org/archives/1582
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS  items(
        item_id INTEGER PRIMARY KEY UNIQUE,
        name TEXT ,
        memo_text TEXT 
    ) """)
    conn.execute("INSERT INTO items (name, memo_text) VALUES (?,?)", (memo_title, memo_text))
    conn.close()


    # memoReload()
    return memo_reload()


@eel.expose
def memo_reload():
    return output_memos()

@eel.expose
def output_memos():
    # 書き込みの確認コード、中身的にはOutputMemos管轄
    conn = sqlite3.connect('memo.db')
    cur = conn.cursor()
    return_data = []
    for data_row in cur.execute("SELECT name, memo_text FROM items "):
        return_data.append([data_row[0], data_row[1]])
        # print(data_row[0])
        # print(data_row[1])
    conn.close()
    return return_data


eel.start('html/index.html')
