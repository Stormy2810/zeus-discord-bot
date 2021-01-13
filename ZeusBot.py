import discord
import os
import shutil
from os import system
from discord.ext import commands
from discord.utils import get
import random
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import json
import requests
import aiohttp
from aiohttp import ClientSession
from datetime import datetime
from discord import TextChannel
import time
from itertools import cycle
import urllib
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix = '?')
status = cycle(['name=f"{len(client.users)} Users', 'name=f"Zeus Bot | ?help'])


bot.remove_command('help')
bot.launch_time = datetime.utcnow()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f"Zeus Bot ⚡ ?help"))
    print('Zeus is ready and online!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(color=0x004c86, title=f"**Command Not Found!**",
                              description=f"``Please use this Command {ctx.prefix}help``")
        await ctx.send(embed=embed)

@bot.command()
async def links(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**Bot Invite**",
                     value=f"**[Invite](https://stormy2810.wixsite.com/zeusdiscordbot)**")
    embed4.add_field(name=f"**Friend's Bot**",
                     value=f"**[Revenge Bot](https://discord.com/oauth2/authorize?client_id=704452467995312139&permissions=8&scope=bot)**")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def help(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**Fun**",
                     value=f"?fun")
    embed4.add_field(name=f"**Other**",
                     value=f"?other")
    embed4.add_field(name=f"**Mod**",
                     value=f"?mod")
    embed4.add_field(name=f"**NSFW**",
                     value=f"?nsfw")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def fun(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**Fun Commands (12)**",
                     value=f"8ball, hack, hug, smug, pat, flipcoin, trapcard, meme, slap, karate, punch, tickle, avatar, shrekislove, tweet, slot, dick")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def other(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**Other Commands (4)**",
                     value=f"ping, ip, links, say")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def mod(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**Mod Commands (7)**",
                     value=f"ban, unban, kick, clear, lock, unlock, announce")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def nsfw(ctx):
    embed4 = discord.Embed(color=0x004c86, timestamp=ctx.message.created_at)
    embed4.add_field(name=f"**NSFW Commands (5)**",
                     value=f"pussy, lesbian, boobs, hentai, kiss")
    embed4.set_footer(text="Zeus Bot")
    embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/752930568051622008/753828194141863936/AnyConv.com__ZeusNonGif.jpeg')
    await ctx.send(embed = embed4)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain dumbass.',
                 'It is decidedly so fellow retard.',
                 'Without a doubt cunt.',
                 'Yes - definitely.',
                 'You may reply on it, lazy whore.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again',
                 'Ask again later, when ur taller then 5ft.',
                 'Better not tell you now.',
                 'Cannot predict it now, im fuckin ur mom.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My Reply is no.',
                 'My sources(google) say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def ip(ctx, *, ipaddr: str = '1.3.3.7'):

    await ctx.send(f"HEHEHE I'll find them.")

    await asyncio.sleep(3)

    r = requests.get(f'https://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    country = geo['countryCode']
    embed = discord.Embed(color=0x004c86, title=f"IP Lookup.", timestamp=ctx.message.created_at)
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'IP Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']}
    ]

    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
            embed.set_thumbnail(url=f"https://www.countryflags.io/{country}/flat/64.png")
            embed.set_footer(text=f"Zues Bot")
    return await ctx.send(embed=embed)

@bot.command()
async def flipcoin(ctx, *, question):
    responses = ['heads',
                'tails']
    await ctx.send('https://media.giphy.com/media/a8TIlyVS7JixO/giphy.gif')
    await asyncio.sleep(3)
    await ctx.send(f'Heads Or Tails?: {question}\nLanded: {random.choice(responses)}')

@flipcoin.error
async def flipcoin_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}flipcoin <answer>``")
        await ctx.send(embed=embed)

@bot.command()
async def murder(ctx, member : discord.Member):
    await ctx.send("The Fuck you say about my Momma?")
    await asyncio.sleep(1)
    await ctx.send('https://media.giphy.com/media/T6erVmXL956DK/giphy.gif')

@murder.error
async def murder_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}punch <user>``")
        await ctx.send(embed=embed)


@bot.command()
async def punch(ctx, member: discord.Member):
    await ctx.send("The Fuck you say bitch!")
    await asyncio.sleep(2)
    await ctx.send('https://media.giphy.com/media/3oEhn4mIrTuCf0bn1u/giphy.gif')

@punch.error
async def punch_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}punch <user>``")
        await ctx.send(embed=embed)

@bot.command()
async def karate(ctx, member: discord.Member):
    await ctx.send("Karate kick y'all ass Cunt!")
    await asyncio.sleep(2)
    await ctx.send('https://media.giphy.com/media/5jQ2FIhtc3M88/giphy.gif')

@karate.error
async def karate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}karate <user>``")
        await ctx.send(embed=embed)

@bot.command()
async def trapcard(ctx, member: discord.Member):
    await ctx.send('https://media.giphy.com/media/piT8fcScOXb8BzgWt2/giphy.gif')
    time.sleep(3)
    await ctx.send('I have trapped them me lord.')

@trapcard.error
async def trapcard_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}trapcard <user>``")
        await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    embed = discord.Embed(color=0x004c86, title=f"Grabbing a Meme that is Not Racist.")
    fetch = await ctx.send(embed=embed)
    await asyncio.sleep(2)
    req = requests.get("https://apis.duncte123.me/meme")
    meme = req.json()
    embed = discord.Embed(color=0x004c86, description=f"**[{meme['data']['title']}]({meme['data']['url']})**", timestamp=ctx.message.created_at)
    embed.set_image(url=meme['data']['image'])
    await fetch.edit(embed=embed)

