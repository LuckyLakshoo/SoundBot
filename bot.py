import os
import random
import discord

from discord import FFmpegPCMAudio
from discord.ext import commands
from dotenv import load_dotenv
from pytube import YouTube

from constants import MEDIA_DIR, TOKEN, BIN, HELP_TEXT


def download_yt(url):
    yt = YouTube(url)
    title = yt.title
    stream = yt.streams.filter(only_audio=True)[-1]
    stream.download(MEDIA_DIR, filename=title)


def get_sounds(sound):
    ''' 
    Collects audio data of sound
    
    Params:
        sound: reference to audio data
    '''
    pass


bot = commands.Bot(command_prefix='!')

@bot.command(name='total', help=HELP_TEXT['total'])
async def play_sound(ctx, number: int):
    '''
    Bot joins channel of message author and plays SOUND[number] via voice
    
    Params:
        number: index of song to be played
    '''
    
    # join channel of author
    print("comman receiver: ", number)
    connected = ctx.author.voice
    if connected:
        vc = await connected.channel.connect()
        print("connected to channel: ", connected.channel.name)
        
        try:
            fpath = os.path.join(MEDIA_DIR, os.listdir(MEDIA_DIR)[number])
            vc.play(FFmpegPCMAudio(fpath), after=None)
        except Exception as e:
            raise discord.DiscordException 
    pass


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=Gy6xJQSgOu4'
    download_yt(url)
    print('running bot')
    bot.run(TOKEN)
