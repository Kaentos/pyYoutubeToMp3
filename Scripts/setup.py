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
    print("\n\nPlease install the missing package with 'pip install <package_name>' into to the venv.")
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
    if checkFunctions.checkIfFileExists(name=f"venv/Scripts/{local_data['win32-setup']['AP_fileName']}", create=False) == False:
        print("Extracting AtomicParsley...", end=" ")
        try:
            if not checkFunctions.checkIfFolderExists(name="Data/Temp", create=False):
                print(f"{error_sufix}Missing Temp Files. Please download them again.")
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
            path_AP = path_dest + "/" + local_data["win32-setup"]["AP_folderName"] + "/" + local_data["win32-setup"]["AP_fileName"]
            path_dest = path_main + "venv/Scripts"
            shutil.move(path_AP, path_dest)
            print("OK!")
        except PermissionError:
            print(f"{error_sufix}You don't have permissions to move files!")
            raise
        except OSError:
            raise
        except BaseException:
            print(f"{error_sufix}Error 4: check Data/errorList.txt.")
            raise
        
        print("Removing Temp folder...", end=" ")
        shutil.rmtree(f"{path_main}/Data/Temp")
        print("OK!")
    