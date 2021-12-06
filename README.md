# Spotify-Downloader-GUI
This Program helps you download songs from the Spotify track's link you give in. <br>
It uses yt-dlp to download songs from Youtube.

# What it does
  * It gets the link from the user<br>
  * Scraps the Webpage and gets the song's title from Spotify<br>
  * Then the title is used the get the youtube video's link
  * Now the link is passed in to yt-dlp and the track will be downloaded to the selected path


# Requirements
  * [yt-dlp](https://pypi.org/project/yt-dlp/)  
  * [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  * [Pillow ](https://pypi.org/project/Pillow/)
  * [requests](https://pypi.org/project/requests/)  
  * Tkinter
  * ffmpeg(Place Binary file inside where the script is present)
