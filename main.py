from tkinter import *
from PIL import ImageTk
from tkinter import filedialog
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL


def download(link, dir):
    dir = dir.replace('/', '\\')
    path = dir+'\\'

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {'format': 'bestaudio',

                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],

                'progress_hooks': [my_hook],
                'outtmpl': path+'%(title)s.%(ext)s',
                }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def youtube(title, path):
    url = f"https://www.youtube.com/results?q={title}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        raise Exception("No Video Found for this Topic!")

    download(f"https://www.youtube.com{lst[count - 5]}", path)


def spotify(link, path):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, "html.parser")

    spotify_song_name = soup.title.get_text()

    spotify_song_name = spotify_song_name.replace(" song by", "")
    spotify_song_name = spotify_song_name.replace(" | Spotify", "")

    youtube(spotify_song_name, path)


def get_path():  # Gets the download location(path)
    path = filedialog.askdirectory()
    f = open(r"path\path.txt", "w")
    f.write(path)
    f.close()


def get_link():  # Gets the spotify link from the entry widget
    f = open(r"path\path.txt", "r")
    path = f.read()

    if path == '': #checks if path exists 
        f.close()
        get_path()

        f = open(r"path\path.txt", "r")
        path = f.read()
        f.close()
    else:
        f.close()

    link = entry.get()

    if link == '': # checks if links present
        messagebox.showinfo("", "Enter a link!")
    else:
        print(link)
        print(path)
        spotify(link, path)


root = Tk()
root.title("Spotify Downloader")
root.iconbitmap(default=r'img\spotify.ico')
root.geometry("883x529")

# BackGround
bg = ImageTk.PhotoImage(file=r"img\bg.jpg")
label = Label(root, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)
#

# entry
entry = Entry(root, width=32, font=('Gotham Book', 16))
entry.place(x=178, y=265)
#


# download button
dl_btn_img = PhotoImage(
    file=r"img\download button.png")

dl_btn_img_label = Label(image=dl_btn_img)


dl_btn = Button(root, image=dl_btn_img,
                borderwidth=0, bg='black', activebackground='black', command=get_link)
dl_btn.place(x=347, y=365)
#

# path_button
pth_btn_img = ImageTk.PhotoImage(
    file=r"img\path 4.jpg")

pth_btn = Button(root, image=pth_btn_img, borderwidth=0,
                 bg='black', activebackground='black', command=get_path)
pth_btn.place(x=670, y=265)


root.resizable(False, False)
root.mainloop()
