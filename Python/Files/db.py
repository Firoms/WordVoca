import sqlite3
import datetime
from gtts import gTTS


def add_db(lang, word, content):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Words")
    count = cursor.fetchone()[0]
    date = datetime.datetime.now()
    insert_query = f'INSERT INTO Words VALUES("{count+1}", "{lang}", "{word}", "{content}", "{date}", "False")'
    cursor.execute(insert_query)
    db.commit()
    tts1 = gTTS(text=word, lang=lang)
    tts1.save(f"../../Sound/{count+1}_1.mp3")
    tts2 = gTTS(text=content, lang='ko')
    tts2.save(f"../../Sound/{count+1}_2.mp3")


def get_ran_word(lang):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT Word, Content, Seq FROM Words Where Del=="False" and Type=="{lang}" Order by random()'
    )
    return cursor.fetchall()

def get_word_num():
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT Count(*) FROM Words Where Del=="False"'
    )
    return cursor.fetchone()[0]



def get_all_words(sort):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    if sort[1]==True:
        cursor.execute(
            f'SELECT Seq, Type, Word, Content, Date FROM Words Where Del=="False" ORDER BY {sort[0]}'
        )
    else:
        cursor.execute(
            f'SELECT Seq, Type, Word, Content, Date FROM Words Where Del=="False" ORDER BY {sort[0]} DESC'
        )
    return cursor.fetchall()

def delete_word(seq):
    db = sqlite3.connect("../../Database/Words.db")
    cursor = db.cursor()
    cursor.execute(
            f'UPDATE Words SET Del="True" Where Seq=={seq}'
        )
    db.commit()