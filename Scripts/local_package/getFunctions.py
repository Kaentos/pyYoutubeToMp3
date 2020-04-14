import configparser
import os

def getLocalData():
    try:
        if os.path.exists("Data/info.ini"): 
            local_data = configparser.ConfigParser()
            local_data.read("Data/info.ini")
            return local_data
        else:
            return None
    except PermissionError:
        print("You don't have permissions to read files.")
        raise
    except BaseException:
        print("Error 2: check Data/errorList.txt.")
        raise