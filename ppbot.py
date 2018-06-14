import discord
import asyncio

client = discord.Client()


@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!dispo"):
        yield from client.delete_message(message)
    if message.content.startswith("!dispo"):
        message = yield from client.send_message(discord.Object(id='456515389741072386'), str(message.content)[6:])
        yield from client.add_reaction(message,'\u2705')
        yield from client.add_reaction(message,'\u274C')

@client.event
@asyncio.coroutine
def on_reaction_add(reaction,user):
    if "Dispos#9884" not in str(user):
        if str(reaction.emoji) == "✅":
            an="**"+str(user)+"** est disponible pour le match ! :smiley:"
            yield from client.send_message(discord.Object(id='456515271964753930'),an)

@client.event
@asyncio.coroutine
def on_voice_state_update(before,after):
    if before.voice_channel != after.voice_channel:
        if after.voice_channel.id == '456057790579081220':
            yield from client.send_message(discord.Object(id='456515271964753930'),"Besoin d'un admin")
        
@client.event
@asyncio.coroutine
def on_ready():  
    print("Ready")

client.run(TOKEN)
