import customtkinter as ctk
from tkinter import filedialog
from pytube import Playlist
from PIL import Image
from moviepy.editor import VideoFileClip
import os


class Converter:
    def __init__(self, video_file, audio_file):
        self.video_file = video_file
        self.audio_file = audio_file

    def convert_mp4_to_mp3(self):
        video_clip = VideoFileClip(self.video_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(self.audio_file)
        video_clip.close()
        audio_clip.close()

    def remove_video_file(self):
        os.remove(self.video_file)


class Downloader:
    def yt_download_playlist(self):
        yt_playlist = Playlist(str(self.link.get()))
        counter = 1
        if bool(self.is_audio_only.get()):
            for video in yt_playlist.videos:
                file_name = self.prepare_name_for_audio_playlist(counter, video.title)
                video.streams.get_audio_only().download(output_path=str(self.download_path.get()), filename=file_name)
                print("Downloaded: ", file_name)  # TODO: zamienić to na info na okienku
                counter = counter + 1
            print("\nAll tracks have been downloaded.")  # TODO: zamienić to na info na okienku
        else:
            for video in yt_playlist.videos:
                file_name = self.prepare_name_for_video_playlist(counter, video.title)
                video.streams.get_highest_resolution().download(
                    output_path=str(self.download_path.get()), filename=file_name)
                print("Downloaded: ", file_name)
                counter = counter + 1
            print("\nAll videos have been downloaded.")

    def yt_download_single(self):
        pass

    def yt_download(self):
        if bool(self.is_a_playlist.get()):
            self.yt_download_playlist()
        else:
            self.yt_download_single()

    @staticmethod
    def prepare_name_for_video_playlist(counter, name):
        return "0" + str(counter) + " " + name + ".mp4" if counter < 10 else str(counter) + " " + name + ".mp4"

    @staticmethod
    def prepare_name_for_audio_playlist(counter, name):
        return "0" + str(counter) + " " + name + ".mp3" if counter < 10 else str(counter) + " " + name + ".mp3"

    @staticmethod
    def file_system_explorer(event, download_path):
        wnd.directory = filedialog.askdirectory(initialdir="/", title="Select a directory")
        download_path.set(wnd.directory)

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
        self.is_audio_only = ctk.IntVar()
        self.is_audio_only.set(0)
        self.format_radiobutton_1 = ctk.CTkRadioButton(window, height=40, text="VIDEO", text_color="black",
                                                       variable=self.is_audio_only, value=0)
        self.format_radiobutton_2 = ctk.CTkRadioButton(window, height=40, text="AUDIO", text_color="black",
                                                       variable=self.is_audio_only, value=1)
        self.format_radiobutton_1.grid(row=4, columnspan=7)
        self.format_radiobutton_2.grid(row=5, columnspan=7)
        # TODO: QUANTITY CHOICE
        self.quantity_label = ctk.CTkLabel(window, height=60, text_color="black",
                                           text="Quantity od files",
                                           font=("Arial", 32, "bold"))
        self.quantity_label.grid(row=6, columnspan=7)
        self.is_a_playlist = ctk.IntVar()
        self.is_a_playlist.set(0)
        self.quantity_radiobutton_1 = ctk.CTkRadioButton(window, height=40, text="SINGLE", text_color="black",
                                                         variable=self.is_a_playlist, value=0)
        self.quantity_radiobutton_2 = ctk.CTkRadioButton(window, height=40, text="PLAYLIST", text_color="black",
                                                         variable=self.is_a_playlist, value=1)
        self.quantity_radiobutton_1.grid(row=7, columnspan=7)
        self.quantity_radiobutton_2.grid(row=8, columnspan=7)
        # TODO: DOWNLOAD PATH
        self.dir_path_label = ctk.CTkLabel(window, height=60, text_color="black", text="Download Path",
                                           font=("Arial", 32, "bold"))
        self.dir_path_label.grid(row=9, columnspan=7)
        self.download_path = ctk.StringVar(window, value="")
        self.download_path_entry = ctk.CTkEntry(window, width=550, textvariable=self.download_path)
        self.download_path_entry.grid(row=10, columnspan=7)
        self.browse_button = ctk.CTkButton(window, text="Browse...")
        self.browse_button.bind("<Button-1>",
                                lambda event, arg=self.download_path: self.file_system_explorer(event, arg))
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
                                             font=("Arial", 20, "bold"), command=self.yt_download)
        self.download_button.grid(row=14, columnspan=7)
        self.space_label_2 = ctk.CTkLabel(window, height=30, text_color="black", text="")
        self.space_label_2.grid(row=15, columnspan=7)


wnd = ctk.CTk()
downloader = Downloader(wnd)
wnd.mainloop()
