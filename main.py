import discord
from discord.ext import commands
import youtube_dl
import asyncio
import time
import os
import heroku3



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="#", intents=intents, description="Bot de Gamaxi", help_command=None)


# évènement pour savoir si il est pret


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="#helpme", url='https://www.youtube.com/channel/UCSj1IUDv0vXdUhi4GDq5CAw'))
    print("Le bot est prêt")


# New member

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(789479498948149298)
    await channel.send(f"\U0001F609 Bienvenue dans GamaxHitkai {member.mention} \U0001F30C !")
    print("Une personne a rejoin le serveur !")
    '''
    verif_chan: discord.TextChannel = bot.get_channel(857967958315368468)
    await verif_chan.send("Salut ! J'aurai besoin que tu fasse un escape game avant d'entré dans se serveur \U0001F609 ! ")
    await verif_chan.send("2+2 c'est quoi selon toi ? indice: ||dans la description||")
    if 'poisson' in message.content:
        role = discord.utils.get(member.server.roles, name='pass')
        await bot.add_roles(member, role)
        await verif_chan.delete_messages(messages=verif_chan.history)
    else:
        await verif_chan.send("Incorrect ! Cherche encore")
    print(f"{member.display_name}, est venu ! :)")
    x = 120
    while x >= 0:
        x = x-1
        time.sleep(1)
    await verif_chan.send("Si tu n'y arrive pas à passer depuis 20min fais #help \U0001F609")
    '''
@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(789479498948149298)
    await channel.send(f"{member.mention} nous a quitté, j'éspère qu'on te reverra \U0001F622 ! ")
    print(f"{member.display_name}, est parti :(")



@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="**Erreur**", color=0x9C0000)
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061131_640.png")
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="**Il te manque un argument !**", value="Regarde bien ce que tu as écrit ! Si c'est pas un numéro qui manque !", inline=True)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed.add_field(name="**Tu n'as pas la permissions de le faire !**", value="Fais #helpme si tu ne sais les commandes que tu as le droit", inline=True)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        embed.add_field(name="**Cette commande n'éxiste pas !**", value="Pour savoir les commandes, fais #helpme", inline=True)
        await ctx.send(embed=embed)


@bot.event
async def on_raw_reaction_add(payload):
    global members
    message_id = payload.message_id
    if message_id == 870045547308937268:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        members = payload.member

        if payload.emoji.name == '\U0001F532':
            print('Une personne a réagit GD')
            role = discord.utils.get(guild.roles, name='Geometry Dash🟥')
        elif payload.emoji.name == '\U0001F30F':
            print('une personne a reagit MC')
            role = discord.utils.get(guild.roles, name='🌎Minecraft🌍')
        elif payload.emoji.name == '\U0001F697':
            print('une personne a réagit RL')
            role = discord.utils.get(guild.roles, name='🚘Rocket League🚗')
        elif payload.emoji.name == '\U0001F304':
            print("Une personne a réagit genshin impact !")
            role = discord.utils.get(guild.roles, name='🌄Genshin impact🌄')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await members.add_roles(role)

    if message_id == 870045568792150076:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        members = payload.member

        if payload.emoji.name == '\U0001F534':
            role = discord.utils.get(guild.roles, name='🎬YouTubeur/se🎥')
            print("Une personne est youtubeur/se !")
        elif payload.emoji.name == '\U0001F7E3':
            role = discord.utils.get(guild.roles, name='📷Streameur/se📡')
            print("Une personne est streameur/se !")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await members.add_roles(role)

    if message_id == 870045136644620288:

        members = payload.member
        if payload.emoji.name == '\U00002709':
            channel = bot.get_channel(798575028643561483)
            await channel.send(content=f"{members.display_name} a besoin d'un d'entre vous, faite vite !")
            return
        else:
            print("Il n'y a pas de réclamation")


@bot.event
async def on_raw_reaction_remove(payload):
    global Members
    message_id = payload.message_id
    if message_id == 870045547308937268:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        Members = await guild.fetch_member(payload.user_id)

        if payload.emoji.name == '\U0001F532':
            print('Une personne ne réagit plus réagit GD')
            role = discord.utils.get(guild.roles, name='Geometry Dash🟥')
        elif payload.emoji.name == '\U0001F30F':
            print('une personne ne réagit plus reagit MC')
            role = discord.utils.get(guild.roles, name='🌎Minecraft🌍')
        elif payload.emoji.name == '\U0001F697':
            print('une personne ne réagit plus réagit RL')
            role = discord.utils.get(guild.roles, name='🚘Rocket League🚗')
        elif payload.emoji.name == '\U0001F304':
            print("Une personne ne réagit plus réagit genshin impact !")
            role = discord.utils.get(guild.roles, name='🌄Genshin impact🌄')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if Members is not None:
            await Members.remove_roles(role)
        else:
            print("Member is not found")

    if message_id == 870045568792150076:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        Members = await guild.fetch_member(payload.user_id)

        if payload.emoji.name == '\U0001F534':
            role = discord.utils.get(guild.roles, name='🎬YouTubeur/se🎥')
            print("Une personne n'est finalement pas Youtubeur/se")
        elif payload.emoji.name == '\U0001F7E3':
            role = discord.utils.get(guild.roles, name='📷Streameur/se📡')
            print("Une personne n'est finalement pas streameur/se")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if Members is not None:
            await Members.remove_roles(role)
        else:
            print("Member is not found")



