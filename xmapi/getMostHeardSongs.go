package xmapi

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

type Song struct {
	ID      string `json:"id"`
	Plays   int    `json:"plays"`
	Spotify struct {
		SpotifyID  string `json:"spotify_id"`
		PreviewURL string `json:"preview_url"`
		Cover      string `json:"cover"`
	} `json:"spotify"`
	Track struct {
		ID        string    `json:"id"`
		Name      string    `json:"name"`
		Artists   []string  `json:"artists"`
		CreatedAt time.Time `json:"created_at"`
	} `json:"track"`
	Links []struct {
		URL  string `json:"url"`
		Site string `json:"site"`
	} `json:"links"`
}

type SpotifyInfo struct {
	Spotify struct {
		SpotifyID string `json:"spotify_id"`
	}
}

func GetMostHeardSongs() []Song {
	var baseURL string = "https://xmplaylist.com"
	var hitsOne string = "siriusxmhits1"
	var url string = baseURL + "/api/station/" + hitsOne + "/most-heard?subDays=30"
	var songs []Song

	response, err := http.Get(url)
	if err != nil {
		fmt.Println("Error while performing the request", err)
		os.Exit(1)
	}

	if response.StatusCode == 200 {
		body, readErr := io.ReadAll(response.Body)
		if readErr != nil {
			fmt.Println("Error while reading the response body", readErr)
			os.Exit(1)
		}

		unmarshalErr := json.Unmarshal(body, &songs)
		if unmarshalErr != nil {
			fmt.Println("Error while parsing the response body", unmarshalErr)
			os.Exit(1)
		}
	} else {
		fmt.Println("The request was not successful.")
		fmt.Println("Response status code:", response.StatusCode)
		os.Exit(1)
	}
	return songs
}

func GetSpotifyIDs(songs []Song) []string {
	ids := make([]string, len(songs))
	for i, SpotifyInfo := range songs {
		ids[i] = SpotifyInfo.Spotify.SpotifyID
	}
	return ids
}

func CreateSpotifyIDData() []string {
	songs := GetMostHeardSongs()
	ids := GetSpotifyIDs(songs)
	return ids
}
