import datetime
def CreateFile(label,text,checkDate):
        try:
            filename = label+".json"
            note = open("notes/"+filename,"x")
            date = Time()
            if checkDate:
                note.write(date + "\n")
            note.write(text)
            note.close()
            return True,filename
        except FileExistsError:
            return False,filename

def Time():
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y %H:%M")
    return date