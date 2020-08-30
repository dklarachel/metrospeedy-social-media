import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

# instagram credentials
IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")

# linkedin credentials
LI_EMAIL = os.environ.get("LI_EMAIL")
LI_PASSWORD = os.environ.get("LI_PASSWORD")

# twitter api credentials
TWITTER_KEY = os.environ.get("TWITTER_KEY")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")

