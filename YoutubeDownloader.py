from tkinter import*
from tkinter import filedialog
from moviepy import*
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil 

#Functions
def select_path():
    #allows user to select a path from explorer
    path = filedialog.askdirectory()
    path_label.configure(text = path)

def download_file():
    #pass keyword can be used to handle error of empty function
    #this function gets user path
    get_link = link_field.get()
    #get path userselected
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    ##move file to selected directory 
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download another file..')




screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen , width = 500, height = 500)
canvas.pack()

#image logo 
logo_img = PhotoImage(file = 'youtubeLogo.svg')
#resize image 
logo_img = logo_img.subsample(7,7)

canvas.create_image(250,120,image = logo_img)

##link field 
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter download link", font = ('Arial', 15))

# Select Path for saving file 
path_label = Label(screen, text = "Select Path for Download", font = ('Arial', 15))
select_btn = Button (screen, text = "Select", command = select_path )

#Add widgets to window
canvas.create_window(250,220, window = link_label)
canvas.create_window(250,270, window = link_field )

#Add select field widgets to window
canvas.create_window(250, 320, window = path_label)
canvas.create_window(250, 360, window = select_btn)

#Download button
download_btn = Button(screen, text = "Download File", command=download_file)
#Add download button to canvas
canvas.create_window(250, 420, window = download_btn )



screen.mainloop()