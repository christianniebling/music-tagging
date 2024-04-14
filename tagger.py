import music_tag
import os

# Variables

LIBRARY_PATH = "F:\music\library"
OVERWRITE_TAGS = False

# Optional

ONLY_EDIT_THIS_ALBUM = ""

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

    if OVERWRITE_TAGS or not f.get('title'):
        f['title'] = title

    if OVERWRITE_TAGS or not f.get('album'):
        f['album'] = album

    if OVERWRITE_TAGS or not f.get('artist'):
        f['artist'] = artist
    
    f.save()
    print(f'Tagged: \t"{title}"')

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
                    edit_metadata(song_path, song_title, artist, album)
                    if (ONLY_EDIT_THIS_ALBUM == ""):
                        edit_metadata(song_path, song_title, artist, album)
                    else:
                        if (album == ONLY_EDIT_THIS_ALBUM):
                            edit_metadata(song_path, song_title, artist, album)

if __name__ == "__main__":
    if os.path.exists(LIBRARY_PATH):
        main()
    else:
        print("Path not found.")
