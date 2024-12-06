
from helpers import *

def main():
    PlayListUpdater = Updater()
    PlayListUpdater.updateALTPlaylist()
    PlayListUpdater.updateLithiumPlaylist()
    PlayListUpdater.updateDiploPlaylist()
    print("Playlists Updated")

if __name__ == "__main__":
    main()