# commande pour le bot

@bot.command()
async def credit(ctx):
    Gamaxi = bot.get_user(734874277798739979)
    embed = discord.Embed(title="**Crédit**", url='https://www.youtube.com/channel/UCSj1IUDv0vXdUhi4GDq5CAw', color=0x7BCFFF)
    embed.add_field(name="**Développeur :**", value=Gamaxi.mention, inline=False)
    embed.add_field(name="**Version du Bot**", value="1", inline=True)
    embed.set_footer(text="By gamaxi Gayou® in 2021")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    member = ctx.author
    channelmodo = bot.get_channel(798575028643561483)
    await channelmodo.send(f"{member.mention} a besoin qu'on l'aide dans le channel vérification !")
    await ctx.send("Vous avez appelé a l'aide, un staff du serveur va arriver !")

@bot.command()
async def sondage(ctx, *, mess=None):
    mess = "".join(mess)
    embed = discord.Embed(title="**Sondage**", description=mess, color=discord.Colour.random())
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('\U00002705')
    await msg.add_reaction('\U0000274C')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def autodestruction(ctx):
    x = 6
    while x > 0:
        x = x-1
        time.sleep(1)
        await ctx.send(x)
    await ctx.send("Bot désactiv")
    for loop in range(5):
        await ctx.send("ééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééé")
        embed = discord.Embed(title="**ERROR SYSTEM**", color=discord.Colour.random())
        await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(manage_messages=True)
async def support(ctx):
    embed = discord.Embed(title="**Report**", description="Vous avez trouvé un bug, ou vous trouvez quelques choses d'anormal ?", color=0x0FFF00)
    embed.set_footer(text="Si vous avez besoin d'un STAFF du serveur cliquez sur cette réaction, en revanche si c'est inutile vous aurez une sanction !")
    ms = await ctx.send(embed=embed)
    emojie = "\U00002709"
    await ms.add_reaction(emojie)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def sup(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()
    print("Un membre a supprimé des messages !")


@bot.command()
async def yt(ctx):
    embed = discord.Embed(title="**Nos chaînes YouTube !**", color=0xFF0000)
    embed.add_field(name="Voici la chaîne youtube de Hitkai :",
                    value="*https://www.youtube.com/channel/UCFEih30KWHqcERHKLwYSKYQ*", inline=True)
    embed.add_field(name="Voici celle de Gamaxi :", value="*https://www.youtube.com/channel/UCSj1IUDv0vXdUhi4GDq5CAw*",
                    inline=True)
    await ctx.send(embed=embed)
    print("Un membre veux savoir notre chaîne !")


@bot.command()
@commands.has_role("Co-Fondateur")
async def rolre2(ctx):
    embed = discord.Embed(title="**Rôle en plus !**", description="Choisi le/les rôles que tu es !", color=0x0700FF)
    embed.add_field(name="\U0001F7E3", value="= Tu es streameur/se", inline=True)
    embed.add_field(name="\U0001F534", value="= Tu es youtubeur/se", inline=True)
    emoji2 = '\U0001F534'
    emoji1 = '\U0001F7E3'

    message = await ctx.send(embed=embed)
    await message.add_reaction(emoji1)
    await message.add_reaction(emoji2)


@bot.command()
@commands.has_role("Co-Fondateur")
async def rolre(ctx):
    embed = discord.Embed(title="**Rôle**", description="Choisi le/les rôles auquel tu joue !", color=0x0600CD)
    embed.add_field(name="\U0001F532", value="= Tu joue à Geometry Dash", inline=True)
    embed.add_field(name="\U0001F697", value="= Tu joue à Rocket League", inline=True)
    embed.add_field(name="\U0001F304", value="= Tu joue à Genshin Impact", inline=True)
    embed.add_field(name="\U0001F30F", value="= Tu joue à Minecraft", inline=True)
    emoji2 = '\U0001F532'
    emoji1 = '\U0001F30F'
    emoji3 = '\U0001F697'
    emoji4 = '\U0001F304'
    message = await ctx.send(embed=embed)
    await message.add_reaction(emoji1)
    await message.add_reaction(emoji2)
    await message.add_reaction(emoji3)
    await message.add_reaction(emoji4)


@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="**Besoin d'aide ?**", description="Voici les commandes qui pourront être utile !:",
                          color=0xAE00FF)
    embed.set_thumbnail(url="https://images.emojiterra.com/google/android-pie/512px/1f44d.png")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="#yt", value="Savoir nos chaînes yt", inline=True)
    embed.add_field(name="#play {url}", value="Mettre un son", inline=True)
    embed.add_field(name="#paused", value="Mettre en pause le son", inline=True)
    embed.add_field(name="#resume", value="Reprendre le son", inline=True)
    embed.add_field(name="#skip", value="Passé au prochain son de la queue", inline=True)
    embed.add_field(name="#leave", value="Le bot quitte le vocal", inline=True)
    embed.add_field(name="#credit", value="Les crédits du bot !", inline=True)
    embed.add_field(name="#sondage {text}", value="Vous pouvez mettre un sondage !(à utiliser dans le salon sondage)", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def helpmemodo(ctx):
    embed = discord.Embed(title="**Besoin d'aide les modos ?**", description="Voici les commandes qui pourront être utile pour vous !:",
                          color=0xFF00F7)
    embed.set_thumbnail(url="https://images.emojiterra.com/google/android-pie/512px/1f44d.png")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="#sup {numéro}", value="Supprime le nombres de message que vous avez dit", inline=True)
    embed.add_field(name="#kick {user}", value="Expulser un membre", inline=True)
    embed.add_field(name="#ban {user}", value="Bannir un membre", inline=True)
    embed.add_field(name="#unban", value="Déban un membre", inline=True)
    embed.add_field(name="#warn", value="Met un avertissement à un membre", inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, member: discord.User):
    await ctx.guild.unban(member, reason=reason)
    embed = discord.Embed(title="**UNBAN**", description=f"Le membre {member.display_name} a été déban !", color=0x42FF00)
    embed.add_field(name="ID", value=member.id, inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.User, *, reason=None):
    reason = ''.join(reason)
    await ctx.guild.ban(member, reason=reason)
    embed = discord.Embed(title="**BAN**", description=f"Le membre {member.display_name} a été ban !", color=0xFF3600)
    embed.set_thumbnail(url="https://www.pngall.com/wp-content/uploads/5/Banned-PNG-Free-Download.png")
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="*Raison :*", value=reason, inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.User, *, reason=None):
    reason = ''.join(reason)
    await ctx.guild.kick(member, reason=reason)
    embed = discord.Embed(title="**Kick**", color=0xFBFF00)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/PublicInformationSymbol_EmergencyExit.svg/2048px-PublicInformationSymbol_EmergencyExit.svg.png")
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_footer(text=f"Le membre {member.display_name} a été kick !", icon_url=ctx.member.avatar_url)
    await ctx.send(embed=embed)

