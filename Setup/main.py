print("Starting setup...\n\n")

try:
    import configparser
    import os
    import pathlib
except ImportError:
    raise ImportError("Please make sure you have installed all the packages in requirements.txt to the venv.")
except BaseException:
    raise BaseException("Error 1: check Data/errorList.txt.")

try:
    local_data = configparser.ConfigParser()
    local_data.read("Data/info.ini")
except PermissionError:
    raise PermissionError("You don't have permissions to read files.")
except OSError:
    raise OSError("Do you have Data/info.ini? If not please download from the original repository. https://github.com/Kaentos/pyYoutubeToMp3")
except BaseException:
    raise BaseException("Error 2: check Data/errorList.txt.")

print("Creating necessary folders...", end=" ")
try:
    path = f"{pathlib.Path().absolute()}/Downloads"
    os.mkdir(path)
except PermissionError:
    raise PermissionError("You don't have permissions to create folders here!")
except OSError:
    raise OSError(f"Downloads folder is already created. If you wish to run this script please delete {path}/.")
except BaseException:
    raise BaseException("Error 3: check Data/errorList.txt.")
print("OK!")

