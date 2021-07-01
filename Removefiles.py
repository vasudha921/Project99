import os
import shutil
import time

path = input("Enter your path")
day = 30


#time.time() returns current time in seconds
seconds = time.time() - (day * 24 * 3600)

if os.path.exists(path):
    path2 = os.walk(path)

    for root_folders,folders,files in path2:
        folder_path = os.path.join(root_folders,folders,files)
    
        ctime = os.stat(folder_path).st_ctime
        if ctime >= seconds :
             os.remove(path)

        if not  os.path.exists(folder_path):
            print("path not found")