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
            message = yield from client.send_message(discord.Object(id='456515389741072386'), "**"+str(message.content)[6:]+"**")
            yield from client.add_reaction(message,'\u2705')
            yield from client.add_reaction(message,'\u274C')
        if message.content.startswith("!clean"):
            yield from client.delete_message(message)
            yield from client.purge_from(discord.Object(id='456515389741072386'), limit=100, check=None, before=None, after=None, around=None)
            an="**"+str(message.author)+"** a nettoyé le channel préparation-ccfn \U0001F5D1"
            yield from client.send_message(discord.Object(id='456515271964753930'),an)

@client.event
@asyncio.coroutine
def on_reaction_add(reaction,user):
    if reaction.message.channel.id == '456515389741072386':
        if "[P²]#4011" not in str(user):
            if str(reaction.emoji) == "✅":
                if str(user) not in reaction.message.content:
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content+"\n-"+str(user)+" in")

@client.event
@asyncio.coroutine
def on_reaction_remove(reaction, user):
    if reaction.message.channel.id == '456515389741072386':
        if "[P²]#4011" not in str(user):
            if str(reaction.emoji) == "✅":
                if "\n-"+str(user)+" in" in reaction.message.content:
                    lol = reaction.message.content
                    an = lol.replace("\n-"+str(user)+" in", " ")
                    yield from client.edit_message(reaction.message, new_content=an)
@client.event
@asyncio.coroutine
def on_voice_state_update(before,after):
    if before.voice_channel != after.voice_channel:
        if after.voice_channel.id == '456057790579081220':
            yield from client.send_message(discord.Object(id='456515271964753930'),"**"+str(after)+"** a besoin d'un @Admin \U0001F198")
 
@client.event
@asyncio.coroutine
def on_ready():  
    print("Ready")

client.run(os.environ['TOKEN'])
