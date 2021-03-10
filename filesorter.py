#!/usr/bin/env python
import os
import shutil
path = "/home/wesley/Diskdrive/Downloads/"
names = os.listdir(path)
folder_name = ['image','text','archive','pdf','docx','ppt','pythonfiles','jar','documents']
for x in range(0,9):
    if not os.path. exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for files in names:
    if ".png" in files and not os.path.exists(path+'image'+files):
        shutil.move(path+files, path+'image/'+files)

    if ".jpg" in files and not os.path.exists(path+'image'+files):
        shutil.move(path+files, path+'image/'+files)

    if ".txt" in files and not os.path.exists(path+'text'+files):
        shutil.move(path+files, path+'text/'+files)

    if ".gz" in files and not os.path.exists(path+'archive'+files):
        shutil.move(path+files, path+'archive/'+files)

    if ".jpeg" in files and not os.path.exists(path+'image'+files):
        shutil.move(path+files, path+'image/'+files)
    
    if ".deb" in files and not os.path.exists(path+'archive'+files):
        shutil.move(path+files, path+'archive/'+files)
    
    if ".xz" in files and not os.path.exists(path+'archive'+files):
        shutil.move(path+files, path+'archive/'+files)

    if ".py" in files and not os.path.exists(path+'pythonfiles'+files):
        shutil.move(path + files, path+'pythonfiles/'+files)
    
    if ".pdf" in files and not os.path.exists(path+'pdf'+files):
        shutil.move(path+files, path+'pdf/'+files)

    if ".docx" in files and not os.path.exists(path+'documents'+files):
        shutil.move(path+files, path+'documents/'+files)

    if ".ppt" in files and not os.path.exists(path+'ppt'+files):
        shutil.move(path+files, path+'ppt/'+files)

    if ".jar" in files and not os.path.exists(path+'jar'+files):
        shutil.move(path+files, path+'jar/'+files)

    if ".zip" in files and not os.path.exists(path+'archive'+files):
        shutil.move(path+files, path+'archive/'+files)

    if ".bak" in files and not os.path.exists(path+'documents'+files):
        shutil.move(path+files, path+'documents/'+files)
# change the file directory "path"
