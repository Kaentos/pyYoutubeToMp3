from configparser import ConfigParser
import requests


Info = ConfigParser()
Info.read("info.ini")

url = Info["ffmpeg"]["downloadLink"]
rContent = requests.get(url)

with open('ffmpeg.zip', 'wb') as file:
    file.write(rContent.content)