import discord
import asyncio
import os

client = discord.Client()


@client.event
@asyncio.coroutine
async def fetch_logs(channel):
    List = []
    async for log in client.logs_from(channel,limit=500):
        List.append(log)
    return List

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == '441518062575943680':
        if message.content.startswith("!dispo"):
            yield from client.delete_message(message)
            message = yield from client.send_message(discord.Object(id='443359172470374400'), str(message.content)[6:]+"\n\nLes présents sont :")
            yield from client.add_reaction(message,'\u2705')
            yield from client.add_reaction(message,'\u274C')
        if message.content.startswith("!last"):
            yield from client.delete_message(message)
            message = yield from client.send_message(discord.Object(id='484640273960402951'), str(message.content)[6:]+"\n\nLes présents sont :")
            yield from client.add_reaction(message,'\u2705')
            yield from client.add_reaction(message,'\u274C')
        if message.content.startswith("!msg"):
            for r in message.channel_mentions:
                yield from client.send_message(r, message.content[26:])
        if message.content.startswith("!clean"):
            yield from client.delete_message(message)
            yield from client.purge_from(discord.Object(id='443906036701855757'), limit=100, check=None, before=None, after=None, around=None)
            an="<@"+str(message.author.id)+"> a nettoyé le channel préparation-ccfn \U0001F5D1"
            yield from client.send_message(discord.Object(id='441518062575943680'),an)
        if message.content.startswith("!vote"):
            Nb = 0
            for x in client.get_all_members():
                for r in x.roles:
                    if r.name == 'Membres':
                        Nb = Nb+1
                    if r.name == 'Ancien':
                        Nb = Nb+1
                    if r.name == 'Admin':
                        Nb = Nb+1
            yield from client.delete_message(message)
            message = yield from client.send_message(discord.Object(id='442578879673270283'), str(message.content)[6:]+"\n\nRésultats :\n000 | 000 | 000 sur un total de "+str(Nb).zfill(3)+" voix")
            yield from client.add_reaction(message,'\u2705')
            yield from client.add_reaction(message,'\u274C')
            yield from client.add_reaction(message,'\U0001F910')
            

@client.event
@asyncio.coroutine
def on_reaction_add(reaction,user):
    if reaction.message.channel.id == '443359172470374400':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    if str(user) not in reaction.message.content:
                        yield from client.edit_message(reaction.message, new_content=reaction.message.content+"\n-<@"+str(user.id)+">")
    if reaction.message.channel.id == '484640273960402951':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    if str(user) not in reaction.message.content:
                        yield from client.edit_message(reaction.message, new_content=reaction.message.content+"\n-<@"+str(user.id)+">")                    
    if reaction.message.channel.id == '442578879673270283':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    ok = int(reaction.message.content[-40:-37])
                    ak = int(reaction.message.content[-8:-5])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok+1
                        if r.name == 'Ancien':
                            ok = ok+1
                        if r.name == 'Admin':
                            ok = ok+1
                    if ok > ak/2 and ok <= ak/2 + 3:
                        yield from client.send_message(discord.Object(id='441518062575943680'),"**Une majorité a été obtenue** \u270C")
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-40]+str(ok).zfill(3)+reaction.message.content[-37:])
                if str(reaction.emoji) == "\u274C":
                    ok = int(reaction.message.content[-34:-31])
                    ak = int(reaction.message.content[-8:-5])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok+1
                        if r.name == 'Ancien':
                            ok = ok+1
                        if r.name == 'Admin':
                            ok = ok+1
                    if ok > ak/2 and ok <= ak/2 + 3:
                        yield from client.send_message(discord.Object(id='441518062575943680'),"**Une majorité a été obtenue** \U0001F44E")
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-34]+str(ok).zfill(3)+reaction.message.content[-31:])
                if str(reaction.emoji) == "\U0001F910":
                    ok = int(reaction.message.content[-28:-25])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok+1
                        if r.name == 'Ancien':
                            ok = ok+1
                        if r.name == 'Admin':
                            ok = ok+1
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-28]+str(ok).zfill(3)+reaction.message.content[-25:])

@client.event
@asyncio.coroutine
def on_reaction_remove(reaction, user):
    if reaction.message.channel.id == '443359172470374400':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    if "\n-<@"+str(user.id)+">" in reaction.message.content:
                        lol = reaction.message.content
                        an = lol.replace("\n-<@"+str(user.id)+">", " ")
                        yield from client.edit_message(reaction.message, new_content=an)
    if reaction.message.channel.id == '484640273960402951':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    if "\n-<@"+str(user.id)+">" in reaction.message.content:
                        lol = reaction.message.content
                        an = lol.replace("\n-<@"+str(user.id)+">", " ")
                        yield from client.edit_message(reaction.message, new_content=an)                    
    if reaction.message.channel.id == '442578879673270283':
        if reaction.message.author.id == "458596694796402700":
            if "[P²]#4011" not in str(user):
                if str(reaction.emoji) == "✅":
                    ok = int(reaction.message.content[-40:-37])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok-1
                        if r.name == 'Ancien':
                            ok = ok-1
                        if r.name == 'Admin':
                            ok = ok-1
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-40]+str(ok).zfill(3)+reaction.message.content[-37:])
                if str(reaction.emoji) == "\u274C":
                    ok = int(reaction.message.content[-34:-31])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok-1
                        if r.name == 'Ancien':
                            ok = ok-1
                        if r.name == 'Admin':
                            ok = ok-1
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-34]+str(ok).zfill(3)+reaction.message.content[-31:])
                if str(reaction.emoji) == "\U0001F910":
                    ok = int(reaction.message.content[-28:-25])
                    for r in user.roles:
                        if r.name == 'Membres':
                            ok = ok-1
                        if r.name == 'Ancien':
                            ok = ok-1
                        if r.name == 'Admin':
                            ok = ok-1
                    yield from client.edit_message(reaction.message, new_content=reaction.message.content[:-28]+str(ok).zfill(3)+reaction.message.content[-25:])

@client.event
@asyncio.coroutine
def on_voice_state_update(before,after):
    if before.voice_channel != after.voice_channel:
        if after.voice_channel.id == '436860873882075151':
            yield from client.send_message(discord.Object(id='441518062575943680'),"<@"+str(after.id)+"> a besoin d'un <@&440560633696616459> \U0001F198")


@client.event
@asyncio.coroutine
def on_ready():
    old1 = yield from client.fetch_logs(discord.Object(id='443359172470374400'))
    for x in old1:
        client.messages.append(x)
    old2 = yield from client.fetch_logs(discord.Object(id='442578879673270283'))
    for x in old2:
        client.messages.append(x)
    print("Ready")

client.run(os.environ['TOKEN'])
