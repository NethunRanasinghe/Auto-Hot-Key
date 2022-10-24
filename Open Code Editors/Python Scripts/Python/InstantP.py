import os
from datetime import datetime
from pynput.keyboard import Key, Listener

comb = []
enb = 0

def CreateNewFileVSC(Type):
    if(Type == 1):
        ext = 'py'
    elif(Type == 2):
        ext = 'c'

    C_Time = datetime.now().strftime('%d-%b-%y_%H-%M')
    Folder_Path = 'D:\\Other\\Projects\\Python\\Instant'

    if not (os.path.exists(Folder_Path)):
        os.mkdir(Folder_Path)

    os.system(f'code {Folder_Path}\\{C_Time}.{ext}')

def IntelliJNewProj():
    C_Time = datetime.now().strftime('%d-%m-%Y')
    Save_Folder_Path = f'D:\\NSBM\\Year 2\\Sem -01\\JAVA\\{C_Time}'
    
    if not (os.path.exists(Save_Folder_Path)):
        try:
            os.mkdir(Save_Folder_Path)
        except:
            pass
    
    if(os.path.exists(Save_Folder_Path)):
        os.system('idea64')


def on_press(key):
    global enb

    try:
        if(key == key.delete):
            comb.clear()
            enb = 1
    except:
        comb.clear()
    
    if(enb == 1):
        comb.append(key)
        
        if(len(comb) >= 3):
            if(comb[0] == Key.delete and comb[1] == Key.insert and comb[2] == Key.end):
                CreateNewFileVSC(1)
                comb.clear()
                enb = 0

            elif(comb[0] == Key.delete and comb[1] == Key.insert and comb[2] == Key.down):
                CreateNewFileVSC(2)
                comb.clear()
                enb = 0

            elif(comb[0] == Key.delete and comb[1] == Key.insert and comb[2] == Key.page_down):
                IntelliJNewProj()
                comb.clear()
                enb = 0

# Creating listner and joining it to the main thread
with Listener(on_press=on_press) as listener:
    listener.join()