from configparser import ConfigParser
import requests
import zipfile
import os
import shutil

if __name__ == "__main__":
    Info = ConfigParser()
    Info.read("info.ini")

    url = Info["ffmpeg"]["downloadLink"]
    print("Downloading ffmpeg.zip...")
    rContent = requests.get(url)
    print("ffmpeg.zip downloaded.")

    print("Creating Temp/...")
    try:
        os.mkdir("Temp")
    except OSError:
        print ("Error creating folder.")
    print ("Temp/ was successfully created.")

    print("Saving ffmpeg.zip to Temp/...")
    with open("Temp/ffmpeg.zip", "wb") as file:
        file.write(rContent.content)
    print("Saved successfully.")
    
    print("Unzipping ffmpeg.zip...")
    with zipfile.ZipFile("Temp/ffmpeg.zip", "r") as zip_file:
        zip_file.extractall("Temp/")
    print("Unzipped successfully.")

    print("Copying necessary files...")
    for file_name in os.listdir(f"Temp/{Info['ffmpeg']['fileName']}/bin"):
        print(file_name)
        shutil.copy(f"Temp/{Info['ffmpeg']['fileName']}/bin/{file_name}", f"venv/Scripts/{file_name}")
    print("All files copied.")

    print("Removing Temp/...")
    shutil.rmtree("Temp/")
    print("Temp/ removed.")