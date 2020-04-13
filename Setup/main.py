print("Starting setup...\n\n")

try:
    import configparser
    import os
    import pathlib
except ImportError:
    print("Please make sure you have installed all the packages in requirements.txt to the venv.")
    raise
except BaseException:
    print("Error 1: check Data/errorList.txt.")
    raise

try:
    local_data = configparser.ConfigParser()
    local_data.read("Data/info.ini")
except PermissionError:
    print("You don't have permissions to read files.")
    raise
except OSError:
    print("Do you have Data/info.ini? If not please download from the original repository. https://github.com/Kaentos/pyYoutubeToMp3")
    raise
except BaseException:
    print("Error 2: check Data/errorList.txt.")
    raise

try:
    if local_data["user_setti2ngs"]["setup_concluded"] == True:
        print("You already runned this script do you wish to run it again? (y/n)\nIt may cause problems and will probably give you lots of errors.")
        op = input("Input: ").replace(" ", "")
        if op in ["y", "yes"]:
            local_data["user_settings"]["setup_concluded"] = False
        else:
            exit()
except KeyError:
    print("Please don't change Data/info.ini (if you don't what you are doing).\nTo fix this problem download info.ini from https://github.com/Kaentos/pyYoutubeToMp3.")
    raise

print("Creating necessary folders...", end=" ")
try:
    path = f"{pathlib.Path().absolute()}/Downloads"
    os.mkdir(path)
except PermissionError:
    print("You don't have permissions to create folders here!")
    raise
except OSError:
    print(f"Downloads folder is already created. If you wish to run this script please delete {path}/.")
    raise
except BaseException:
    print("Error 3: check Data/errorList.txt.")
    raise
print("OK!")

