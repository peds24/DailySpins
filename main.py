import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


# Load environment variables from .env file
load_dotenv()

# Replace these with your app's credentials
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# Scope defines what permissions you are requesting
SCOPE = 'user-library-read'

# Authenticate and get access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Example: Get the current user's saved tracks
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")
