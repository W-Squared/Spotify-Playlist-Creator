import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


class SongFinder:
    def __init__(self, id=None, plays=None, spotify_id=None, preview_url=None, cover=None, track_id=None, name=None, artists=None, created_at=None, links=None):
        self.id = id
        self.plays = plays
        self.spotify_id = spotify_id
        self.preview_url = preview_url
        self.cover = cover
        self.track_id = track_id
        self.name = name
        self.artists = artists
        self.created_at = created_at
        self.links = links

    def ALTNationSongs(self):
        BaseXMURL = "https://xmplaylist.com"
        RadioStation = "altnation"
        url = f"{BaseXMURL}/api/station/{RadioStation}/most-heard?subDays=30"
        
        response = requests.get(url)
        if response.status_code != 200:
            print("The request was not successful.")
            print("Response status code:", response.status_code)
            exit(1)
        
        songs_data = response.json()
        songs = []
        for song_data in songs_data:
            if 'spotify' in song_data:
                song = SongFinder(
                    id=song_data['id'],
                    plays=song_data['plays'],
                    spotify_id=song_data['spotify']['spotify_id'],
                    preview_url=song_data['spotify']['preview_url'],
                    cover=song_data['spotify']['cover'],
                    track_id=song_data['track']['id'],
                    name=song_data['track']['name'],
                    artists=song_data['track']['artists'],
                    created_at=datetime.strptime(song_data['track']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    links=song_data['links']
                )
                songs.append(song)
        ids = ["spotify:track:" + song.spotify_id for song in songs]
        return ids

    def LithiumSongs(self):
        BaseXMURL = "https://xmplaylist.com"
        RadioStation = "lithium"
        url = f"{BaseXMURL}/api/station/{RadioStation}/most-heard?subDays=30"
        
        response = requests.get(url)
        if response.status_code != 200:
            print("The request was not successful.")
            print("Response status code:", response.status_code)
            exit(1)
        
        songs_data = response.json()
        songs = []
        for song_data in songs_data:
            if 'spotify' in song_data:
                song = SongFinder(
                    id=song_data['id'],
                    plays=song_data['plays'],
                    spotify_id=song_data['spotify']['spotify_id'],
                    preview_url=song_data['spotify']['preview_url'],
                    cover=song_data['spotify']['cover'],
                    track_id=song_data['track']['id'],
                    name=song_data['track']['name'],
                    artists=song_data['track']['artists'],
                    created_at=datetime.strptime(song_data['track']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    links=song_data['links']
                )
                songs.append(song)
        ids = ["spotify:track:" + song.spotify_id for song in songs]
        return ids

    def DiploSongs(self):
        BaseXMURL = "https://xmplaylist.com"
        RadioStation = "diplosrevolution"
        url = f"{BaseXMURL}/api/station/{RadioStation}/most-heard?subDays=30"
        
        response = requests.get(url)
        if response.status_code != 200:
            print("The request was not successful.")
            print("Response status code:", response.status_code)
            exit(1)
        
        songs_data = response.json()
        songs = []
        for song_data in songs_data:
            if 'spotify' in song_data:
                song = SongFinder(
                    id=song_data['id'],
                    plays=song_data['plays'],
                    spotify_id=song_data['spotify']['spotify_id'],
                    preview_url=song_data['spotify']['preview_url'],
                    cover=song_data['spotify']['cover'],
                    track_id=song_data['track']['id'],
                    name=song_data['track']['name'],
                    artists=song_data['track']['artists'],
                    created_at=datetime.strptime(song_data['track']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    links=song_data['links']
                )
                songs.append(song)
        ids = ["spotify:track:" + song.spotify_id for song in songs]
        return ids
    
    
class Updater:
    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="playlist-modify-public playlist-modify-private"
        ))
    
    def updateALTPlaylist(self):
        ALTPlaylistID = "4FNtubP22U9WRkitZzSpX3"
        Finder = SongFinder()
        Songs = Finder.ALTNationSongs()
        CurrentPlaylistsongs = self.GetCurrentPlaylistTracks(ALTPlaylistID)
        for Song in Songs:
            if Song and Song not in CurrentPlaylistsongs:
                self.spotify.playlist_add_items(ALTPlaylistID, [Song])
    
    def updateLithiumPlaylist(self):
        LithiumPlaylistID = "1PEM8ab7B0E48U7b2okX4t"
        Finder = SongFinder()
        Songs = Finder.LithiumSongs()
        CurrentPlaylistsongs = self.GetCurrentPlaylistTracks(LithiumPlaylistID)
        for Song in Songs:
            if Song and Song not in CurrentPlaylistsongs:
                self.spotify.playlist_add_items(LithiumPlaylistID, [Song])
                
    def updateDiploPlaylist(self):
        DiploPlaylistID = "59uEQlh3ORJTp2gOUET4mQ"
        Finder = SongFinder()
        Songs = Finder.DiploSongs()
        CurrentPlaylistsongs = self.GetCurrentPlaylistTracks(DiploPlaylistID)
        for Song in Songs:
            if Song and Song not in CurrentPlaylistsongs:
                self.spotify.playlist_add_items(DiploPlaylistID, [Song])
    
    def GetCurrentPlaylistTracks(self, playlist_id):
        tracks = []
        results = self.spotify.playlist_tracks(playlist_id)
        tracks.extend(results['items'])
        while results['next']:
            results = self.spotify.next(results)
            tracks.extend(results['items'])
        return [f"spotify:track:{track['track']['id']}" for track in tracks if track['track'] and track['track']['id']]