warnings = {}
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user: discord.User, *, reason=None):
    reason = ''.join(reason)
    Id = user.id
    if Id not in warnings:
        warnings[Id] = 0
        print("La personne n'a aucun avertissement !")

    warnings[Id] += 1

    if warnings[Id] == 3:
        warnings[Id] = 0
        await user.send("Désolé de te le dire, mais tu as eu trop d'avertissement sur le serveur donc tu as été éjecté du serveur !")
        await ctx.guild.kick(user, reason=reason)

    embed = discord.Embed(title="**Warn**", description=f"L'utilisateur {user} a été warn !", color=0xFF8700)
    embed.set_thumbnail(url="https://findicons.com/files/icons/1008/quiet/256/attention.png")
    embed.add_field(name="*Raison :*", value=reason, inline=True)
    embed.add_field(name="ID", value=Id, inline=True)
    embed.add_field(name="Warn", value=warnings[Id], inline=True)
    await ctx.send(embed=embed)


# Musique et commande

music = {}
ytdl = youtube_dl.YoutubeDL()


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]
        self.title = video['title']
        self.duration = video['duration']
        self.thumbnail = video['thumbnail']
        return


def play_song(clients, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url,
                                                                 before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(clients, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(clients.disconnect(), bot.loop)

    clients.play(source, after=next)


@bot.command()
async def skip(ctx):
    clients = ctx.guild.voice_client
    clients.stop()


@bot.command()
async def paused(ctx):
    client_p = ctx.guild.voice_client
    if not client_p.is_paused():
        client_p.pause()


@bot.command()
async def resume(ctx):
    client_p = ctx.guild.voice_client
    if client_p.is_paused():
        client_p.resume()


@bot.command()
async def leave(ctx):
    client_p = ctx.guild.voice_client
    await client_p.disconnect()
    music[ctx.guild] = []


@bot.command()
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send(" {} Vous devez vous connectez a un salon vocal !".format("<:no_entry:862022003639713892>"))
        return
    else:
        clients = ctx.guild.voice_client

        if clients and clients.channel:
            video = Video(url)
            music[ctx.guild].append(video)
        else:
            channels = ctx.message.author.voice.channel
            video = Video(url)
            music[ctx.guild] = []
            clients = await channels.connect()
            embed = discord.Embed(title="**Je met cette vidéo !**", color=0xFF0000, url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=video.thumbnail)
            embed.add_field(name="Titre :", value=video.title, inline=True)
            embed.add_field(name="Durée :", value=f"{video.duration}s", inline=True)
            await ctx.send(embed=embed)
            play_song(clients, music[ctx.guild], video)


# _________________________________________________________________________________


config["authorization_strings"] = data
    config["heroku_api_token"] = key
    if api_token is not None:
        config["api_id"] = api_token.ID
def get_app(authorization_strings, key, api_token=None, create_new=True, full_match=False):
    heroku = heroku3.from_key(key)
    app = None

