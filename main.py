from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

root = Tk()

# Create menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a submenu

submenu= Menu(menubar, tearoff=0)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build by Shouvick')
submenu= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us",command=about_us)


mixer.init()    #initializing the mixer

root.geometry('300x300')

root.title('Melody')
# root.iconbitmap(r'melody.ico')

text = Label(root,text="Let's make some noise!")
text.pack()

def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
    except:
        tkinter.messagebox.showerror('Error', 'File not found. Please check again.')

def stop_music():
    mixer.music.stop()

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

play_photo = PhotoImage(file="arrows.png")
play_btn = Button(root, image=play_photo,command=play_music)
play_btn.pack()

stop_photo = PhotoImage(file="stop.png")
stop_btn = Button(root, image=stop_photo,command=stop_music)
stop_btn.pack()

scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(50)
mixer.music.set_volume(0.5)

scale.pack()

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN)
statusbar.pack(side=BOTTOM,fill=X)



root.mainloop()




