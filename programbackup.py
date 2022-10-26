# NO DOCUMENTATION WOOHOO

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import datetime
import os
import shutil

window = tk.Tk()

lastPath = os.getcwd()
sourceDir = "Not selected"
toDir = "Not selected"
backupState = "No backups this session"

def fileBrowseSource():
    global sourceDir
    global lastPath
    sourceDir = filedialog.askdirectory(initialdir = lastPath, title="Select a source directory")
    if sourceDir == "":
        sourceDir = "Not selected"
    textFrom['text'] = sourceDir
    lastPath = sourceDir
      

def fileBrowseTo():
    global toDir
    global lastPath
    toDir = filedialog.askdirectory(initialdir = lastPath, title="Select a directory to backup to")
    if toDir == "":
        toDir = "Not selected"
    textTo['text'] = toDir
    lastPath = toDir
    
def backup():
    global sourceDir
    global toDir
    global backupState
    if (sourceDir != "Not selected") and (toDir != "Not selected"):
        currTime = datetime.datetime.now()
        dirName = ("Backup at " + currTime.strftime("%c")).replace(":", "-")
        path = toDir + "/" + dirName
        shutil.copytree(sourceDir, path)
        backupState = "Last backed up at " + currTime.strftime("%c")
        textBackup['text'] = backupState
    elif sourceDir == "Not selected":
        tk.messagebox.showerror(title="Error", message="Please select a source directory first.")
    elif toDir == "Not selected":
        tk.messagebox.showerror(title="Error", message="Please select a directory to back up to first.")
    else:
        tk.messagebox.showerror(title="Error", message="Unknown error. Oopsies!")

window.geometry("750x185")
window.title("Program Backup Tool")
window.iconbitmap("icon.ico")

title = tk.Label(text="Program backup tool", font=("Arial", 25))
subtitle = tk.Label(text="Made with pride by Osteofelidae", font=("Arial", 10))

browseSourceButton = ttk.Button(window, command=fileBrowseSource, text="Choose source directory", width = 30) 
browseToButton = ttk.Button(window, command=fileBrowseTo, text="Choose directory to backup to", width = 30)
backupButton = ttk.Button(window, command=backup, text="BACKUP", width = 30) 

title.place(x=10, y=0)
subtitle.place(x=10, y=40)

browseSourceButton.place(x=10, y=80)

textFrom = tk.Label(text=sourceDir, font=("Arial", 10))
textFrom.place(x=210, y=82)

browseToButton.place(x=10, y=110)

textTo = tk.Label(text=toDir, font=("Arial", 10))
textTo.place(x=210, y=112)

backupButton.place(x=10, y=150)

textBackup = tk.Label(text=backupState, font=("Arial", 10))
textBackup.place(x=210, y=152)

window.mainloop()