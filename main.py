import os
import time

import discord
from dotenv import load_dotenv
import random

load_dotenv()

random.seed(12749012743)
client = discord.Client()
dir_path = os.getcwd()

audio_dir = {
    0: 'akkurat',
    1: 'cringe',
    2: 'digga',
    3: 'geringverdiener',
    4: 'mittwoch',
    5: 'pappatastisch',
    6: 'same',
    7: 'sheesh',
    8: 'sus',
    9: 'wild'
}


@client.event
async def on_ready():
    print(f'{client.user} has connected')
    print(client.guilds)


@client.event
async def on_voice_state_update(member, before, after):
    print(member)

    if member != client.user:
        if after.channel is not None and before.channel is None and len(after.channel.members) == 1:  # if the user is not the bot and someone connects to the channel it plays a sound
            time.sleep(1)
            voiceclient = await after.channel.connect()  # wait x amount of seconds so it randomize joins
            speakrandom(voiceclient)

        if after.channel is not None:
            print(after.channel)

        if before.channel is not None:
            if len(before.channel.members) == 1:
                print(client.voice_clients)


def speakrandom(voiceclient):
    time.sleep(2)  # wait 2 seconds so everybody is confest
    audio = audio_dir.get(random.randint(0, 9))  # get one of the audios (spezified in the audio dictionary)
    print(audio)
    voiceclient.play(discord.FFmpegPCMAudio(dir_path + fr'\\audio\\{audio}.mp3'))  # play sound


client.run(os.getenv("DISCORD_TOKEN"))
