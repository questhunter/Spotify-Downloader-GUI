![Annotation 2021-12-06 133807](https://user-images.githubusercontent.com/74132905/144810108-ea6af3f3-9d7b-48c2-8ce5-945d77cf2def.png)

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

 
