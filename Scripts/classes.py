from datetime import datetime

class youtube_dlOptions:
    def __init__(self):
        self.isPlaylist = None
        self.fileFormat = None
        self.folderName = None
        self.addThumbnail = None
        self.audio_formats = ["MP3", "M4A"]
        self.video_formats = ["MP4", "WEBM"]

    def getOptions(self):
        self.folderName = datetime.now().strftime('%Y-%m-%d %H%M%S')
        if self.fileFormat.upper() in self.audio_formats:
            options = {
                "format": "bestaudio/best",
                "outtmpl": f"Downloads/{self.folderName}" + "/%(title)s." + self.fileFormat,
                "noplaylist": not self.isPlaylist
            }
            if self.addThumbnail:
                options["writethumbnail"] = self.addThumbnail
                options["postprocessors"] = [{ "key" : "EmbedThumbnail" }]
        elif self.fileFormat.upper() in self.video_formats:
            options = {
                "format": "bestvideo[height<=2160]+bestaudio[ext=m4a]" if self.addThumbnail else "bestvideo[height<=2160]+bestaudio",
                "videoformat" : self.fileFormat,
                "outtmpl": f"Downloads/{self.folderName}" + "/%(title)s.%(ext)s",
                "noplaylist": not self.isPlaylist
            }
            if self.addThumbnail:
                options["writethumbnail"] = self.addThumbnail
                options["postprocessors"] = [{"key" : "EmbedThumbnail"}]
        # can add [filesize<XXM] to limit the maximum size of file 
        return options