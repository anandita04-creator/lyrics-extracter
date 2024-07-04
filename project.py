import lyricsgenius

genius = lyricsgenius.Genius("yEfXPS27EiIekPhNjoiIFQBhjqxd8_tmcvhzGSSeCm-6uNSiXH7Gc2mRRjLB05do")

music=input("Enter song name :")
artist=input("Enter artist name :")

song = genius.search_song(music,artist="")

with open('lyrics.txt', "w", encoding='utf-8') as f:
    f.write(song.lyrics)