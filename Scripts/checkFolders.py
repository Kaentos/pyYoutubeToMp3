import os

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

if __name__ == "__main__":
    print("You can only run this script via other script!")