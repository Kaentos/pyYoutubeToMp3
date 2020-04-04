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

def updatePackages(packages):
    for p in packages:
        try:
            subprocess.call(['pip', 'install', '-U', p])
        except:
            raise(f"Something went wrong updating: {p}. Please try again, if it keeps giving you this error report it to: https://github.com/Kaentos/pyYoutubeToMp3/issues")

def checkOutDatedPackages():
    outdated = subprocess.check_output(["pip", "list", "-o", "--format", "json"])
    outdated = [package["name"] for package in json.loads(outdated)]
    if outdated:
        print("Outdated packages: ", outdated)
        updatePackages(outdated)
        print("Packages updated.")
    else:
        print("All packages are updated")

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
    if not os.path.exists(path):
        print("Missing Downloads folder. Creating a new one...")
        os.mkdir(path)
        print("Done.")
    if user_os == "win32":
        subprocess.call(["explorer", path])
    elif user_os == "linux":
        subprocess.call(["xdg-open", path])
    elif user_os == "darwin":
        subprocess.call(["open", path])
    else:
        raise OSError("Your platform isn't supported, please open an issue.")

with open("Data/alias.json", "r") as f:
    alias = json.load(f)

# NÃO NECESSARIO
audio_formats = ["MP3", "AAC", "FLAC", "M4A", "OPUS", "OGG", "WAV"]
video_formats = ["MP4", "WEBM"]
# NÃO NECESSARIO

downloadOptions = classes.youtube_dlOptions()
checkOutDatedPackages()

has_file_type = False
has_file_format = False
file_formats = {
    "audio" : downloadOptions.audio_formats,
    "video" : downloadOptions.video_formats
}

def printFileFormats(file_type):
    if file_type == "audio":
        print("\n\n> Audio formats:\nThumbnail only available for MP3 and M4A formats.")
        print("1) MP3\n2) AAC\n3) FLAC\n4) M4A\n5) OPUS\n6) OGG\n7) WAV\n0) Back")
    elif file_type == "video":
        print("Video formats:")
        print("1) MP4\n2) WEBM\n0) Back")
    else:
        print("Error: I-FT")
        exit()

while True: # Main loop
    print("1) Start converting\n2) Open Download folder\n3) Settings / Options\n0) Exit")
    op = getOP()
    if op == "1": # Youtube Converter
        while True:
            if not has_file_type and not has_file_format:
                print("\n\n> File type:\n1) Audio\n2) Video\n0) Back")
                op = getOP().lower()
                if op in alias["audio_type"] or op in alias["video_type"]:
                    has_file_type = True
                elif op in alias["back"]:
                    break
                else:
                    print("Invalid file type.")
                    continue
            
            if has_file_type:
                if op in alias["audio_type"]:
                    printFileFormats("audio")
                    selected_format = "audio"
                elif op in alias["video_type"]:
                    printFileFormats("video")
                    selected_format = "video"
                op = getOP().lower()

                if op in alias["back"]:
                    has_file_type = False
                    continue
                if op.upper() not in file_formats[selected_format]:
                    try:
                        int_op = int(op)
                        if int_op > 0:
                            selected_format = file_formats[selected_format][int_op - 1].lower()
                            has_file_format = True
                        else:
                            raise IndexError
                    except (ValueError, IndexError): # handle not int or index out of bounds
                        print("Invalid audio format.")
                        continue
                else:
                    selected_format = op
                    has_file_format = True
            print(selected_format)
            
            if has_file_format:
                downloadOptions.fileFormat = selected_format
                print("\n\n> What do you which to convert?\n1) Single video\n2) Multiple videos\n3) Single playlist\n4) Multiple playlists\n0) Back")
                op = getOP()
                if op in alias["1video"]:
                    downloadOptions.isPlaylist = False
                    url = getVideoURL(alias)
                    if url:
                        downloadOne(url, downloadOptions.getOptions())
                        openFileOrFolder(os.path.join("Downloads", downloadOptions.folderName))
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
                            continue
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
                elif op in alias["back"]:
                    has_file_format = False
                else:
                    print("Invalid option!")

            if has_file_type and has_file_format: # if downloaded ask if user wants to quit
                print("Do you wish to exit? (y/n)")
                op = getOP().replace(" ", "")
                if op in ["1", "y", "yes"]:
                    exit()


    elif op == "2": # open download folder
        openFileOrFolder("Downloads")
    elif op == "3": # menu 2 / settings
        # Can clear downloads / remove all folders inside downloads
        print("Coming soon...")
        continue
    elif op in alias["back"]: # sair
        exit()
    else:
        print("OP inválida")