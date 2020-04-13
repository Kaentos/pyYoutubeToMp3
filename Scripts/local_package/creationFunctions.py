import os

def createFolder(path):
    try:
        os.mkdir(path)
    except PermissionError:
        print("You do not have enough permissions to create folders.")
        raise
    except OSError:
        print(f"{path} folder is already created.")
        raise
    except BaseException:
        print("Error 3: check Data/errorList.txt.")
        raise
    return path