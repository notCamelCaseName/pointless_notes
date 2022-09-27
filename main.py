import os
import sys
import sqlite3
from datetime import datetime


def main(op, args):
    if op == "init":
        init()
    elif op == "add":
        course, name, note_type = args
        filepath = "note_files/" + name
        add(course, name, note_type, filepath)
    elif op == "edit":
        name = args[0]
        edit(name)
    elif op == "create":
        course, name, note_type = args
        filepath = "note_files/" + name
        add(course, name, note_type, filepath)
        edit(name)
    elif op == "list":
        list_notes()


def init():
    if os.path.exists(".notesdb"):
        print("Pointless notes already initialized here")
        return
    con = sqlite3.connect(".notesdb")
    cur = con.cursor()
    cur.execute("CREATE TABLE notes(file, name, course, date, type)")
    con.commit()
    os.mkdir("note_files")
    os.mkdir("html")


def add(course, name, note_type, filepath):
    if not os.path.exists(filepath):
        open(filepath, "x").close()
    con = sqlite3.connect(".notesdb")
    cur = con.cursor()
    date = datetime.today().strftime("%Y-%m-%d")
    cur.execute(f"""INSERT INTO notes VALUES
            ('{filepath}','{name}','{course}','{date}','{note_type}')
            """)
    con.commit()

def edit(name):
    con = sqlite3.connect(".notesdb")
    cur = con.cursor()
    cur.execute(f"SELECT file FROM notes WHERE name='{name}'")
    res = cur.fetchone()
    if res is None:
        print("Fichier introuvable")
        return
    filepath = res[0]
    os.system("{} {}".format(os.getenv("EDITOR"), filepath))

def list_notes():
    con = sqlite3.connect(".notesdb")
    cur = con.cursor()
    cur.execute("SELECT course, name, date, type FROM notes ORDER BY course")
    res = cur.fetchall()
    for c, n, d, t in res:
        print(c, n, d, t)


if __name__=="__main__":
    main(sys.argv[1], sys.argv[2:])
