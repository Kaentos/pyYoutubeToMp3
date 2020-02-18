from youtube_dl import YoutubeDL
import requests
from configparser import ConfigParser
import checkFunctions
import resetFunctions

class DownloadOptions:
    def __init__(self):
        self.fileType = None
        self.isPlaylist = None
        self.fileFormat = None

    def ytdl_options(self):
        options = {
            "format": "bestaudio/best",
            "outtmpl": "Mp3/%(title)s.%(ext)s",
            "noplaylist": self.isPlaylist,
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
        return options

def getOP():
    return input("Option: ").lower()

def goBack(op):
    if op == 0 or "back" in op or op[0] == "b":
        return True
    else:
        return False
    
############################
#          Prints          #
############################
def printTitle(title):
    print(f"\n\n\n> {title} <")

def printSubTitle(title):
    print(f"\n# {title}")

def printBack():
    print("0) Back")

def printConvertType():
    printSubTitle("Convert to?")
    print("1) Audio")
    print("2) Video")
    printBack()
    return input("Option: ")

def getAudioFormat():
    while(True):
        audio_formats = ["MP3", "AAC", "FLAC", "M4A", "OPUS", "VORBIS", "WAV"]
        printSubTitle("Availabe audio formats:")
        for i, text in enumerate(audio_formats):
            print(f"{i+1}) {text}")
        printBack()
        op = getOP().upper()
        try:
            if op in audio_formats:
                return op.lower()
            elif int(op) in range(1, len(audio_formats) + 1):
                return audio_formats[int(op) - 1].lower()
            elif int(op) == 0 or op.lower() in ["back", "b"]:
                return False
            else:
                print("Not a valid format.\n")
        except ValueError:
            pass


def printVideoFormats():
    return "None"

def printInvalidOption(invalidType):
    print(f"The {invalidType} you chose is invalid!")
############################
#        End Prints        #
############################

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("Data/info.ini")
    
    video_formats = ["AVI", "MOV", "MP4", "WEBM", "WMV"]
    ytOptions = ["Single Video", "Multiples Videos", "Single Playlist", "Multiples Playlists"]
    ytAlias = [
        ["1", "single video", "singlevideo", "1 video", "1video", "single v", "singlev", "s video", "svideo", "video", "s v", "sv", "1 v", "1v", "v"],
        ["2", "multiple videos", "multiplevideos", "m videos", "mvideos", "multiple v", "multiplev", "m v", "mv", "vs"],
        ["3", "single playlist", "singleplaylist", "1 playlist", "1playlist", "playlist", "play", "list", "sp", "s p"],
        ["4", "multiple playlists", "multipleplaylists", "playlists", "lists", "plays", "mp", "m p"]
    ]
    DownOptions = DownloadOptions()
    print("Welcome to <projectname>!")
    print("What do you wish to do?")
    print("1) Youtube converter / downloader")
    print("2) Local converter")
    print("0) Exit")
    op = getOP()

    if op == "1" or any(alias in op for alias in ["youtube", "yt"]):
        DownOptions.fileType = "video"
        print("\n\n\n> Youtube <")
        for i, text in enumerate(ytOptions):
            print(f"{i+1}) {text}")
        printBack()
        getOP()
        if any(alias in op for alias in ytAlias[0]): # single video
            DownOptions.isPlaylist = False
            printTitle(ytOptions[0])
            while True:
                convertType = printConvertType()
                if convertType == "1": # audio
                    DownOptions.fileFormat = getAudioFormat()
                    if not DownOptions.fileFormat: # Wants to go back
                        print("<-- back\n")
                        break
                    else:
                        print(DownOptions.fileFormat)
                        print(DownOptions.ytdl_options())
                    break
                elif convertType == "2": # video
                    printVideoFormats()
                    break
                elif goBack(convertType):
                    break
                else:
                    printInvalidOption("convert type")
                

        elif any(alias in op for alias in ytAlias[1]): # multiple videos
            DownOptions.isPlaylist = False
            printTitle(ytOptions[1])
            printConvertType()

        elif any(alias in op for alias in ytAlias[2]): # single playlist
            DownOptions.isPlaylist = True
            printTitle(ytOptions[2])
            printConvertType()

        elif any(alias in op for alias in ytAlias[3]): # multiple playlists
            DownOptions.isPlaylist = True
            printTitle(ytOptions[3])
            printConvertType()












    exit()
    checkFunctions.checkURLFile()
    checkFunctions.checkMp3()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "Mp3/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {
                'key': 'FFmpegMetadata'
            },
        ]
    }

    basicURL = "https://www.youtube.com/watch?v="
    validURLs = []
    with open("musicURLs.txt", "r") as file:
        URLs = file.readlines()
        if len(URLs) > 0:
            for url in URLs:
                url = url.strip("\n")
                if basicURL in url:
                    if requests.get(f"{Info['yt']['checkLink']}{url}").status_code == 200:
                        validURLs.append(url)
        else:
            print("There are no URLs in musicURLs.txt.")
            exit()
    if validURLs:
        print(f"URLs to download: {validURLs}")
        with YoutubeDL(ydl_opts) as ydl:
            for url in validURLs:
                ydl.download([url])
        print("Download completed, check Mp3/.")
    else:
        print("There are no videos to convert, did you input some in musicURLs.txt? Did you input them correctly?")
        exit()

    resetFunctions.resetFile()