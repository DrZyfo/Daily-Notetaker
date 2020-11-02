from datetime import date
import time, sys

def notesaver():
    while True:
        today_day = str(date.today())
        datetxt = today_day + '.txt'
        file = open(datetxt, "a+")
        file.close() 
        file = open(datetxt, "r")
        filecontent = file.read()
        print(filecontent)
        file.close()
        file = open(datetxt, "a")
        file.write("\n")
        tdynote = input('note; ')
        if tdynote == 'exit':
            sys.exit()
            break
        else:   
            file.write(tdynote)
   
        




if __name__ == '__main__':
    notesaver()



