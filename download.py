import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
from tkinter import messagebox
import set_path
import threading
import tkinter
from tkinter import ttk, Label


def download_track(link, dir):  # downloads the track

    try:
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

    except:
        messagebox.showerror("", "Error, Download Incomplete!")


def youtube(title, path):  # get's the YT video link

    try:

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

    except:
        messagebox.showerror("", "Error, Download Incomplete!")


def spotify(link, path):  # get song's name by scrapping spotify

    try:
        url = requests.get(link)
        soup = BeautifulSoup(url.content, "html.parser")

        spotify_song_name = soup.title.get_text()

        spotify_song_name = spotify_song_name.replace(" song by", "")
        spotify_song_name = spotify_song_name.replace(" | Spotify", "")
        youtube(spotify_song_name, path)
    except:
        messagebox.showerror("", "Error, Download Incomplete!")


def get_link(gui):  # Gets the spotify link

    try:
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
            spotify(link, path)
    except:
        messagebox.showerror("", "Error, Download Incomplete!")


def threads(gui):

    gui.dl_btn['state'] = 'disabled'    # disable download button
    t = threading.Thread(target=get_link, args=[gui])
    t.start()

    def check_schedule(t, gui):
        gui.root.after(1000, check_if_done, t, gui)

    def check_if_done(t, gui):
        # If the thread has finished, re-enable the button and show a message.
        if not t.is_alive():

            dl_popup.destroy()  # close the popup window
            dl_popup.update()

            # enable download button after download complete
            gui.dl_btn['state'] = 'normal'
            messagebox.showinfo("", "Download complete!")
        else:
            # Otherwise check again after one second.
            check_schedule(t, gui)

    # download progress window(popup)
    dl_popup = tkinter.Toplevel(gui.root)

    # align popup to the center of the  root window

    root_x = gui.root.winfo_rootx()  # get main window position
    root_y = gui.root.winfo_rooty()

    dl_popup_x = root_x + 330  # add offset to this position
    dl_popup_y = root_y + 220
    dl_popup.geometry(f'+{dl_popup_x}+{dl_popup_y}')

    dl_popup.attributes('-topmost', 'true')
    # dl_popup.overrideredirect(True) #remove title bar

    label = Label(dl_popup, text="Downloading...")
    label.pack()

    pb = ttk.Progressbar(dl_popup, orient="horizontal",
                         length=200, mode="indeterminate")
    pb.pack()
    pb.start(10)

    check_if_done(t, gui)

    dl_popup.mainloop()
