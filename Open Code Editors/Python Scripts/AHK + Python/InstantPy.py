import os
from datetime import datetime

def CreateNewFile():
    C_Time = datetime.now().strftime('%d-%b-%y_%H-%M')
    Folder_Path = 'D:\\Other\\Projects\\Python\\Instant'

    if not (os.path.exists(Folder_Path)):
        os.mkdir(Folder_Path)

    os.system(f'code {Folder_Path}\\{C_Time}.py')
    
CreateNewFile()