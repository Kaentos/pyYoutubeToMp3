from configparser import ConfigParser
import requests
import zipfile
import os

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("info.ini")

    url = Info["ffmpeg"]["downloadLink"]
    print("Downloading ffmpeg.zip...")
    rContent = requests.get(url)
    print("ffmpeg.zip downloaded.")

    with open("ffmpeg.zip", "wb") as file:
        file.write(rContent.content)
    
    with zipfile.ZipFile("ffmpeg.zip", "r") as zip_file:
        zip_file.extractall("Temp")

    print("Removing ffmpeg.zip...")
    os.remove("ffmpeg.zip")
    print("ffmpeg.zip removed.")