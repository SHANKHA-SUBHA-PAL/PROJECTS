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