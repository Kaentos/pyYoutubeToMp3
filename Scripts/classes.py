from datetime import datetime

class youtube_dlOptions:
    def __init__(self):
        self.isPlaylist = None
        self.fileFormat = None
        self.folderName = None
        self.audio_formats = ["MP3", "AAC", "FLAC", "M4A", "OPUS", "OGG", "WAV"]
        self.video_formats = ["MP4", "WEBM"]

    def getOptions(self):
        self.folderName = datetime.now().strftime('%Y-%m-%d %H%M%S')
        if self.fileFormat.upper() in self.audio_formats:
            options = {
            "format": "bestaudio/best",
            "outtmpl": f"Downloads/{self.folderName}" + "/%(title)s." + self.fileFormat,
            "noplaylist": not self.isPlaylist
            }
        elif self.fileFormat.upper() in self.video_formats:
            options = {
                "format": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
                "videoformat" : self.fileFormat,
                "outtmpl": f"Downloads/{self.folderName}" + "/%(title)s.%(ext)s",
                "noplaylist": not self.isPlaylist
            }

        #if self.fileFormat in "mp3":
        #    options["writethumbnail"] = True
        #    options["postprocessors"].append({ "key" : "EmbedThumbnail" })
        return options