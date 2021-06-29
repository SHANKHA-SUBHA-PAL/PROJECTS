import os 
import shutil
import time

path = 'c:/Users/SUBHANKAR PAL/OneDrive/Desktop/Python'

sec = time.time()

pathExists=os.path.exists(path)

files=os.walk(path,topdown=True)
print(files)

joining = os.path.join(path,'/Projects')
print(joining)

name = 
days = 30
# path =  "C:\Users\admin\Videos "
seconds = time.time()

if os.path.exists(path+'/'+ext):
        os.walk(path)
        #This will go through each and every fille
        for file in list_of_files:
        name, ext = os.path.splitext(file)
        os.path.join()

        #This is going to store extension type
        ext = ext[1:]
        if days > 30:
             os.remove(path)

        else:
          
            print("Not found")
            break


#This will create a properly organized list 

list_of_files = os.listdir(path)

