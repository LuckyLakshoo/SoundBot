import os

from os.path import join, dirname, abspath
from dotenv import load_dotenv

# Directories
root = dirname(abspath(__file__))
MEDIA_DIR = join(root, "media")


# Envirionment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
try:
    BIN = os.getenv('FFMPEG')
except:
    BIN = None


# Strings
HELP_TEXT = {
    'total': 'Bruder ich joine deinem Channel und spiel nen sound ab'
} 