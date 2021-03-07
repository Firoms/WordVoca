import sqlite3
import time
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def check_pin_num(num):
    db = sqlite3.connect("../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM User WHERE Pin_Num =="{num}"')
    result = cursor.fetchone()
    return str(result)


def check_seq_user():
    db = sqlite3.connect(f"../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM User")
    count = cursor.fetchone()[0]
    return int(count)


def get_last_user():
    db = sqlite3.connect(f"../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT Name, Content FROM User Order By "Seq" DESC')
    try:
        data = cursor.fetchone()
        return list(data)
    except:
        return ["No Data", "No Data"]


def check_seq_list():
    db = sqlite3.connect(f"../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM List")
    count = cursor.fetchone()[0]
    return int(count)


def get_last_list():
    db = sqlite3.connect(f"../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT Date, Time, Name, Content FROM List Order By "Seq" DESC')
    try:
        data = cursor.fetchone()
        return list(data)
    except:
        return ["No Data", "No Data", "No Data", "No Data"]


def get_list(sort, desc):
    db = sqlite3.connect(f"../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM List")
    count_lists = cursor.fetchone()[0]
    get_list = []
    if int(desc) == 0:
        cursor.execute(f'SELECT * FROM List Order By "{sort}"')
    else:
        cursor.execute(f'SELECT * FROM List Order By "{sort}" DESC')

    for i in range(count_lists):
        li = cursor.fetchone()[1:]
        get_list.append(li)
    return get_list


def input_Name(num, name, content):
    db = sqlite3.connect("../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM User")
    count = cursor.fetchone()[0]
    insert_query = f"INSERT INTO User VALUES('{count+1}','{num}','{name}','{content}')"
    cursor.execute(insert_query)
    db.commit()


def save(num):
    db = sqlite3.connect("../../database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM List")
    count = cursor.fetchone()[0]
    cursor.execute(f'SELECT Name, Content FROM User WHERE Pin_Num =="{num}"')
    data = cursor.fetchone()
    name = data[0]
    content = data[1]
    now = time.localtime()
    Date = "%04d년 %02d월 %02d일" % (now.tm_year, now.tm_mon, now.tm_mday)
    Time = "%02d시 %02d분 %02d초" % (now.tm_hour, now.tm_min, now.tm_sec)
    insert_query = (
        f"INSERT INTO List VALUES('{count+1}','{Date}','{Time}','{name}','{content}')"
    )
    cursor.execute(insert_query)
    db.commit()
