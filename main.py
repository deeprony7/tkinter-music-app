from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
import os

root = Tk()

# Create menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a submenu

submenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo(
        'About Melody', 'This is a music player built by Shouvick')


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command=about_us)


mixer.init()  # initializing the mixer

# root.geometry('300x300')

root.title('Melody')
# root.iconbitmap(r'images/melody.ico')

filelabel = Label(root, text="Let's make some noise!")
filelabel.pack(pady=10)

lengthlabel = Label(root, text='Duration : --:--')
lengthlabel.pack()


def show_details():
    filelabel['text'] = "Playing " + os.path.basename(filename)

    file_data = os.path.splitext(filename)

    if file_data[-1] == '.mp3':
        audio = MP3(filename)
        duration = audio.info.length
    else:
        a = mixer.Sound(filename)
        duration = a.get_length()

    # div - duration/60, mod - duration % 60
    mins, secs = divmod(duration, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Duration : " + timeformat
    


def play_music():
    global paused
    
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music resumed"
        paused = FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing - " + os.path.basename(filename)
            show_details()
        except:
            tkinter.messagebox.showerror(
                'Error', 'File not found. Please check again.')

paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music paused"

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music stopped"


def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)  # set_volume takes only values between 0 and 1

def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded"

muted = FALSE

def mute_music():
    global muted
    global last_volume

    if muted:
        mixer.music.set_volume(last_volume*0.01)
        volume_btn.configure(image=volume_photo)
        scale.set(last_volume)
        muted= FALSE
    else:
        mixer.music.set_volume(0)
        volume_btn.configure(image=mute_photo)
        last_volume = scale.get()
        print(last_volume)
        scale.set(0)
        muted = TRUE

middleframe= Frame(root)
middleframe.pack(padx=30,pady=30)

play_photo = PhotoImage(file="images/arrows.png")
play_btn = Button(middleframe, image=play_photo, command=play_music)
play_btn.grid(row=0,column=0,padx=10)


pause_photo = PhotoImage(file="images/pause.png")
pause_btn = Button(middleframe, image=pause_photo, command=pause_music)
pause_btn.grid(row=0,column=1,padx=10)

stop_photo = PhotoImage(file="images/stop.png")
stop_btn = Button(middleframe, image=stop_photo, command=stop_music)
stop_btn.grid(row=0,column=2,padx=10)

# Bottomframe for volume, rewind, mute, etc

bottomframe = Frame(root)
bottomframe.pack()


rewind_photo = PhotoImage(file="images/rewind.png")
rewind_btn = Button(bottomframe, image=rewind_photo, command=rewind_music)
rewind_btn.grid(row=0,column=0)

mute_photo = PhotoImage(file="images/mute.png")
volume_photo = PhotoImage(file="images/volume.png")
volume_btn = Button(bottomframe, image=volume_photo, command=mute_music)
volume_btn.grid(row=0,column=1)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)   # default scale value (only sets the slider)
mixer.music.set_volume(0.5) # actually sets the volume
scale.grid(row=0,column=2,padx=30,pady=15)

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)


root.mainloop()

