# YouTube Video Downloader Project

# import important files for the project
import pytubefix
from pytubefix import YouTube
import tkinter as tk
import customtkinter as ct
import os

# function defintion:
# download_video:
# takes in video url and a path to the location where the file should be saved
# if path or url is not valid: exception is thrown
def download_video(url, progress):
    url_str = url.get().strip()

    try:
        video = YouTube(url_str)
        stream = video.streams.first()
        
        print("Available streams:", stream)

        # Define the path to the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # download video
        y_title = video.title
        stream.download(output_path=downloads_folder, filename=f'{y_title}.mp4')
        progress.configure(text="Video downloaded", text_color="green")
    except Exception as e:
        print(e)
        progress.configure(text="Download error!", text_color="red")



# App setup
ct.set_appearance_mode("Light")
ct.set_default_color_theme("youtube_downloader/themes/cherry.json")
# theme from a13xe on GitHub

app = ct.CTk()
app.title("YouTube Downloader")
app.geometry("720x480")

# Screen elements
title = ct.CTkLabel(app, text="Insert YouTube link:")
title.pack(padx=10, pady=20)

# Take in input
url = tk.StringVar()
link  = ct.CTkEntry(app, width = 350, height=50, textvariable=url)
link.pack(pady=15)

# Download progress
finish = ct.CTkLabel(app, text= "")
finish.pack()


# Download
dw = ct.CTkButton(app, text="Download Video", command=lambda: 
                  download_video(url, finish))
dw.pack()

# Run app
app.mainloop()
