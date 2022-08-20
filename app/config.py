from pydantic import BaseSettings
import os

class Settings():
    happy_playlist_id:str = os.getenv("HAPPY_PLAYLIST_ID", "75OwbDQ46OhGxa94S9QeSP")
    sad_playlist_id:str = os.getenv("SAD_PLAYLIST_ID", "1DuKY4VTzPZr1rm56yJBBY")
    neutral_playlist_id:str = os.getenv("NEUTRAL_PLAYLIST_ID", "5modmNyv0c2lxwHO7J0S6Q")
    client_id:str = os.getenv("CLIENT_ID", "2c115b5e727e407d9a7143ee54906b4e")
    client_secret:str = os.getenv("CLIENT_SECRET", "2734918e6d9647bdb4222fa545da2088")
    base_url:str = os.getenv("BASE_URL", "http://localhost:8000")

settings = Settings()
