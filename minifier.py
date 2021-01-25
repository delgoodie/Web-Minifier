import os
import requests
import re
import shutil
import stat
from pathlib import Path
import sys


minPath = str(os.path.join(Path.home(), "Downloads\\"))
websitePath = sys.argv[1]

if(websitePath[-1] != "\\"):
    websitePath += "\\"

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)   
    
def resetFolder():
    try:
        rmtree(minPath + "Website")
    except OSError as e:
        0

    shutil.copytree(websitePath, minPath + "Website")

    for dirPath, dirName, files in os.walk(minPath + "Website"):
        if(".git" in dirPath):
            rmtree(dirPath)
            continue
        for filename in files:
            if ".js" in filename or ".css" in filename or "index.html" in filename or "README.md" in files:
                os.remove(dirPath + "/" + filename)
        try:
            os.removedirs(dirPath)
        except OSError as e:
            0

def minFile(path):
    ext = path[path.index(".") : len(path)]
    if ext == ".js":
        return requests.post("https://javascript-minifier.com/raw", data={'input': open(path).read()}).text
    elif ext == ".css":
        return open(path).read().replace("\n", "").replace("    ", " ")

def Minify():
    resetFolder()
    js = ""
    css = ""
    min = open(minPath + "Website/index.html", "w+")
    min.truncate(0)
    html = open(websitePath + "index.html")
    html = html.readlines()
    i = 0
    while i < len(html):
        if re.search(r"<script src='[^(http)]", html[i]):
            fileName = re.search(r"(?<=src=').+\.js", html[i]).group(0)
            js += minFile(websitePath + fileName)  
        elif re.search(r"<link rel='stylesheet' href='[^(http)]", html[i]):
            fileName = re.search(r"(?<=href=').+\.css", html[i]).group(0)
            css += minFile(websitePath + fileName)
        elif re.search(r"</(head)|(body)>", html[i]):
            if css != "":
                min.write("<style>")
                min.write(css)
                min.write("</style>")
                css = ""
            if js != "":
                min.write("<script>")
                min.write(js)
                min.write("</script>")
                js = ""
            min.write(html[i])
        else:
            if re.search(r"\w", html[i]):
                min.write(html[i])
        i += 1
    min.close()

Minify()

os.system("START chrome " + minPath + "Website/index.html || START " + minPath + "Website/index.html")