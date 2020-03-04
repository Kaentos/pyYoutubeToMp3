import requests
import os
from youtube_dl import YoutubeDL
from datetime import datetime

## This file will replace main.py

class youtube_dlOptions:
    def __init__(self):
        self.isPlaylist = None
        self.fileFormat = None
        self.folderName = None

    def setFolderName(self):
        now = datetime.now()
        newName = now.strftime("%Y-%m-%d %H%M%S")
        self.folderName = newName

    def getOptions(self):
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"Downloads/{self.folderName}" + "/%(title)s.%(ext)s",
            "noplaylist": not self.isPlaylist,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self.fileFormat,
                    "preferredquality": "192",
                },
                {
                    'key': 'FFmpegMetadata'
                },
            ]
        }
        if self.fileFormat in "mp3":
            options["writethumbnail"] = True
            options["postprocessors"].append({ "key" : "EmbedThumbnail" })
        return options


def getOP():
    return input("Option: ")

def getVideoURL(alias):
    print("URL must at least contain www.youtube.com/watch?v= / ID must be 11 characters long.")
    while True:
        url = input("URL/ID: ")
        if "www.youtube.com/watch?v=" in url:
            if checkURL(url):
                return url
        elif len(url) == 11: # 11 = length of video id
            url = f"www.youtube.com/watch?v={url}"
            if checkURL(url):
                return url
        elif url in alias["back"]:
            return None

def getPlaylistURL(alias):
    print("URL must contain www.youtube.com/playlist?list= or www.youtube.com/watch?=<id>&list= / ID must be 34 characters long.")
    while True:
        url = input("URL/ID: ")
        if "www.youtube.com/playlist?list=" in url or "&?list=" in url:
            if checkURL(url):
                return url
        elif len(url) == 34:
            url = f"https://www.youtube.com/oembed?format=json&url=www.youtube.com/playlist?list={url}"
            if checkURL(url):
                return url
        elif url in alias["back"]:
            return None

def checkURL(url):
    if requests.get(f"https://www.youtube.com/oembed?format=json&url={url}").status_code == 200:
        return True
    else:
        return False

def downloadOne(url, ytdl_options):
    print(ytdl_options)
    print(url)
    with YoutubeDL(ytdl_options) as ytdl:
        ytdl.download([url])

alias = { # Dict that stores alias for options
    ## type of conversion ##
    "youtube" : [ "1", "s", "start", "convert", "yt", "you", "tube", "youtube" ],
    "settings" : [ "2", "set", "sett", "settings", "o", "op", "opt", "options"],
    ## End of type of conversion ##

    ## File type ##
    "audio_type" : [ "1", "a", "aux", "audio" ],
    "video_type" : [ "2", "v", "vid", "video" ],
    ## End file type ##

    ## Conversion options ##
    "1video" : ["1", "single video", "singlevideo", "1 video", "1video", "single v", "singlev", "s video", "svideo", "video", "s v", "sv", "1 v", "1v", "v"],
    ">1video" : ["2", "multiple videos", "multiplevideos", "m videos", "mvideos", "multiple v", "multiplev", "m v", "mv", "vs"],
    "1playlist" : ["3", "single playlist", "singleplaylist", "1 playlist", "1playlist", "playlist", "play", "list", "sp", "s p"],
    ">1playlist" : ["4", "multiple playlists", "multipleplaylists", "playlists", "lists", "plays", "mp", "m p"],
    ## End conversion options ##

    ## Back option ##
    "back": ["0", "b", "back", "exit"]
    ## End back option ##
}

audio_formats = ["MP3", "ACC", "FLAC", "M4A", "OPUS", "VORBIS", "WAV"]
downloadOptions = youtube_dlOptions()

while True: # Main loop
    print("1) Start converting\n2) Open Download folder\n3) Settings / Options\n0) Exit")
    op = getOP()
    if op == "1": # Youtube Converter
        while op not in alias["back"]: # get file type (audio or video)
            print("\n\n> File type:\n1) Audio\n2) Video\n0) Back")
            op = getOP()
            if op in alias["audio_type"]: # User choose audio type
                print("\n\n> Audio format:\nThumbnail only available for MP3 and M4A formats.")
                print("1) MP3\n2) ACC\n3) FLAC\n4) M4A\n5) OPUS\n6) VORBIS\n7) WAV\n0) Back")
                while True:
                    op = getOP().lower()
                    if op not in audio_formats: # check if user inputed number
                        try:
                            selected_format = audio_formats[int(op) - 1].lower()
                        except (ValueError, IndexError): # handle not int or index out of bounds
                            print("Invalid audio format.")
                            continue
                    else:
                        selected_format = op
                    downloadOptions.fileFormat = selected_format
                    break
            elif op in alias["video_type"]: # User choose video type
                while True:
                    print("Menu video")
                    op = getOP()
                    ## Set file ext/format in class
                    break
            elif op in alias["back"]: # Return to main menu
                break
            else:
                print("Invalid file type.")
                continue

            # Get option (1 video, >1 videos, 1 playlist, >1 playlist)
            if op not in alias["back"]:
                print("\n\n> What do you which to convert?\n1) Single video\n2) Multiple videos\n3) Single playlist\n4) Multiple playlists")
                while True:
                    op = getOP()
                    if op in alias["1video"]:
                        downloadOptions.isPlaylist = False
                        downloadOptions.setFolderName()
                        url = getVideoURL(alias)
                        if url:
                            downloadOne(url, downloadOptions.getOptions())
                        break
                    elif op in alias[">1video"]:
                        downloadOptions.isPlaylist = False
                        ## open text file
                        break
                    elif op in alias["1playlist"]:
                        downloadOptions.isPlaylist = True
                        url = getPlaylistURL(alias)
                        if url:
                            pass #download
                        break
                    elif op in alias[">1playlist"]:
                        downloadOptions.isPlaylist = True
                        ## open text file
                        break

            if op in alias["back"]:
                break
            else: 
                print("Do you wish to exit? (y/n)")
                op = getOP()
                if op == "y" or op == "yes":
                    exit()


    elif op == "2":
        os.startfile("Downloads")
    elif op == "3": # menu 2 / settings
        print("Coming soon...")
        continue
    elif op in alias["back"]: # sair
        exit()
    else:
        print("OP inválida")