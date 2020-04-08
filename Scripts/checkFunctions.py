import os
import subprocess
import requests
import sys
import pathlib
import json



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



## Files/Folders related
def checkIfFolderExists(name):
    path = os.path.join(pathlib.Path().absolute(), name)
    if not os.path.exists(path):
        print("Missing folder. Creating a new one...")
        try: 
            os.mkdir(path)
        except BaseException:
            raise BaseException("Cannot create folder")
        print("Done.")
        return path
    else:
        return path

def checkIfFileExists(name):
    path = os.path.join(pathlib.Path().absolute(), name)
    if not os.path.exists(path):
        print("Missing file. Creating a new one...")
        try:
            with open(path, "w") as f:
                f.close()
        except BaseException:
            raise BaseException("Cannot create file.")
        print("Done.")
        return path
    else:
        return path
## end files/folders



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