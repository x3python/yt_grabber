import yt_dlp
from tkinter import *
import validators
import time
import re

root = Tk()
root.title("YouTube to mp3 Converter")
root.geometry("800x350")
root["bg"] = "#212529"

logo = PhotoImage(file = "logo.png")
lg_label = Label(root, image=logo, borderwidth = 0, highlightthickness=1, highlightbackground="#212529", activebackground="#212529")
lg_label.pack(pady=30)

title_label = Label(root, text = "To convert video to mp3 just enter a link here: ", font = "sans-serif")
title_label.place(x=210,y=110)
title_label["bg"] = "#212529"


box = Entry(root)
box["bg"] = "#ccc5b9"
box["fg"] = "black"
box["relief"] = "flat"
box.place(x=125,y=140, width=550, height=35)


def click():
    url=box.get()
    if validators.url(url) == True:
        URLS = [url]
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'mp3/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',}]
                }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                file = info['title'] + '.mp3'
                x = re.sub("[\(\[].*?[\)\]]", "", file)
                error_code = ydl.download(URLS)
        except:
            errorServer = Label(root, text = "Sorry, this Url doesn't support the programm", font = "sans-selif")
            errorServer.place(x=150,y=180, width=500, height=30)
            errorServer["bg"] = "#212529"
            errorServer["fg"] = "#eb5e28"
            root.after(4000, errorServer.destroy)
            root.after(box.delete(0,END))

        done_mess = Label(root, text = x+"\n Done!", font = "sans-selif")
        done_mess.place(x=25,y=180, width=750, height=50)
        done_mess["bg"] = "#212529"
        done_mess["fg"] = "#eb5e28"
        root.after(10000, done_mess.destroy)
        box.delete(0,END)

    else:
        labelError = Label(root, text = "Enter a link please...", font = "sans-serif")
        labelError.place(x=285,y=180, width=200, height=30)
        labelError["bg"] = "#212529"
        labelError["fg"] = "#eb5e28"
        root.after(3000, labelError.destroy)

btn = PhotoImage(file = "btn.png")
bt = Button(root, image=btn, command = click, borderwidth = 0, highlightthickness=1, highlightbackground="#212529", activebackground="#212529")
bt["relief"] = "flat"
bt["bg"] = "#212529"

bt.place(x=330,y=240, width=120, height=44)


root.mainloop()
