import os, sqlite3
from datetime import datetime

def init():
    editor = input("Enter default editor command : ")
    with open(".pnotescfg", "w") as cfgfile:
        cfgfile.write(editor)
    if os.path.exists(".pnotesdb"):
        print("Pointless notes already initialized here")
        return
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    cur.execute("CREATE TABLE notes(file, name, course, date, type)")
    con.commit()
    os.mkdir("note_files")
    os.mkdir("html")


def add(course, name, note_type, filepath):
    if not os.path.exists(filepath):
        open(filepath, "x").close()
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    date = datetime.today().strftime("%Y-%m-%d")
    cur.execute(f"""INSERT INTO notes VALUES
            ('{filepath}','{name}','{course}','{date}','{note_type}')
            """)
    con.commit()

def edit(course, name):
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    cur.execute(f"SELECT file FROM notes WHERE name='{name}' AND course='{course}'")
    res = cur.fetchone()
    if res is None:
        print("Fichier introuvable")
        return
    filepath = res[0]
    with open(".pnotescfg","r") as cfgfile:
        editor = cfgfile.readline().strip()
    os.system("{} {}".format(editor, filepath))

def list_notes():
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    cur.execute("SELECT course, name, date, type FROM notes ORDER BY course")
    res = cur.fetchall()
    for c, n, d, t in res:
        print(c, n, d, t)


