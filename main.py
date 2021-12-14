import tkinter
from PIL import ImageTk
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

        GUI.center(self.root)

        # entry

        self.entry = tkinter.Entry(root, font=('Gotham Book', 16))
        self.entry.place(relwidth=0.55, x=178, y=265)
        #

        # right  click menu
        GUI.make_menu(root)
        self.entry.bind_class(
            "Entry", "<Button-3>", GUI.show_menu)

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

    def make_menu(w):
        global the_menu
        the_menu = tkinter.Menu(w, tearoff=0)
        the_menu.add_command(label="Cut")
        the_menu.add_command(label="Copy")
        the_menu.add_command(label="Paste")

    def show_menu(e):
        w = e.widget
        the_menu.entryconfigure("Cut",
                                command=lambda: w.event_generate("<<Cut>>"))
        the_menu.entryconfigure("Copy",
                                command=lambda: w.event_generate("<<Copy>>"))
        the_menu.entryconfigure("Paste",
                                command=lambda: w.event_generate("<<Paste>>"))
        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()


if __name__ == "__main__":

    GUI()
