import os
import subprocess
import requests
import sys
import pathlib
import json
from local_package import creationFunctions



## OS related
def checkUserOS(issueLink):
    user_os = sys.platform
    if user_os == "win32":
        return ["win32", "explorer"]
    elif user_os == "linux":
        return ["linux", "xdg-open"]
    elif user_os == "darwin":
        return ["darwin", "open"]
    else:
        raise OSError("Your platform isn't supported, please open an issue on ")
## end of OS related



## Python related
def updatePackages(packages, issueLink):
    for p in packages:
        try:
            subprocess.call(['pip', 'install', '-U', p])
        except BaseException:
            raise BaseException(f"Something went wrong updating: {p}. Please try again, if it keeps giving you this error report it to: {issueLink}")

def checkOutDatedPackages(issueLink):
    try:
        outdated = subprocess.check_output(["pip", "list", "-o", "--format", "json"])
        outdated = [package["name"] for package in json.loads(outdated)]
        if outdated:
            print("Outdated packages: ", outdated)
            updatePackages(outdated, issueLink)
            print("Packages updated.")
        else:
            print("All packages are updated")
    except BaseException:
        raise BaseException(f"If it keeps giving you this error report it to: {issueLink}")
## end of python



## Files/Folders/Path related
def checkIfInProjectPath():
    project_name = "pyYoutubeDownloader"
    if project_name not in os.getcwd():
        print(f"Please execute this script inside project folder (folder name must be: {project_name}).")
        exit()
    else:
        path_main = os.getcwd().replace("\\", "/").partition(project_name)
        path_main = path_main[0] + path_main[1] + "/"
        return path_main

def checkIfFolderExists(name, create:bool):
    path = os.getcwd().replace("\\", "/") + f"/{name}"
    if not os.path.exists(path) and create:
        return creationFunctions.createFolder(path)
    elif not os.path.exists(path) and create == False:
        print(f"Missing {path}.")
        exit()
    else:
        return path

def checkIfFileExists(name, create:bool):
    path = os.path.join(pathlib.Path().absolute(), name)
    if not os.path.exists(path) and create:
        return creationFunctions.createFile(path)
    elif not os.path.exists(path) and create == False:
        print(f"Missing {path}.")
        exit()
    else:
        return path
## end files/folders/path



## Main.py related
def checkURL(url, checkLink):
    if requests.get(checkLink + url).status_code == 200:
        return True
    else:
        return False

def checkURLfromFile(issueLink):
    with open("url_input.txt", "r") as f:
        fContent = f.readlines()
    
    valid_urls = []
    print("Validating urls...", end=" ")
    for url in fContent:
        url = url.strip("\n")
        if len(url) >= 11 and checkURL(url, issueLink):
            valid_urls.append(url)
    print("OK.")

    print("Removing duplicated urls...", end=" ")
    valid_urls = set(valid_urls)
    print("OK.")
    print(f"Valid urls: {valid_urls}")
    return valid_urls
## end of main.py



if __name__ == "__main__":
    print("Run main.py!")
    exit()