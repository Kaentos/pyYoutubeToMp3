import os
import resetFunctions

def checkSinglePlaylist():
    if not os.path.exists("SinglePlaylist/"):
        print("Missing folder. Creating SinglePlaylist/.")
        os.mkdir("SinglePlaylist/")
        print("SinglePlaylist/ created.")

def checkMp3():
    if not os.path.exists("Mp3/"):
        print("Missing folder. Creating Mp3/.")
        os.mkdir("Mp3/")
        print("Mp3/ created.")

def checkURLFile():
    if not os.path.exists("musicURLs.txt"):
        print("musicURLs.txt not found, creating a new one...")
        resetFunctions.resetFile()
        print("musicURLs.txt created, you can now input your music URLs there.")
        exit()

if __name__ == "__main__":
    print("You can only run this script via other script!")