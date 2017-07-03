import requests

class musixmatchclient:
    apikey = ''
    title = ''
    artist = ''

    @classmethod
    def setAPIKey(self,key):
        self.apikey = key

    @classmethod
    def setTitle(self,t):
        self.title = t
    
    @classmethod
    def setArtist(self,a):
        self.artist = a

    @classmethod
    def getLyrics(self):
        url = "http://api.musixmatch.com/ws/1.1/matcher.lyrics.get"
        querystring = {
            "q_track" : self.title,
            "q_artist" : self.artist,
            "apikey" : self.apikey
        }

        headers = {
            'content-type' : 'application/json'
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return (response.text)