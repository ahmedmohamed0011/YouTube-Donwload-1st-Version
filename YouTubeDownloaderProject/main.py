import os
import threading
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from tkinter import filedialog
from pytube import YouTube
from pytube import *
from pydub import AudioSegment

root = Tk()
root.title("YouTube Downloader")
root.geometry("550x360")
root.resizable(False, False)

# Functions
def broswe():
    dirctory = filedialog.askdirectory(title="Save Video")
    savePathEntry.delete(0, "end")
    savePathEntry.insert(0, dirctory)

def ytDownloadmp4():
    status.config(text="Status: Downloading....")
    link = linkEntry.get()
    folder = savePathEntry.get()
    YouTube(link, on_complete_callback=finish).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)

def ytDownloadmp3():
    status.config(text="Status: Downloading....")
    link = linkEntry.get()
    folder = savePathEntry.get()
    YouTube(link, on_complete_callback=finish).streams.filter(only_audio='True').first().download(folder)
    

def finish(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status: Download Finished.!", bg="green")
    messagebox.showinfo("Thanks", "Thank You For Using My App❤️..!")
    clear()

def start_download_thread_mp4():
    threading.Thread(target=ytDownloadmp4).start()

def start_download_thread_mp3():
    threading.Thread(target=ytDownloadmp3).start()

def clear ():
    link = linkEntry.delete(0, "end")
    path = savePathEntry.delete(0, "end")
    status.config(text="Status: Ready.!", bg="white")

def clearButton ():
    link = linkEntry.delete(0, "end")
    path = savePathEntry.delete(0, "end")
    status.config(text="Status: Ready.!", bg="white")
    messagebox.showinfo("Clear Info", "Clear Is Finished..!")

def on_closing():
    # Show information window
    if messagebox.askokcancel("Quit", "This Program Developed By : Ahmed Mohamed ! \n To Support Me... \n InstaPay User : ahmed.mohamed5050@instapay \n Do You Want Quit ?"):
        root.destroy()

# GUI Section 

# Youtube Logo
photoLink = PhotoImage(file="YouTube-logo.png").subsample(30)
youtubeLogo = ttk.Label(root, image=photoLink)
youtubeLogo.place(relx=0.5, rely=0.25, anchor="center")

# Youtube link
linkLabel = ttk.Label(root, text="YouTube Link :")
linkLabel.place(x=25, y=180)

linkEntry = ttk.Entry(root, width=60)
linkEntry.place(x=140, y=180)

# Folder Save Browse
savePathLabel = ttk.Label(root, text="Save Folder :")
savePathLabel.place(x=25, y=225)

savePathEntry = ttk.Entry(root, width = 45)
savePathEntry.place(x=140, y=225)

browseButton = ttk.Button(root, text="Browse", command=broswe)
browseButton.place(x=440 ,y=225)

# Download Button
# Mp4 Button
downloadButton = ttk.Button(root, text="Download Mp4!", width=25, command=start_download_thread_mp4)
downloadButton.place(relx=0.7, rely=0.79, anchor="center")

# Mp3 Button
downloadButton = ttk.Button(root, text="Download Mp3!", width=25, command=start_download_thread_mp3)
downloadButton.place(relx=0.3, rely=0.79, anchor="center")

# Clear Button 
clearButton = ttk.Button(root, text="Clear", command=clearButton)
clearButton.place(rely=0.85, relx=0.8)

# Status bar
status = Label(root, text="Status: Ready", font="Calibre 10 italic", fg="black", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
