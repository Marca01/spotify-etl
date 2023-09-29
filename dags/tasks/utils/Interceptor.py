import requests
import os
import dotenv
import time
import base64
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

dotenv.load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = 'https://developer.spotify.com/documentation/web-api/reference/get-recently-played'
scope = 'user-read-recently-played'
TOKEN = None
expiration_time = 0

# Create an auth manager with the scope parameter
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=redirect_uri,
                            scope=scope)

# Create a Spotify object with the auth manager
sp = spotipy.Spotify(auth_manager=auth_manager)

# def get_token():
#     global TOKEN, expiration_time
#
#     auth_string = CLIENT_ID + ":" + CLIENT_SECRET
#     auth_bytes = auth_string.encode('utf-8')
#     auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
#
#     data = requests.post("https://accounts.spotify.com/api/token",
#                           headers={
#                               "Authorization": f"Basic {auth_base64}",
#                               "Content-Type": "application/x-www-form-urlencoded"
#                           }, data={
#                               "grant_type": "client_credentials"
#                               # "client_id": CLIENT_ID,
#                               # "client_secret": CLIENT_SECRET
#                           }).json()
#     TOKEN = data['access_token']
#     expires_in = data['expires_in']
#     expiration_time = time.time() + expires_in
#     # return token
#
#
# # Define a custom interceptor class
# class CustomInterceptor(requests.Session):
#     # Override the send method
#     def send(self, request, **kwargs):
#         global TOKEN, expiration_time
#
#         # Add a custom header to the request
#         request.headers['Authorization'] = f'Bearer {TOKEN}'
#         # Send the request and get the response
#         response = super().send(request, **kwargs)
#
#         if time.time() > expiration_time or response.status_code == 401:
#             get_token()
#             print(time.time() > expiration_time, response.status_code, TOKEN)
#
#             # Update a custom header to the request
#             request.headers['Authorization'] = f'Bearer {TOKEN}'
#             response = super().send(request, **kwargs)
#
#         # Return the response
#         return response