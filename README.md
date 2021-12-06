# Spotify-Downloader-GUI
This Program helps you download songs from the Spotify track's link you give in. <br>
It uses yt-dlp to download songs from Youtube.<br>

# What it does
  * It gets the link from the user<br>
  * Scraps the Webpage and gets the song's title from Spotify<br>
  * Then the title is used the get the youtube video's link
  * Now the link is passed in to yt-dlp and the track will be downloaded to the selected path
  * Atlast the downloaded file is converted into mp3 using ffmpeg

# Requirements
  * [yt-dlp](https://pypi.org/project/yt-dlp/)  
  * [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  * [Pillow ](https://pypi.org/project/Pillow/)
  * [requests](https://pypi.org/project/requests/)  
  * Tkinter
  * [ffmpeg](https://ffmpeg.org/download.html) (Place the Binary file inside the project's folder)

# Note:
 * It is not a complete project, it is still under development
 * It may be buggy at some point
 * You can only use keyboard shortcuts to copy and paste the link inside the entry box.
 * It may stop responding, though it will complete the download without any problem. Wait till then (This is because of running the whole program on the main thread, I am working on it)
 
