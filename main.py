import tkinter
from PIL import ImageTk
import threading
import download
import set_path


class GUI:
    def __init__(self, root=None):

        self.root = tkinter.Tk()
        self.root.title("Spotify Downloader")
        self.root.iconbitmap(default=r'img\spotify.ico')
        self.root.geometry("883x529")

        # BackGround
        self.bg = ImageTk.PhotoImage(file=r"img\bg.jpg")
        self.label = tkinter.Label(root, image=self.bg)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        #

        # entry

        self.entry = tkinter.Entry(root, width=40, font=('Gotham Book', 16))
        self.entry.place(x=178, y=265)
        #

        # download button
        self.dl_btn_img = tkinter.PhotoImage(file=r"img\download button.png")

        self.dl_btn_img_label = tkinter.Label(image=self.dl_btn_img)

        self.dl_btn = tkinter.Button(root, image=self.dl_btn_img, borderwidth=0, bg='black',
                                     activebackground='black', command=lambda: download.threads(self))
        self.dl_btn.place(x=347, y=365)
        #

        # path_button
        self.pth_btn_img = ImageTk.PhotoImage(file=r"img\path 4.jpg")

        self.pth_btn = tkinter.Button(root, image=self.pth_btn_img, borderwidth=0,
                                      bg='black', activebackground='black', command=set_path.get_path)
        self.pth_btn.place(x=670, y=265)

        self.root.resizable(False, False)
        self.root.mainloop()


if __name__ == "__main__":

    GUI()
