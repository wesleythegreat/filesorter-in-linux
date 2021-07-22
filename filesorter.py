#!/usr/bin/env python
import os
import shutil
import time
while True:
        time.sleep(2)
        path = "/home/wesley/Diskdrive/Downloads/"
        names = os.listdir(path)
        folder_name = ['image', 'text', 'archive', 'pdf', 'ppt', 'pythonfiles', 'jar', 'documents', 'iso', 'torrent',
                       'music', 'html', 'codefile', 'docsave', 'video']
        for x in range(0, 15):
            if not os.path.exists(path + folder_name[x]):
                os.makedirs(path + folder_name[x])
        for files in names:
            if ".png" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".jpg" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".txt" in files and not os.path.exists(path + 'text' + files):
                shutil.move(path + files, path + 'text/' + files)

            if ".gz" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".jpeg" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".deb" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".xz" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".py" in files and not os.path.exists(path + 'pythonfiles' + files):
                shutil.move(path + files, path + 'pythonfiles/' + files)

            if ".pdf" in files and not os.path.exists(path + 'pdf' + files):
                shutil.move(path + files, path + 'pdf/' + files)

            if ".docx" in files and not os.path.exists(path + 'documents' + files):
                shutil.move(path + files, path + 'documents/' + files)

            if ".ppt" in files and not os.path.exists(path + 'ppt' + files):
                shutil.move(path + files, path + 'ppt/' + files)

            if ".jar" in files and not os.path.exists(path + 'jar' + files):
                shutil.move(path + files, path + 'jar/' + files)

            if ".zip" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".bak" in files and not os.path.exists(path + 'documents' + files):
                shutil.move(path + files, path + 'documents/' + files)

            if ".svg" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".iso" in files and not os.path.exists(path + 'iso' + files):
                shutil.move(path + files, path + 'iso/' + files)

            if ".torrent" in files and not os.path.exists(path + 'torrent' + files):
                shutil.move(path + files, path + 'torrent/' + files)

            if ".mp3" in files and not os.path.exists(path + 'music' + files):
                shutil.move(path + files, path + 'music/' + files)

            if ".html" in files and not os.path.exists(path + 'html' + files):
                shutil.move(path + files, path + 'html/' + files)

            if ".ico" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".gif" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".deb" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".img" in files and not os.path.exists(path + 'iso' + files):
                shutil.move(path + files, path + 'iso/' + files)

            if ".rar" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".json" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".xml" in files and not os.path.exists(path + 'html' + files):
                shutil.move(path + files, path + 'html/' + files)

            if ".psd" in files and not os.path.exists(path + 'docsave' + files):
                shutil.move(path + files, path + 'docsave/' + files)

            if ".sh" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".tar" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".zst" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".xcf" in files and not os.path.exists(path + 'docsave' + files):
                shutil.move(path + files, path + 'docsave/' + files)

            if ".mp4" in files and not os.path.exists(path + 'video' + files):
                shutil.move(path + files, path + 'video/' + files)

            if ".abr" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".exe" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".7z" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".AppImage" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".kdenlive" in files and not os.path.exists(path + 'docsave' + files):
                shutil.move(path + files, path + 'docsave/' + files)

            if ".bat" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".bmp" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".m4a" in files and not os.path.exists(path + 'music' + files):
                shutil.move(path + files, path + 'music/' + files)

            if ".mpeg" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".pst" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".bin" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".cpp" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".gif" in files and not os.path.exists(path + 'image' + files):
                shutil.move(path + files, path + 'image/' + files)

            if ".php" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".rpm" in files and not os.path.exists(path + 'codefile' + files):
                shutil.move(path + files, path + 'codefile/' + files)

            if ".tar.gz" in files and not os.path.exists(path + 'archive' + files):
                shutil.move(path + files, path + 'archive/' + files)

            if ".wav" in files and not os.path.exists(path + 'music' + files):
                shutil.move(path + files, path + 'music/' + files)

            if ".xcf.gz" in files and not os.path.exists(path + 'docsave' + files):
                shutil.move(path + files, path + 'docsave/' + files)
            if ".mkv" in files and not os.path.exists(path + 'video' + files):
                shutil.move(path +files, path + 'video/' + files)
        print("Done")
