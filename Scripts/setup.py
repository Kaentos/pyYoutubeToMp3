print("Starting setup...")
print("Importing packages...", end=" ")
try:
    import sys
    import configparser
    import os
    import zipfile
    from local_package import checkFunctions
except ImportError:
    print("ERROR!\n\nPlease make sure you have installed all the packages referenced in requirements.txt into the venv and you have all the scripts in Scripts/.")
    print("If you don't have files please download from: https://github.com/Kaentos/pyYoutubeToMp3")
    raise
except BaseException:
    print("Error 1: check Data/errorList.txt.")
    raise
print("OK!")


path_main = checkFunctions.checkIfInProjectPath() 
error_sufix = "ERROR!\n\n"

try:
    path = path_main + "Data/info.ini"
    if os.path.exists(path): 
        local_data = configparser.ConfigParser()
        local_data.read("Data/info.ini")
except PermissionError:
    print("You don't have permissions to read files.")
    raise
except BaseException:
    print("Error 2: check Data/errorList.txt.")
    raise

try:
    if local_data["user_settings"]["setup_concluded"] == True:
        print("You already runned this script do you wish to run it again? (y/n)")
        print("It may cause problems and will probably give you lots of errors.")
        op = input("Input: ").replace(" ", "")
        if op in ["y", "yes"]:
            local_data["user_settings"]["setup_concluded"] = False
        else:
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
        path_dest = checkFunctions.checkIfFolderExists(name="Data/Temp/AP", create=True)
        with zipfile.ZipFile(checkFunctions.checkIfFileExists(f"Data/Temp/{local_data['win32-setup']['AP_fileName']}", False) ,"r") as zip_file:
            zip_file.extractall(path_dest)
    except BaseException:
        raise
    print("OK!")