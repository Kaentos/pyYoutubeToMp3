print("Starting setup...")
print("Importing packages...", end=" ")
try:
    import sys
    import configparser
    import os
    import zipfile
    import shutil
    from local_package import checkFunctions
    from local_package import getFunctions
except ImportError:
    print("ERROR!\n\nPlease make sure you have installed all the packages referenced in requirements.txt into the venv and you have all the scripts in Scripts/.")
    print("If you don't have files please download from: https://github.com/Kaentos/pyYoutubeToMp3")
    raise
except BaseException:
    print("Error 1: check Data/errorList.txt.")
    raise
print("OK!")


path_main = checkFunctions.checkIfInProjectPath()
local_data = getFunctions.getLocalData() 
error_sufix = "ERROR!\n\n"

try:
    if local_data["user_settings"]["setup_concluded"] == True:
        print("You cannot run this script again!")
        print("If you still want to run it, you will need to delete project folder it's recommended to remove all project files and download it again from: https://github.com/Kaentos/pyYoutubeToMp3")
        exit()
except KeyError:
    print("Please don't change Data/info.ini (if you don't what you are doing).")
    print("To fix this problem download info.ini from https://github.com/Kaentos/pyYoutubeToMp3 and replace yours.")
    raise



## Creation of folders
print("Creating necessary folders...", end=" ")
result = checkFunctions.checkIfFolderExists(name="Downloads", create=True)
print("OK!")
## End creation of folders

if os.sys.platform == "win32":
    print("Extracting AtomicParsley...", end=" ")
    try:
        if not checkFunctions.checkIfFolderExists(name="Data/Temp", create=False):
            print("Missing Temp Files...")
            exit()
        path_dest = checkFunctions.checkIfFolderExists(name="Data/Temp/toMove", create=True)
        with zipfile.ZipFile(checkFunctions.checkIfFileExists(f"Data/Temp/{local_data['win32-setup']['AP_zipName']}", False) ,"r") as zip_file:
            for filename in zip_file.namelist():
                if local_data["win32-setup"]["AP_fileName"] in filename:
                    zip_file.extract(filename, path=path_dest)
    except BaseException:
        raise
    print("OK!")
    print("Moving AtomicParsley...", end=" ")
    try:
        if checkFunctions.checkIfFileExists(name=f"venv/Scripts/{local_data['win32-setup']['AP_fileName']}", create=False) == False:
            path_AP = path_dest + "/" + local_data["win32-setup"]["AP_fileName"]
            path_dest = path_main + "venv/Scripts"
            shutil.move(path_AP, path_dest)
            print("OK!")
        else:
            print("NOT NEEDED, OK!")
            pass
    except PermissionError:
        print(f"{error_sufix}You don't have permissions to move files!")
        raise
    except OSError:
        raise
    except BaseException:
        print(f"{error_sufix}Error 4: check Data/errorList.txt.")
    
    print("Removing Temp folder...", end=" ")
    