
def CreateFile(label,text):
        note = open(label+".json","w+")
        note.write(text)
        note.close()

