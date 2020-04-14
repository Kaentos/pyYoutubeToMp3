try:
    import os
    import subprocess
    import requests
    import sys
    import pathlib
    import json
    import configparser
    import time
    from local_package import creationFunctions
    from local_package import getFunctions
except ImportError:
    print("\n\nPlease install the missing package with 'pip install <package_name>' into to the venv.")
    raise


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
    project_name = getFunctions.getLocalData()["project-details"]
    project_name = [project_name["name"], project_name["name_branch"]]
    if project_name[0] and os.getcwd().endswith(project_name[0]):
        project_name = project_name[0]
    elif project_name[1] and os.getcwd().endswith(project_name[1]):
        print(f"It's recommened to rename project folder from {project_name[1]} to {project_name[0]}")
        project_name = project_name[1]
        time.sleep(3)
    else:
        print("Run this script inside project folder!")
        exit()

    path_main = os.getcwd().replace("\\", "/").partition(project_name)
    path_main = path_main[0] + path_main[1] + "/"
    return path_main

def checkIfFolderExists(name, create:bool):
    path = os.getcwd().replace("\\", "/") + f"/{name}"
    if os.path.exists(path):
        return path
    elif not os.path.exists(path) and create:
        return creationFunctions.createFolder(path)
    elif not os.path.exists(path) and create == False:
        return False

def checkIfFileExists(name, create:bool):
    path = os.getcwd().replace("\\", "/") + f"/{name}"
    if os.path.exists(path):
        return path
    elif not os.path.exists(path) and create:
        return creationFunctions.createFile(path)
    elif not os.path.exists(path) and create == False:
        return False
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