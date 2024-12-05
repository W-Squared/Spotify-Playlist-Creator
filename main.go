package main

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"

	"github.com/w-squared/spotify-playlist-creator/xmapi"
)

var ClientID string = "0de55ab175f24766b03eb226b4296e15"
var ClientSecret string = "42aeafc85a944adc9ad64838932345ec"
var WilliamUserID string = "1mp6dza0t2vfx5dci1uvbx1xt"

func main() {
	fmt.Println(xmapi.CreateSpotifyIDData())
	//fmt.Println(GetAccessToken())
}

func GetAccessToken() (string, error) {
	var TokenURL string = "https://accounts.spotify.com/api/token"
	var authentication string = ClientID + ":" + ClientSecret
	var encodedAuthentication string = base64.StdEncoding.EncodeToString([]byte(authentication))
	fmt.Println(encodedAuthentication)

	request, err := http.NewRequest("POST", TokenURL, strings.NewReader("grant_type=client_credentials"))
	request.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	request.Header.Add("Authorization", "Basic"+encodedAuthentication)
	if err != nil {
		fmt.Println("Error while performing the request", err)
		os.Exit(1)
	}

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		fmt.Println("Error while performing the request", err)
		os.Exit(1)
	}

	defer response.Body.Close()
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("Error while reading the response body", err)
		os.Exit(1)
	}

	return string(body), nil
}
