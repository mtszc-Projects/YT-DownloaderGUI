import customtkinter as ctk
import tkinter as tk
from PIL import Image


class Downloader:
    def __init__(self, window):
        window.title("YT Downloader")
        window.resizable(width=False, height=False)
        self.my_label = ctk.CTkLabel(window, text="Supported platforms:", font=("Arial", 32, "bold"))
        self.my_label.grid(row=0, columnspan=5)
        self.canvas = ctk.CTkCanvas(window, width=512, height=512, background="#202020")
        # self.yt_image = ctk.CTkImage(light_image=Image.open("./logos/youtube.png"),
        #                              dark_image=Image.open("./logos/youtube.png"),
        #                              size=(360, 360))
        self.yt_image = tk.PhotoImage(file="./logos/youtube.png")
        self.canvas.create_image(256, 256, image=self.yt_image)
        self.canvas.grid(row=1)
        # self.logos_frame = ctk.CTkFrame
        # self.button = ctk.CTkButton(window, image=self.yt_image, text="")
        # self.button.grid(row=1)
        self.entry_value = ctk.StringVar(window, value="")
        self.link_entry = ctk.CTkEntry(window, width=1000, textvariable=self.entry_value)
        self.link_entry.grid(row=2, columnspan=5)


wnd = ctk.CTk()
downloader = Downloader(wnd)
wnd.mainloop()
