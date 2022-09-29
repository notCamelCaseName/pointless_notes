# Pointless notes
Easy command line based notes manager because i'm too lazy to learn to use anything else

## Features
* Notes creation and editing
* Notes ordering in a filesystem by subject and type
* Convert notes to a static website

## Installation
Simply clone the repository and run install.sh

## How to use
There are 6 commands to use pointless notes, all used with the syntax `pnotes [command] (args)`

### init
Use this command first, needed to initialize pointless notes in tour folder.
No args required
Will create 2 folders : `note_files` and `html` as well as a config file `.pnotescfg` and a database `.pnotesdb` required to use pointless notes
> Will ask you to enter command to open your favourite editor

### add
Use this command to add a file to the notes system.
`pnotes add [course] [name] [note type (notes/cheatsheet)] (filepath)`
This command adds a file to the note system, filepath is optional, if not submitted a new file will be created in note_files under the name convention {course}::{name}.md.

### edit
Use this command to edit a note.
`pnotes edit [course] [name]`
Lets you edit an already existing note using your configured editor.

### create
Shortcut for add and edit at the same time.
`pnotes add [course] [name] [note type (notes/cheatsheet)]`

### list
List all existing notes.
No args required

### compile
Use this command to compile every existing notes into html.
No args required
This will compile every note in the note system into a static html format. Everything is automatically written in the html folder with 1 folder per course, each folder with its own index.html. Can be used to publish notes on a personal website.
