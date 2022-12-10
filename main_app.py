import customtkinter as ctk
from tkinter import filedialog
from pytube import Playlist
from PIL import Image


class Downloader:
    def download_playlist(self):
        yt_playlist = Playlist(str(self.link.get()))
        path = str(self.download_path.get())
        counter = 1
        for video in yt_playlist.videos:
            file_name = self.prepare_name_for_playlist(counter, video.title)
            video.streams.get_highest_resolution().download(output_path=path, filename=file_name)
            print("Downloaded: ", file_name)
            counter = counter + 1
        print("\nAll videos have been downloaded.")

    @staticmethod
    def prepare_name_for_playlist(counter, name):
        return "0" + str(counter) + " " + name + ".mp4" if counter < 10 else str(counter) + " " + name + ".mp4"

    @staticmethod
    def file_system_explorer():
        wnd.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                  filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))

    def __init__(self, window):
        window.title("YT Downloader")
        window.resizable(width=False, height=False)
        self.my_label = ctk.CTkLabel(window, height=60, text_color="black",
                                     text="Source platform",
                                     font=("Arial", 32, "bold"))
        self.my_label.grid(row=1, columnspan=7)
        # TODO: PLATFORM CHOICE
        # YT BUTTON
        self.resized_yt_image = ctk.CTkImage(light_image=Image.open("./logos/youtube.png").resize((192, 192)),
                                             dark_image=Image.open("./logos/youtube.png").resize((192, 192)),
                                             size=(192, 192))
        self.yt_button = ctk.CTkButton(window, image=self.resized_yt_image, height=192, width=192, text="",
                                       fg_color="#242424", bg_color="#242424", hover_color="#FF0000")
        self.yt_button.grid(row=2, column=1, columnspan=2)
        # BC BUTTON
        self.resized_bc_image = ctk.CTkImage(light_image=Image.open("./logos/bandcamp.png").resize((192, 192)),
                                             dark_image=Image.open("./logos/bandcamp.png").resize((192, 192)),
                                             size=(192, 192))
        self.bc_button = ctk.CTkButton(window, image=self.resized_bc_image, height=192, width=192, text="",
                                       fg_color="#242424", bg_color="#242424", hover_color="#629aa9")
        self.bc_button.grid(row=2, column=4, columnspan=2)
        # TODO: FORMAT CHOICE
        self.format_label = ctk.CTkLabel(window, height=60, text_color="black",
                                         text="File format",
                                         font=("Arial", 32, "bold"))
        self.format_label.grid(row=3, columnspan=7)
        self.format_switch = ctk.IntVar()
        self.format_switch.set(0)
        self.format_radiobutton_1 = ctk.CTkRadioButton(window, height=40, text="VIDEO", text_color="black",
                                                       variable=self.format_switch, value=0)
        self.format_radiobutton_2 = ctk.CTkRadioButton(window, height=40, text="AUDIO", text_color="black",
                                                       variable=self.format_switch, value=1)
        self.format_radiobutton_1.grid(row=4, columnspan=7)
        self.format_radiobutton_2.grid(row=5, columnspan=7)
        # TODO: QUANTITY CHOICE
        self.quantity_label = ctk.CTkLabel(window, height=60, text_color="black",
                                           text="Quantity od files",
                                           font=("Arial", 32, "bold"))
        self.quantity_label.grid(row=6, columnspan=7)
        self.quantity_switch = ctk.IntVar()
        self.format_switch.set(0)
        self.quantity_radiobutton_1 = ctk.CTkRadioButton(window, height=40, text="SINGLE", text_color="black",
                                                         variable=self.quantity_switch, value=0)
        self.quantity_radiobutton_2 = ctk.CTkRadioButton(window, height=40, text="PLAYLIST", text_color="black",
                                                         variable=self.quantity_switch, value=1)
        self.quantity_radiobutton_1.grid(row=7, columnspan=7)
        self.quantity_radiobutton_2.grid(row=8, columnspan=7)
        # TODO: DOWNLOAD PATH
        self.dir_path_label = ctk.CTkLabel(window, height=60, text_color="black", text="Download Path",
                                           font=("Arial", 32, "bold"))
        self.dir_path_label.grid(row=9, columnspan=7)
        self.download_path = ctk.StringVar(window, value="")
        self.download_path_entry = ctk.CTkEntry(window, width=550, textvariable=self.download_path)
        self.download_path_entry.grid(row=10, columnspan=7)
        self.browse_button = ctk.CTkButton(window, text="Browse...", command=self.file_system_explorer)
        self.browse_button.grid(row=10, column=5, columnspan=7)
        # TODO: LINK ENTRY
        self.link_label = ctk.CTkLabel(window, height=60, text_color="black", text="Source link",
                                       font=("Arial", 32, "bold"))
        self.link_label.grid(row=11, columnspan=7)
        self.link = ctk.StringVar(window, value="Provide your link here ...")
        self.link_entry = ctk.CTkEntry(window, width=1000, textvariable=self.link)
        self.link_entry.grid(row=12, columnspan=7)
        # TODO: DOWNLOAD BUTTON
        self.space_label_1 = ctk.CTkLabel(window, height=30, text_color="black", text="")
        self.space_label_1.grid(row=13, columnspan=7)
        self.download_button = ctk.CTkButton(window, height=60, width=180, text="DOWNLOAD", text_color="black",
                                             font=("Arial", 20, "bold"), command=self.download_playlist)
        self.download_button.grid(row=14, columnspan=7)
        self.space_label_2 = ctk.CTkLabel(window, height=30, text_color="black", text="")
        self.space_label_2.grid(row=15, columnspan=7)


wnd = ctk.CTk()
downloader = Downloader(wnd)
wnd.mainloop()
