import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
from tkinter import messagebox
import set_path
import threading


def download_track(link, dir):  # downloads the track
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
    messagebox.showinfo("", "Download complete!")


def youtube(title, path):  # get's the YT video link
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
    download_track(f"https://www.youtube.com{lst[count - 5]}", path)
    


def spotify(link, path):  # get song's name by scrapping spotify
    url = requests.get(link)
    soup = BeautifulSoup(url.content, "html.parser")

    spotify_song_name = soup.title.get_text()

    spotify_song_name = spotify_song_name.replace(" song by", "")
    spotify_song_name = spotify_song_name.replace(" | Spotify", "")
    youtube(spotify_song_name, path)


def get_link(gui):  # Gets the spotify link
    f = open(r"path\path.txt", "r")
    path = f.read()

    if path == '':  # checks if path exists
        f.close()
        set_path.get_path()

        f = open(r"path\path.txt", "r")
        path = f.read()
        f.close()
    else:
        f.close()

    link = gui.entry.get()  # gets spotify link from the entry widget

    if link == '':  # checks if links present
        messagebox.showinfo("Alert", "Enter a link!")
    else:
        print(link)
        print(path)
        threading.Thread(target=spotify, args=[link, path]).start()
