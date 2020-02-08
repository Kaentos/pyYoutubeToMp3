from configparser import ConfigParser

Info = ConfigParser()
Info.read("Data/info.ini")

def resetFile():
    with open("musicURLs.txt", "w") as file:
        file.write(Info["txt"]["example"])