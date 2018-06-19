import discord
import asyncio
import os

client = discord.Client()


@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == '456515271964753930':
        if message.content.startswith("!dispo"):
            yield from client.delete_message(message)
        if message.content.startswith("!dispo"):
            message = yield from client.send_message(discord.Object(id='456515389741072386'), str(message.content)[6:])
            yield from client.add_reaction(message,'\u2705')
            yield from client.add_reaction(message,'\u274C')
        if message.content.startswith("!clean"):
            yield from client.purge_from(discord.Object(id='456515389741072386'), limit=100, check=None, before=None, after=None, around=None)

@client.event
@asyncio.coroutine
def on_reaction_add(reaction,user):
    if reaction.message.channel.id == '456515389741072386':
        if "CCFN" in reaction.message.content:
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    an="**"+str(user)+"** est disponible pour le prochain CCFN ! :smiley:"
                    yield from client.send_message(discord.Object(id='456515271964753930'),an)
                    return
        if not "CCFN" in reaction.message.content:
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    an="**"+str(user)+"** est disponible pour le prochain event ! :smiley:"
                    yield from client.send_message(discord.Object(id='456515271964753930'),an)

@client.event
@asyncio.coroutine
def on_voice_state_update(before,after):
    if before.voice_channel != after.voice_channel:
        if after.voice_channel.id == '456057790579081220':
            yield from client.send_message(discord.Object(id='456515271964753930'),"Besoin d'un @Admin")
 
@client.event
@asyncio.coroutine
def on_ready():  
    print("Ready")

client.run(os.environ['TOKEN'])
