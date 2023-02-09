from tkinter import *
from Save import CreateFile

window = Tk()
window.title("Notes")
window.geometry('600x700')
newNote = Button(window,text ="Создать новую заметку",width=40)
newNote.grid(column=0, row=0)
saveBtn = Button(window,text ="Сохранить изменения",width=40)
savedNotes = Button(window,text="Открыть заметку",width=40)
savedNotes.grid(column=0,row=1)
noteName = Entry(window,width=25)

text = Text(width=80, height=40)

# notes = ["gfgh","sdfgt","jhgfd","jhgfds","uytr"]
# notes_var = Variable(value=notes)
# notesListBox = Listbox(listvariable=notes_var)
# notesListBox.grid(column=0,row=2)



def ClickedCreateNewNote(event):
    noteName.grid(column=0,row=2)
    noteName.insert(0,"Note 1")
    text.grid(column=0,row=3)
    saveBtn.grid(column=0,row=4)

def SaveNote(event):
    labelNote = noteName.get()
    textNote = text.get("1.0","end")
    CreateFile(labelNote,textNote)



    
saveBtn.bind("<Button-1>",SaveNote)
newNote.bind("<Button-1>",ClickedCreateNewNote)



window.mainloop()
