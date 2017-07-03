from musixmatchclient import musixmatchclient
from musixmatch import API_KEY

client = musixmatchclient()
client.setAPIKey(API_KEY)
client.setTitle('Dangerous')
client.setArtist('Michael Jackson')
print (client.getLyrics())