I created a lyric generator user will give input as song name and artist name and will get output the lyrics of that song. 

REQUIREMENTS:
- lyricsgenius Python library (install via pip install lyricsgenius)
- Genius.com API access token

 FEATURES:

- Fetches lyrics from Genius.com using the Genius API.
- Simple and easy-to-use interface.

INSTALLATION:
  
1. Install the required dependencies:
    bash
    pip install lyricsgenius
    

2. Obtain a Genius API access token by signing up at [Genius](https://genius.com) and navigating to your API client management page.

SETUP:

1. Replace your_access_token_here with your actual Genius API access token in the script.







USAGE:
1. Import the necessary libraries and set up the Genius client:
    python
    import lyricsgenius

    genius = lyricsgenius.Genius("your_access_token_here")
    

2. Fetch lyrics by providing the song name and artist name:
    python
    song = genius.search_song("Song Name", "Artist Name")
    print(song.lyrics)

