import os
import random
import discord

from discord import FFmpegPCMAudio
from discord.ext import commands
from dotenv import load_dotenv
from pytube import YouTube

from constants import MEDIA_DIR, TOKEN, BIN, HELP_TEXT, FNAME

def download_yt(url):
    yt = YouTube(url)
    fname = yt.title
    stream = yt.streams.filter(only_audio=True)[-1]
    stream.download(MEDIA_DIR, filename=fname)


bot = commands.Bot(command_prefix='!')

@bot.command( name='total', help=HELP_TEXT['total'] )
async def play_sound(ctx, number: int):
    '''
    Bot joins channel of message author and plays SOUND[number] via voice

    Params:
        number: index of song to be played
    '''

    # join channel of author
    connected = ctx.author.voice
    if connected:
        vc = await connected.channel.connect()
        print('connected to channel: ', connected.channel.name)
        try:
            fname = os.path.join(MEDIA_DIR, os.listdir(MEDIA_DIR)[number])
            vc.play(FFmpegPCMAudio(fname), after=None)
        except Exception as e:
            raise discord.DiscordException
    pass


@bot.command( name='dl', help=HELP_TEXT['dl'] )
async def update(ctx, url: str):
    '''Downloads given url'''
    print('Download ', url)
    download_yt(url)


@bot.command( name='show', help=HELP_TEXT['show'])
async def show(ctx):
    '''Display list of available sounds'''
    sounds = os.listdir(MEDIA_DIR)
    msg = 'Available sounds:'
    for i, fname in enumerate(sounds):
        name = fname.split('.')[0]
        msg += f'\n{i}.\t {name}'
    await ctx.send(msg)


if __name__ == '__main__':
    print('running bot')
    bot.run(TOKEN)
