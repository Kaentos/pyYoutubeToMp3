from datetime import datetime

class youtube_dlOptions:
    def __init__(self):
        self.isPlaylist = None
        self.fileFormat = None

    def getOptions(self):
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"Downloads/{datetime.now().strftime('%Y-%m-%d %H%M%S')}" + "/%(title)s.%(ext)s",
            "noplaylist": not self.isPlaylist,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self.fileFormat,
                    "preferredquality": "192",
                },
                {
                    'key': 'FFmpegMetadata'
                },
            ]
        }
        if self.fileFormat in "mp3":
            options["writethumbnail"] = True
            options["postprocessors"].append({ "key" : "EmbedThumbnail" })
        return options