import spotipy

from spotipy.oauth2 import SpotifyOAuth
#                          ^ used when manipulating private user data

#applications ID and secret
clientID = '42109d4352944d808e428d27000d1735'
clientSecret = '93a71ecac90247ac9849c64a0300e012'

#limits the scope to accessing and modifying the user's library
scope = 'user-library-modify'

#necessary for setting up use of private user data
spotOAuth = SpotifyOAuth( \
    client_id='42109d4352944d808e428d27000d1735', \
    client_secret='93a71ecac90247ac9849c64a0300e012', \
    redirect_uri='http://localhost:8080/callback', \
    scope=scope \
)