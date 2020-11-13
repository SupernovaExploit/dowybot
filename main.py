import discord
import os
import time
import random
import string

from discord.ext import (
    commands,
    tasks
)

prefix = 'w!'
owner = '!                           Døwy#0666'
v = "v1"
token = "Nzc2NTA2OTY0NDc2NjkwNDMz.X614dw.RNH7v76v1CEDwv9AjeKXXzxRCEA"

bot = commands.Bot(command_prefix='w!', bot=True)
bot.remove_command("help")
@bot.event
async def on_ready():
    print('Ready!')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

### -- CHANNELS -- ###

@bot.command()
async def event(ctx):
    await ctx.message.delete()
    await ctx.send('''
<a:classic:774972025068060703>  **__NITRO EVENT__** <a:boost:774972026095665182>

**2** Invites = **Nitro Classic** ``1 Month`` <a:classic:774972025068060703>
**3** Invites = **Nitro Classic** ``1 Year`` <a:classic:774972025068060703>

**4** Invites = **Nitro Boost** ``1 Month`` <a:boost:774972026095665182>
**5** Invites = **Nitro Boost** ``1 Year`` <a:boost:774972026095665182>

10 MINUTES LEFT OF EVENT!!! <a:bell:776438868164870194> 
@everyone
''')

@bot.command()
async def reward(ctx):
    await ctx.message.delete()
    await ctx.send('''
    <a:classic:774972025068060703>  **__NITRO REWARDS__** <a:boost:774972026095665182>

**3** Invites = **Nitro Classic** ``1 Month`` <a:classic:774972025068060703>
**6** Invites = **Nitro Classic** ``1 Year`` <a:classic:774972025068060703>

**12** Invites = **Nitro Boost** ``1 Month`` <a:boost:774972026095665182>
**16** Invites = **Nitro Boost** ``1 Year`` <a:boost:774972026095665182>

@everyone
''')

@bot.command()
async def readme(ctx):
    await ctx.message.delete()
    await ctx.send('''
IF YOU DO NOT SUBSCRIBE TO THE 2 CHANNELS BELOW, YOU CAN NOT RECIEVE ANY REWARDS!

 @everyone 

<a:tick:776512436844232724> https://youtube.com/twoky
<a:tick:776512436844232724> https://youtube.com/xZowyHere
    ''')

### -- GHOSTPING -- ###

@bot.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('@everyone', delete_after=0.1)

@bot.command()
async def here(ctx):
    await ctx.message.delete()
    await ctx.send('@here', delete_after=0.1)

### -- NITRO -- ###

@bot.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

### -- OTHER -- ###

@bot.command()
async def nuke(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel is not None:
        await ctx.channel.send('**Nuking...**', delete_after=1)
        await existing_channel.clone(reason="Has been nuked")
        await existing_channel.delete()
        time.sleep(5)
        await ctx.send('**Nuked!**', delete_after=1)
    else:
        await ctx.send(f'No channel named **{channel_name}** was found')

### -- HELP -- ###

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Commands!',
        description = 'This is all of the command to the "3 Invite = Nitro" Bot!',
        colour = discord.Colour.dark_magenta()
    )

    embed.set_footer(text='Created by: ' + owner)
    embed.set_image(url='https://cdn.discordapp.com/attachments/774912535014277140/776507201232568361/tenor.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/774912535014277140/776507201232568361/tenor.gif')
    embed.add_field(name=prefix + "everyone", value="Ghost pings @everyone", inline=True)
    embed.add_field(name=prefix + "here", value="Ghost pings @here", inline=True)
    embed.add_field(name=prefix + "readme", value="Displays a 'No sub no rewards' message", inline=True)
    embed.add_field(name=prefix + "reward", value="Displays a 'Nitro rewards' message", inline=True)
    embed.add_field(name=prefix + "event", value="Displays a 'Nitro Event' message", inline=True)
    embed.add_field(name=prefix + "nitro", value="Sends a random nitro gift", inline=True)

    await ctx.send(embed=embed)



bot.run(token)
