print("Starting setup...")
print("Importing packages...", end=" ")
try:
    import configparser
    import os
    import zipfile
except ImportError:
    print("Please make sure you have installed all the packages in requirements.txt to the venv.")
    raise
except BaseException:
    print("Error 1: check Data/errorList.txt.")
    raise
print("OK!")

project_name = "pyYoutubeDownloader"
if project_name not in os.getcwd():
    print(f"Please execute this script inside project folder ({project_name}).")
    exit()
else:
    path_main = os.getcwd().replace("\\", "/").partition(project_name)
    path_main = path_main[0] + path_main[1] + "/"
    del project_name
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

print("Creating necessary folders...", end=" ")
try:
    path = f"{path_main}/Downloads"
    os.mkdir(path)
except PermissionError:
    print(f"{error_sufix}You don't have permissions to create folders here!")
    raise
except OSError:
    print(f"{error_sufix}Downloads folder is already created. If you wish to run this script please delete {path}/.")
    raise
except BaseException:
    print(f"{error_sufix}Error 3: check Data/errorList.txt.")
    raise
print("OK!")

print("Extracting AtomicParsley...")
try:
    path
    with zipfile.ZipFile("Setup/"):
        exit()
    path_dest = f"{pathlib.Path().absolute()}/Temp"
except:
    exit()