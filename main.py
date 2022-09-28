import os
import sys
import sqlite3
from datetime import datetime

from notes_manager import *


def main(op, args):
    if op == "init":
        init()
    elif op == "add":
        course, name, note_type = args
        filepath = "note_files/" + course + "::" + name + ".md"
        add(course, name, note_type, filepath)
    elif op == "edit":
        course, name = args[0:2]
        edit(course, name)
    elif op == "create":
        course, name, note_type = args[0:3]
        if len(args) > 3:
            filepath = args[4]
        else:
            filepath = "note_files/" + course + "::" + name + ".md"
        add(course, name, note_type, filepath)
        edit(course, name)
    elif op == "list":
        list_notes()


if __name__=="__main__":
    main(sys.argv[1], sys.argv[2:])
