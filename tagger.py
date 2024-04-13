import music_tag
import os

# Variables

LIBRARY_PATH = "F:\music\library"

ONLY_EDIT_THIS_FOLDER = "No Phun Intended"

# Code

def trim_ext(input):
    root, _ = os.path.splitext(input)
    return root

def get_artist_album(input):
    # windows specific dir structure...
    parts = input.split('\\')
    if len(parts) >= 3: 
        album = parts[-1]
        artist = parts[-2]
        return artist, album
    else:
        return None, None
    
def edit_metadata(song_path, title, artist, album):
    f = music_tag.load_file(song_path)
    f['title'] = title
    f['album'] = album
    f['artist'] = artist
    f.save()

def main():
    for root, folders, files in os.walk(LIBRARY_PATH):
        # print(f'Root = {root} \t folders = {folders} \t files = {files}')
        if len(files) != 0:
            artist, album = get_artist_album(root)
            for song in files:
                if song.endswith('.mp3') or song.endswith('.m4a'):
                    # Tis infact a song
                    song_title = trim_ext(song)
                    # We found a song we would like to edit its metadata
                    song_path = root + '\\' + song
                    if (album == ONLY_EDIT_THIS_FOLDER):
                        print(f"song = {song}")
                        edit_metadata(song_path, song_title, artist, album)





if os.path.exists(LIBRARY_PATH):
    main()
else:
    print("Path not found.")
