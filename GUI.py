
from tkinter import *
from Save import CreateFile
import tkinter.messagebox as mb
import os 
from os import path
from tkinter import filedialog as fd


def SaveNote(event):
    labelNote = noteName.get()
    textNote = text.get("1.0","end")
    check,filename = CreateFile(labelNote,textNote,True)
    if check == True:
        saved()
    elif check == False:
        answer = mb.askyesno(
        title="Ошибка", 
        message="Файл с таким именем уже существует. \n Заменить?")
        if answer == True:
            os.remove("notes/"+filename)
            CreateFile(labelNote,textNote,False)
            saved()
            
        else:
            noteName.delete(0,END)

def saved():
        mb.showerror("Информация","Данные успешно сохранены")
        noteName.delete(0,END)
        text.delete("1.0",END)
            

def ClickedCreateNewNote(event):
    noteName.grid(column=0,row=2)
    noteName.insert(0,"Note")
    text.grid(column=0,row=3)
    saveBtn.grid(column=0,row=4)
    deleteBtn.grid(column=0,row=5)

def ClickedDeleteBtn(event):
        filename = noteName.get()
        try:
            f = open("notes/"+filename+".json")
            ch = True
            f.close()
        except FileNotFoundError:
            ch = False
        if ch == True:
            answ = mb.askyesno(
            title="", 
            message="Удалить файл "+filename+".json? \n Изменить это действие будет невозможно.")
            if answ == True:
                os.remove("notes/"+filename+".json")
                noteName.delete(0,END)
                text.delete("1.0",END)
        else:
            answer = mb.askyesno(
            title="", 
            message="Изменения не были сохранены. Желаете очистить?")
            if answer == True:
                noteName.delete(0,END)
                text.delete("1.0",END)
                




def insert_text():
    file_name = fd.askopenfilename(defaultextension=".json",initialdir="notes/")
    full_name = path.basename(file_name)
    name = path.splitext(full_name)[0]
    
    f = open(file_name)
    noteName.grid(column=0,row=2)
    text.grid(column=0,row=3)
    saveBtn.grid(column=0,row=4)
    deleteBtn.grid(column=0,row=5)
    noteName.insert(0,name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

        

    

window = Tk()
window.title("Notes")
window.geometry('600x700')
newNote = Button(window,text ="Создать новую заметку",width=40)
newNote.grid(column=0, row=0)
saveBtn = Button(window,text ="Сохранить изменения",width=40,command=SaveNote)
savedNotes = Button(window,text="Открыть заметку",width=40,command=insert_text)
savedNotes.grid(column=0,row=1)
deleteBtn = Button(window,text = "Удалить заметку",width=40, command=ClickedDeleteBtn)
noteName = Entry(window,width=25)

text = Text(width=80, height=40)





deleteBtn.bind("<Button-1>",ClickedDeleteBtn)   
saveBtn.bind("<Button-1>",SaveNote)
newNote.bind("<Button-1>",ClickedCreateNewNote)



window.mainloop()
