
# pyYoutubeToMp3

Simple way of converting multiple youtube videos/music URLs from a file, that user inputs the URL, to mp3.<br/>
It can only convert videos to .mp3

## Prerequisites

- Python 3.8.0

### Supported OS

-  [Windows 10](#windows-10)

#### Coming soon

- Linux (Ubuntu)

## Windows 10

### Installation
- Run/Open [Setup.bat](setup.bat)<br/>
If you didn't get any [error](#errors) you are ready to go!

### How to use

#### One or more music videos
- Input videos URL in **musicURLs.txt**, each line must contain only one URL<br/>
Example of a **musicURLs.txt** file:
``` 
> Give a new line for each URL (link example: https://www.youtube.com/watch?v=Dqq2wXW3X2Q) <
https://www.youtube.com/watch?v=sqG2wX2xEaX
https://www.youtube.com/watch?v=Azq2w3D3w2Q
https://www.youtube.com/watch?v=Dsq2wS26XxQ
```
- Make sure URLs are correct
- Run/Open [Run.bat](run.bat)<br/>
If you don't get any [error](#erros) check Mp3/ folder!

#### One playlist
- Run/Open [downloadPlaylist.bat](downloadPlaylist.bat)
- Input playlist url to the command prompt<br/>
If you don't get any [error](#erros) check SinglePlaylist/ folder!

#### More than one playlist
Coming soon...

## Errors
If you get any error, open an [issue](/../../issues)!

## Contributing
If you find that you have a better solution, new ideas, etc... just make a pull request!

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
