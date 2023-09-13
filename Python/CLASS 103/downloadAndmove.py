import time
import random
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="/Users/ysatish/Downloads"
destination="/Users/ysatish/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                fileName=os.path.basename(event.src_path)
                print("downloaded "+fileName)

                path1=source+"/"+fileName
                path2=destination+"/"+key
                path3=destination+"/"+key+"/"+fileName

                if os.path.exists(path2):
                    shutil.move(path1,path3)
                else: 
                    os.makedirs(path2)
                    shutil.move(path1,path3)


eventHandler=FileMovementHandler()

observer=Observer()
observer.schedule(eventHandler,destination,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()