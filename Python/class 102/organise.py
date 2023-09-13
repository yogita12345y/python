import os
import shutil

source="/Users/ysatish/Downloads"
destination="/Users/ysatish/Downloads"
files=os.listdir(source)

for i in files:
    name,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in [".docs",".txt",".doc",".pdf",".csv"]:
        path1=source+"/"+i
        path2=destination+"/documents"
        path3=destination+"/documents/"+i

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)