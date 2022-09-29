import markdown2
import sqlite3
import os


def convert_file(filepath, name, respath):
    html = markdown2.markdown_path(filepath)
    with open(respath, "w") as resfile:
        resfile.write(f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>{name}</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    {html}
                </body>
            </html>
        """)

def create_filesystem():
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    courses = cur.execute("SELECT course FROM notes GROUP BY course")
    for course, in courses:
        os.mkdir(f"html/{course}")

def convert_all_notes():
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    data = cur.execute("SELECT file, name, course FROM notes")
    for filepath, name, course in data:
        convert_file(filepath, name, f"html/{course}/{name}.html")

def create_index():
    con = sqlite3.connect(".pnotesdb")
    cur = con.cursor()
    courses = cur.execute("SELECT course FROM notes GROUP BY course").fetchall()
    courses_links = ""
    for course, in courses:
        courses_links += f'<li><a href="{course}/index.html">{course}</a></li>'
        with open(f"html/{course}/index.html", "w") as indexfile:
            table_string = "<table><tr><td><h2>Notes</h2></td><td><h2>Cheatsheets</h2></td></tr><tr><td>"
            last_type = "notes"
            for name, note_type in cur.execute(f"SELECT name, type FROM notes WHERE course=\"{course}\" ORDER BY type DESC"):
                if last_type != note_type:
                    table_string += "</td><td>"
                    last_type = note_type
                table_string += f'<a href="{name}.html">{name}</a><br>'
            table_string += "</td></tr></table>"
            indexfile.write(f"""<!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>{course}</title>
                    </head>
                    <body>
                        <h1>{course}</h1>
                        {table_string}
                    </body>
                </html>
            """)
    with open("html/index.html", "w") as indexfile:
        indexfile.write(f"""<!DOCTYPE html>
            <html>
	            <head>
	            	<meta charset="utf-8">
	            	<title>My classes</title>
            	</head>
            	<body>
            		<h1>My classes :</h1>
            		<ul>
            			{courses_links}
            		</ul>
            	</body>
            </html>
        """)

def compile_notes():
    create_filesystem()
    create_index()
    convert_all_notes()
