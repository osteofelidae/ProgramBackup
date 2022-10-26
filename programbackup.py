# Imports needed modules
import tkinter as tk
from tkinter import filedialog
import datetime
import os
import shutil
import webbrowser

# Initial states of display variables
lastPath = os.getcwd()
sourceDir = "Not selected"
toDir = "Not selected"
backupState = "No backups this session"

# Constant definitions
LEFTX = 10
RIGHTX = 214
TEXTCOLOR = "#FFFFFF"
BGCOLOR = "#111111"
BUTTONBGCOLOR = "#333333"
APPICON = "assets/icon.ico"
MYICON = "assets/osteofelidae.png"
FONT = "Bahnschrift"

# Actions to be executed when 'browse for source' button is clicked
def fileBrowseSource():
    global sourceDir
    global lastPath
    sourceDir = filedialog.askdirectory(initialdir = lastPath, title="Select a source directory")
    if sourceDir == "":
        sourceDir = "Not selected"
    textFrom['text'] = sourceDir
    lastPath = sourceDir
      
# Actions to be executed when 'browse for dest' button is clicked
def fileBrowseTo():
    global toDir
    global lastPath
    toDir = filedialog.askdirectory(initialdir = lastPath, title="Select a directory to backup to")
    if toDir == "":
        toDir = "Not selected"
    textTo['text'] = toDir
    lastPath = toDir
    
# Actions to be executed when 'backup' button is clicked
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
        
# Actions to be executed when my icon is pressed
def openGithub():
    webbrowser.open('osteofelidae.github.io')

# Window for application
window = tk.Tk()
window.geometry("750x185")
window.title("Program Backup Tool")
window.iconbitmap(APPICON)
window.configure(bg=BGCOLOR)

# Title
title = tk.Label(text="Program backup tool", font=(FONT, 25), bg=BGCOLOR, fg=TEXTCOLOR )
title.place(x=LEFTX, y=0)

# Subtitle button
MYICONIMAGE = tk.PhotoImage(file=MYICON)
subtitleButton = tk.Button(window, command=openGithub, image=MYICONIMAGE, width = 25)
subtitleButton.place(x=LEFTX, y=43)
SUBTITLEBUTTONSTYLE = {"borderwidth": "0", "bg": BGCOLOR, "activebackground": BGCOLOR}
subtitleButton.configure(**SUBTITLEBUTTONSTYLE)


# Subtitle
subtitle = tk.Label(text="Made with pride by Osteofelidae", font=(FONT, 10), bg=BGCOLOR, fg=TEXTCOLOR)
subtitle.place(x=LEFTX + 30, y=45)

# 'Browse for source' button
browseSourceButton = tk.Button(window, command=fileBrowseSource, text="Choose source directory", width = 27) 
browseSourceButton.place(x=LEFTX, y=80)
BROWSESOURCEBUTTONSTYLE = {"borderwidth": "0", "fg":TEXTCOLOR, "bg": BUTTONBGCOLOR, "activebackground": "#261161", 'activeforeground':TEXTCOLOR}
browseSourceButton.configure(**BROWSESOURCEBUTTONSTYLE)

# Text displaying source directory
textFrom = tk.Label(text=sourceDir, font=(FONT, 10), bg=BGCOLOR, fg=TEXTCOLOR)
textFrom.place(x=RIGHTX, y=80)

# 'Browse for dest' button
browseToButton = tk.Button(window, command=fileBrowseTo, text="Choose directory to backup to", width = 27)
browseToButton.place(x=LEFTX, y=110)
BROWSETOBUTTONSTYLE = {"borderwidth": "0", "fg":TEXTCOLOR, "bg": BUTTONBGCOLOR, "activebackground": "#3F0071", 'activeforeground':TEXTCOLOR}
browseToButton.configure(**BROWSETOBUTTONSTYLE)

# Text displaying dest directory
textTo = tk.Label(text=toDir, font=(FONT, 10), bg=BGCOLOR, fg=TEXTCOLOR)
textTo.place(x=RIGHTX, y=110)

# 'Backup' button
backupButton = tk.Button(window, command=backup, text="BACKUP", width = 27) 
backupButton.place(x=LEFTX, y=150)
BACKUPBUTTONSTYLE = {"borderwidth": "0", "fg":TEXTCOLOR, "bg": BUTTONBGCOLOR, "activebackground": "#FB2576", 'activeforeground':TEXTCOLOR}
backupButton.configure(**BACKUPBUTTONSTYLE)

# Text displaying last backup time
textBackup = tk.Label(text=backupState, font=(FONT, 10), bg=BGCOLOR, fg=TEXTCOLOR)
textBackup.place(x=RIGHTX, y=150)

# Run UI loop
window.mainloop()