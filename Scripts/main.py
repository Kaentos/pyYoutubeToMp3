op2, op3 = "-1", "-1"

while True: # main loop
    op = input("MAIN: 1,2,0\nINPUT: ")
    if op == "1": # converter
        while True:

            if op2 == "-1" and op3 == "-1": # buscar tipo
                op = input("TIPO: 1,2,0\nINPUT: ")
                if op == "1": # audio
                    op2 = "1"                

                if op == "2": # video
                    op2 = "2"

                elif op == "0": # sair para anterior - main
                    break
            
            if op2 in ["1", "2"]: # buscar formato
                op = input("Formato: 1,2,0\nINPUT: ")
                if op == "1": # f1
                    op3 = "1"                

                if op == "2": # f2
                    op3 = "2"
                elif op == "0": # sair para anterior - buscar tipo
                    op2 = "-1"

            if op3 in ["1", "2"]: # buscar conteudo
                op = input("Conteudo: 1,2,0\nINPUT: ")
                if op == "1": # c1
                    op4 = "1"                

                if op == "2": # c2
                    op4 = "2"

                elif op == "0": # sair para anterior - formato
                    op3 = "-1"

            
        
    else:
        exit()



while op not in alias["back"]: # get file type (audio or video)
            print("\n\n> File type:\n1) Audio\n2) Video\n0) Back")
            op = getOP()
            if op in alias["audio_type"]: # User choose audio type
                print("\n\n> Audio formats:\nThumbnail only available for MP3 and M4A formats.")
                print("1) MP3\n2) AAC\n3) FLAC\n4) M4A\n5) OPUS\n6) OGG\n7) WAV\n0) Back")
                while True:
                    op = getOP().lower()
                    if op in alias["back"]:
                        break
                    elif op.upper() not in audio_formats: # check if maybe the user inputed number
                        try:
                            int_op = int(op)
                            if int_op > 0:
                                selected_format = audio_formats[int_op - 1].lower()
                            else:
                                raise IndexError
                        except (ValueError, IndexError): # handle not int or index out of bounds
                            print("Invalid audio format.")
                            continue
                    else:
                        selected_format = op
                    downloadOptions.fileFormat = selected_format
                    break
            elif op in alias["video_type"]: # User choose video type
                while True:
                    print("Video formats:")
                    print("1) MP4\n2) WEBM\n0) Back")
                    op = getOP()
                    if op in alias["back"]:
                        op = "1-1"
                        break
                    elif op.upper() not in video_formats: # check if maybe the user inputed number
                        try:
                            int_op = int(op)
                            if int_op > 0:
                                selected_format = video_formats[int_op - 1].lower()
                            else:
                                raise IndexError
                        except (ValueError, IndexError): # handle not int or index out of bounds
                            print("Invalid video format.")
                            continue
                    else:
                        selected_format = op
                    downloadOptions.fileFormat = selected_format
                    break
            elif op in alias["back"]: # Return to main menu
                break
            else:
                print("Invalid file type.")
                continue
            
            if op == "1-1":
                continue

            # Get option (1 video, >1 videos, 1 playlist, >1 playlist)
            if op not in alias["back"]:
                print("\n\n> What do you which to convert?\n1) Single video\n2) Multiple videos\n3) Single playlist\n4) Multiple playlists\n0) Back")
                while True:
                    op = getOP()
                    if op in alias["1video"]:
                        downloadOptions.isPlaylist = False
                        url = getVideoURL(alias)
                        if url:
                            downloadOne(url, downloadOptions.getOptions())
                            openFileOrFolder(os.path.join("Downloads", downloadOptions.folderName))
                        break
                    elif op in alias[">1video"]:
                        downloadOptions.isPlaylist = False
                        while True:
                            openFileOrFolder("url_input.txt")
                            print("Did you input all urls? (yes: continue, no: open file again, exit: quit)")
                            op = getOP()
                            if op in ["yes", "y"]:
                                urls = checkURLfromFile()
                                downloadMultiple(urls, downloadOptions.getOptions())
                                openFileOrFolder(os.path.join("Downloads", downloadOptions.folderName))
                                break
                            elif op not in ["no", "n"]:
                                break
                        break
                    elif op in alias["1playlist"]:
                        downloadOptions.isPlaylist = True
                        url = getPlaylistURL(alias)
                        if url:
                            pass #download
                        break
                    elif op in alias[">1playlist"]:
                        downloadOptions.isPlaylist = True
                        ## open text file
                        break
                    elif op in alias["back"]:
                        op = "1-1"
                        break
                    else:
                        print("Invalid option!")
            if op in "1-1":
                continue
            elif op in alias["back"]:
                break
            else: 
                print("Do you wish to exit? (y/n)")
                op = getOP().replace(" ", "")
                if op in ["y", "yes", alias["back"]]:
                    exit()