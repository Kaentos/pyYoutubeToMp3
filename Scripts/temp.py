import requests
import os
import subprocess
import sys
import pathlib
from youtube_dl import YoutubeDL
from datetime import datetime
import json

## Local files
import classes
## End local files


## This file will replace main.py


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

def downloadMultiple(urls, ytdl_options):
    print(ytdl_options)
    for url in urls:
        print(url)
        with YoutubeDL(ytdl_options) as ytdl:
            ytdl.download([url])

def checkURLfromFile():
    with open("url_input.txt", "r") as f:
        fContent = f.readlines()
    
    valid_urls = []
    print("Validating urls...", end=" ")
    for url in fContent:
        url = url.strip("\n")
        if checkURL(url):
            valid_urls.append(url)
    print("OK.")

    print("Removing duplicated urls...", end=" ")
    valid_urls = set(valid_urls)
    print("OK.")
    print(f"Valid urls: {valid_urls}")
    return valid_urls

def openFileOrFolder(name):
    user_os = sys.platform
    path = os.path.join(pathlib.Path().absolute(), name)
    print(path)
    if user_os == "win32":
        subprocess.call(["explorer", path])
    elif user_os == "linux":
        subprocess.call(["xdg-open", path])
    elif user_os == "darwin":
        subprocess.call(["open", path])

with open("Data/alias.json", "r") as f:
    alias = json.load(f)

audio_formats = ["MP3", "AAC", "FLAC", "M4A", "OPUS", "VORBIS", "WAV"]
downloadOptions = classes.youtube_dlOptions()

while True: # Main loop
    print("1) Start converting\n2) Open Download folder\n3) Settings / Options\n0) Exit")
    op = getOP()
    if op == "1": # Youtube Converter
        while op not in alias["back"]: # get file type (audio or video)
            print("\n\n> File type:\n1) Audio\n2) Video\n0) Back")
            op = getOP()
            if op in alias["audio_type"]: # User choose audio type
                print("\n\n> Audio format:\nThumbnail only available for MP3 and M4A formats.")
                print("1) MP3\n2) AAC\n3) FLAC\n4) M4A\n5) OPUS\n6) VORBIS\n7) WAV\n0) Back")
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
                        url = getVideoURL(alias)
                        if url:
                            downloadOne(url, downloadOptions.getOptions())
                            openFileOrFolder(os.path.join("Downloads", downloadOptions.folderName))
                        break
                    elif op in alias[">1video"]:
                        downloadOptions.isPlaylist = False
                        while True:
                            openFileOrFolder("url_input.txt")
                            print("Did you input all urls? (yes: continue, no: open file again, exit: quit)")
                            op = getOP()
                            if op in ["yes", "y"]:
                                urls = checkURLfromFile()
                                downloadMultiple(urls, downloadOptions.getOptions())
                                openFileOrFolder(os.path.join("Downloads", downloadOptions.folderName))
                                break
                            elif op not in ["no", "n"]:
                                break
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
                op = getOP().replace(" ", "")
                if op in ["y", "yes", alias["back"]]:
                    exit()


    elif op == "2":
        openFileOrFolder("Downloads")
    elif op == "3": # menu 2 / settings
        print("Coming soon...")
        continue
    elif op in alias["back"]: # sair
        exit()
    else:
        print("OP inválida")