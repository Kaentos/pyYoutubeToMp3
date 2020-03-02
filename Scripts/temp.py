def getOP():
    return input("Option: ")

alias = { # Dict that stores alias for options
    ## type of conversion ##
    "youtube" : [ "1", "s", "start", "convert", "yt", "you", "tube", "youtube" ],
    "settings" : [ "2", "set", "sett", "settings", "o", "op", "opt", "options"],
    ## End of type of conversion ##

    ## File type ##
    "audio_type" : [ "1", "a", "aux", "audio" ],
    "video_type" : [ "2", "v", "vid", "video" ],
    ## End file type ##

    ## Back option ##
    "back": ["0", "b", "back", "exit"]
    ## End back option ##
}

audio_formats = ["MP3", "ACC", "FLAC", "M4A", "OPUS", "VORBIS", "WAV"]


while True: # Main loop
    print("1) Start converting\n2) Settings / Options\n0) Exit")
    op = getOP()
    if op == "1": # youtube converter
        print("1) Audio\n2) Video\n0) Back")
        while op not in alias["back"]: # get file type (audio or video)
            op = getOP()
            if op in alias["audio_type"]: # User choose audio type
                print("Thumbnail only available to MP3 and M4A formats.")
                print("1) MP3\n2) ACC\n3) FLAC\n4) M4A\n5) OPUS\n6) VORBIS\n7) WAV\n0) Back")
                while True:
                    op = getOP().lower()
                    if op not in audio_formats: # check if user inputed number
                        try:
                            selected_format = audio_formats[int(op) - 1]
                        except (ValueError, IndexError): # handle not numbers and index out of bounds
                            print("Invalid audio format.")
                            continue
                    else:
                        selected_format = op
                    ## Set file ext/format in class
                    break
            elif op in alias["video_type"]: # User choose video type
                while True:
                    print("Menu 2.2 / tipo de ficheiro desejado")
                    op = getOP()
                    ## Set file ext/format in class
                    break

            elif op in alias["back"]: # Return to main menu
                break
            else:
                print("Invalid file type.")
                continue

            # Get option (1 video, >1 videos, 1 playlist, >1 playlist)
            while op not in alias["back"]:
                print("Menu 3 / pedir opção se é para um ou mais videos/playlists")
                op = getOP()
                print("faz")
                op = "back"
        continue




    elif op == "2": # menu 2 / settings
        print("Coming soon...")
        continue
    elif op in alias["back"]: # sair
        exit()
    else:
        print("OP inválida")