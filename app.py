from flask import Flask, jsonify
from helpers import *

app = Flask(__name__)

ALTPlaylistID = "4FNtubP22U9WRkitZzSpX3"
Shade45PlaylistID = "1KeYBRRe26f3NoKL2RUUvE"

@app.route('/playlistUpdater', methods=['GET'])
def update_playlists():
    PlayListDeDuper = DeDuper()
    PlayListUpdater = Updater()
    
    PlayListDeDuper.dedupePlaylist(ALTPlaylistID)
    PlayListUpdater.updateALTPlaylist()
    
    PlayListDeDuper.dedupePlaylist(Shade45PlaylistID)
    PlayListUpdater.updateShade45Playlist()
    
    return jsonify({"message": "Playlists Updated!"})

if __name__ == "__main__":
    app.run(debug=True)