@bot.command()
async def hack(ctx, member : discord.Member):
    await ctx.send('https://media.giphy.com/media/8WeatsYCC54TC/giphy.gif')
    await ctx.send('Injecting and running rat, deleting all files, ddosing internet connection, Sends parents video of person masturbating.')
    time.sleep(3)
    await ctx.send('He has been hacked sir.')

@hack.error
async def hack_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Missing Arguments!**", description=f"Usage: ``{ctx.prefix}hack <user>``")
        await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@bot.command(pass_context=True)
@commands.has_permissions()
async def say(ctx, *, message):

    embed = discord.Embed(color=0x004c86, description=f'{message}',)
    embed.set_footer(text="Command Demanded By: {}".format(ctx.message.author.name))

    await ctx.message.delete()
    await ctx.send(embed=embed)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Zeus has Failed to Send your Message**", description=f"Usage: ``{ctx.prefix}say <message>``")
        await ctx.send(embed=embed)
    else:
    	raise(error)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def announce(ctx, channel: TextChannel, *, message):

    embed = discord.Embed(color=0x004c86, title='Announcement', description=f'{message}',)
    embed.set_footer(text="Announcement By: {}".format(ctx.message.author.name))

    await channel.send(embed=embed)
    time.sleep(1)
    await ctx.send('Your Announcement has been Sent by Zeus Himself.')

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Zeus has Failed to Send your Message**", description=f"Usage: ``{ctx.prefix}announce <#channel> <message>``")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
    	embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``Administrator``")
    	await ctx.send(embed=embed)
    else:
    	raise(error)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
    	embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``manage_messages``")
    	await ctx.send(embed=embed)
    else:
    	raise(error)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"Channel Locked Ordered By Zeus!")

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``manage_channels``")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"Channel Unlocked Ordered By Zeus!")


@unlock.error
async def unlock_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
	    embed = discord.Embed(title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``manage_channels``", color=0x000000)
	    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.delete()

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x004c86, title=f"**Zeus had Noticed a Error!**", description=f"Usage: ``{ctx.prefix}kick <user> <reason>``")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
    	embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``kick_members``")
    	await ctx.send(embed=embed)
    else:
    	raise(error)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.send(f'Banned {member.mention}')

@ban.error
async def ban_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=0x004c86, title=f"**Zeus had Noticed a Error!**",
                                  description=f"Usage: ``{ctx.prefix}ban <user> <reason>``")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!",
                                  description=f"Permissions Needed \n ``ban_members``")
            await ctx.send(embed=embed)
        else:
            raise (error)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
    	embed = discord.Embed(color=0x004c86, title=f"**Zeus had Noticed a Error!**", description=f"Usage: ``{ctx.prefix}unban <user>``")
    	await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
    	embed = discord.Embed(color=0x004c86, title=f"You Don't have the Power to Control The Almighty Zeus!", description=f"Permissions Needed \n ``ban_members``")
    	await ctx.send(embed=embed)
    else:
    	raise(error)

@bot.command()
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        r = requests.get('https://nekos.life/api/v2/img/Random_hentai_gif')
        res = r.json()
        embed = discord.Embed()
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Please use an NSFW channel.", color=0x000000)
        await ctx.send(embed=embed)

@bot.command()
async def boobs(ctx):
    if ctx.channel.is_nsfw():
        r = requests.get('https://nekos.life/api/v2/img/boobs')
        res = r.json()
        embed = discord.Embed()
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Please use an NSFW channel.", color=0x000000)
        await ctx.send(embed=embed)

@bot.command()
async def lesbian(ctx):
    if ctx.channel.is_nsfw():
        r = requests.get('https://nekos.life/api/v2/img/les')
        res = r.json()
        embed = discord.Embed()
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Please use an NSFW channel.", color=0x000000)
        await ctx.send(embed=embed)

@bot.command()
async def pussy(ctx):
    if ctx.channel.is_nsfw():
        await ctx.message.delete()
        r = requests.get('https://nekos.life/api/v2/img/pussy')
        pussy = r.json()
        embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
        embed.set_image(url=pussy['url'])
        await ctx.send(embed=embed)
    else:
        await ctx.send('Please use an NSFW channel.')

@bot.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])

@bot.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x004c86)
    await ctx.send(embed=em)

@bot.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@bot.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@bot.command()
async def shrekislove(ctx):
    embed = discord.Embed(color=0x32CD32, description=f'I was only 9 years old. I loved Shrek so much, I had all the merchandise and movies. I pray to Shrek every night, thanking him for the life I’ve been given. “Shrek is love” I say, “Shrek is life." My dad hears me and calls me a faggot. I knew he was just jealous of my devotion to Shrek. I called him a cunt. He hits me and sends me to sleep. Im crying now and my face hurts. I lay in bed, really cold. I feel something warm... Its Shrek! I was so happy. He whispers in my ear "This is my swamp. "He grabs me with his ogre hands, and puts me on my hands and knees. Im ready.I spread my ass cheeks for Shrek. He penetrates my butthole. It hurts so much, but I do it for Shrek. I can feel my butt tearing and eyes watering.I want to please Shrek. He roars a mighty roar as he fills my butt with his love. My dad walks in. Shrek looks him straight in the eye and says, "Its all ogre now." Shrek leaves through my window. Shrek is love. Shrek is life.')
    embed.set_footer(text="Shrek Is Love")
    await ctx.send(embed=embed)


bot.run('Token')
