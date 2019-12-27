from __future__ import unicode_literals
import youtube_dl

if __name__ == "__main__":
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "Mp3/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

    with open("musicURLs.txt", "r") as file:
        URLs = file.readlines()
        URLs = [url.strip("\n") for url in URLs]
    print(URLs)
    
    # Validate URLs
    URLs = [ url for url in URLs[1:] if "https://www.youtube.com/watch?v=" in url ]
    print(URLs)


    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #    ydl.download([''])

    with open("musicURLs.txt", "w") as file:
        file.write("> Give a new line for each link (link example: https://www.youtube.com/watch?v=Dqq2wXW3X2Q) <")