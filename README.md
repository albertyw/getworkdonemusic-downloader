getworkdonemusic-downloader
===========================

Script to download music from GetWorkDoneMusic.com

I did some code diving to get the list of music urls which I put 
into `GetWorkDoneMusic.py`.  `downloader.py` just downloads the 
urls in `GetWorkDoneMusic.py` and saves them.  Since lots of 
the song aren't directly downloadable, `downloader.py` uses 
the `soundcloud` package to download the songs.  You'll need 
to register as a developer on soundcloud to get an API key to 
download songs.  

Note: many of the songs' names (and therefore the file names) 
contain non-ASCII characters, which some music players (and 
file systems) don't like.  
