import sqlite3
import datetime


def add_db(lang, word, content):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Words")
    count = cursor.fetchone()[0]
    date = datetime.datetime.now()
    insert_query = f"INSERT INTO Words VALUES('{count+1}', '{lang}', '{word}', '{content}', '{date}', '0')"
    cursor.execute(insert_query)
    db.commit()


def get_ran_word(lang):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Word, Content FROM Words Where Del=='0' and Type=='{lang}' Order by random()"
    )
    return cursor.fetchall()
