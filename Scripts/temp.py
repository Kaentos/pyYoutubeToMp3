import os
import subprocess
from youtube_dl import YoutubeDL
from datetime import datetime
import json
import configparser

## Local files
import classes
import checkFunctions
## End local files

local_data = configparser.ConfigParser()
local_data.read("Data/info.ini")

user_os = checkFunctions.checkUserOS(local_data["repo"]["issueLink"])
checkFunctions.checkOutDatedPackages(local_data["repo"]["issueLink"])

def getOP():
    return input("Option: ")

def getVideoURL(alias):
    print("URL must at least contain www.youtube.com/watch?v=<video_id> / ID must be 11 characters long.")
    while True:
        url = input("URL/ID: ")
        if "www.youtube.com/watch?v=" in url:
            if checkFunctions.checkURL(url, local_data["yt"]["checkLink"]):
                return url
        elif len(url) == 11: # 11 = length of video id
            url = f"https://www.youtube.com/watch?v={url}"
            if checkFunctions.checkURL(url, local_data["yt"]["checkLink"]):
                return url
        elif url in alias["back"]:
            return None

def getPlaylistURL(alias):
    print("URL must contain www.youtube.com/playlist?list=<playlist_id> or www.youtube.com/watch?=<video_id>&list=<playlist_id> / ID must be 34 characters long.")
    while True:
        url = input("URL/ID: ")
        if "www.youtube.com/playlist?list=" in url or "&list=" in url:
            if checkFunctions.checkURL(url, local_data["yt"]["checkLink"]):
                return url
        elif len(url) == 34:
            url = f"www.youtube.com/playlist?list={url}"
            if checkFunctions.checkURL(url, local_data["yt"]["checkLink"]):
                return url
        elif url in alias["back"]:
            return None

def downloadFromFile(alias, did_download, checkLink):
    while True:
        openFile("url_input.txt")
        print("\nDid you input all urls? (yes: continue, no: open file again, back: back)")
        op = getOP()
        if op in ["yes", "y"]:
            urls = checkFunctions.checkURLfromFile(checkLink)
            downloadMultiple(urls, downloadOptions.getOptions())
            openFolder(os.path.join("Downloads", downloadOptions.folderName))
            did_download = True
            return did_download
        elif op in alias["back"]:
            did_download = False
            return did_download
        elif op not in ["no", "n"]:
            continue

def downloadOne(url, ytdl_options):
    with YoutubeDL(ytdl_options) as ytdl:
        ytdl.download([url])

def downloadMultiple(urls, ytdl_options):
    for url in urls:
        with YoutubeDL(ytdl_options) as ytdl:
            ytdl.download([url])

def openFolder(name):
    path = checkFunctions.checkIfFolderExists(name)
    if path:
        subprocess.call([user_os[1], path])
    else:
        raise BaseException(f"The folder you trying to open has an error please open an issue at: {local_data['repo']['issueLink']}")

def openFile(name):
    path = checkFunctions.checkIfFileExists(name)
    if path:
        subprocess.call([user_os[1], path])
    else:
        raise BaseException(f"The file you trying to open has an error please open an issue at: {local_data['repo']['issueLink']}")

def printFileFormats(file_type):
    if file_type == "audio":
        print("\n\n> Audio formats:")
        print("1) MP3\n2) M4A\n0) Back")
    elif file_type == "video":
        print("\n\nVideo formats:")
        print("1) MP4\n2) WEBM\n0) Back")
    else:
        raise ValueError("Error: I-FT, invalid file type")

with open("Data/alias.json", "r") as f:
    alias = json.load(f)

downloadOptions = classes.youtube_dlOptions()

has_file_type = False
has_file_format = False
did_download = False
file_type = None
file_formats = {
    "audio" : downloadOptions.audio_formats,
    "video" : downloadOptions.video_formats
}

while True: # Main loop
    print("\n\n# Main Menu\n1) Start converting\n2) Open Download folder\n3) Settings / Options\n0) Exit")
    op = getOP()
    if op == "1": # Youtube Converter
        while True:
            if not has_file_type and not has_file_format:
                print("\n\n> File type:\n1) Audio\n2) Video\n0) Back")
                op = getOP().lower()
                if op in alias["audio_type"]:
                    has_file_type = True
                    file_type = "audio"
                elif op in alias["video_type"]:
                    has_file_type = True
                    file_type = "video"
                elif op in alias["back"]:
                    break
                else:
                    print("Invalid file type.")
                    continue

                print("\n\nDo you want to add thumbnail? (y/n)")
                op = getOP().lower().replace(" ", "")
                if op in ["1", "y", "yes"]:
                    downloadOptions.addThumbnail = True
                else:
                    downloadOptions.addThumbnail = False
            
            if has_file_type and not has_file_format:
                printFileFormats(file_type)
                op = getOP().lower()

                if op in alias["back"]:
                    has_file_type = False
                    continue
                if op.upper() not in file_formats[file_type]:
                    try:
                        int_op = int(op)
                        if int_op > 0:
                            selected_format = file_formats[file_type][int_op - 1].lower()
                            has_file_format = True
                        else:
                            raise IndexError
                    except (ValueError, IndexError): # handle not int or index out of bounds
                        print("Invalid audio format.")
                        continue
                else:
                    selected_format = op
                    has_file_format = True
            
            if has_file_format:
                downloadOptions.fileFormat = selected_format
                print("\n\n> What do you which to convert?\n1) Single video\n2) Multiple videos\n3) Single playlist\n4) Multiple playlists\n0) Back")
                op = getOP()
                if op in alias["1video"]:
                    downloadOptions.isPlaylist = False
                    url = getVideoURL(alias)
                    if url:
                        downloadOne(url, downloadOptions.getOptions())
                        openFolder(os.path.join("Downloads", downloadOptions.folderName))
                        did_download = True
                elif op in alias[">1video"]:
                    downloadOptions.isPlaylist = False
                    did_download = downloadFromFile(alias, did_download, local_data["yt"]["checkLink"])
                elif op in alias["1playlist"]:
                    downloadOptions.isPlaylist = True
                    url = getPlaylistURL(alias)
                    if url:
                        downloadOne(url, downloadOptions.getOptions())
                        openFolder(os.path.join("Downloads", downloadOptions.folderName))
                        did_download = True
                elif op in alias[">1playlist"]:
                    downloadOptions.isPlaylist = True
                    did_download = downloadFromFile(alias, did_download, local_data["yt"]["checkLink"])
                elif op in alias["back"]:
                    has_file_format = False
                else:
                    print("Invalid option.")
                    did_download = False

            if did_download: # if downloaded ask if user wants to quit
                print("\n\nDo you wish to exit? (y/n)")
                op = getOP().replace(" ", "")
                if op in ["1", "y", "yes"]:
                    exit()
                else:
                    has_file_format = False
                    has_file_type = False


    elif op == "2": # open download folder
        openFolder("Downloads")
    elif op == "3": # settings
        # Can clear downloads / remove all folders inside downloads
        print("Coming soon...")
        continue
    elif op in alias["back"]: # exit
        exit()
    else:
        print("Invalid option.")