import random
import discord
from discord.ext import commands
import json
import os
client = commands.Bot(command_prefix=commands.when_mentioned_or('~'))
#client.remove_command('help')

messagecount = int(0)







@client.command('test')
async def test(ctx):
    await ctx.send('Twinkle twinkle little star, I want to hit you with my car, Throw you off a cliff so high, I hope you break your neck and die')





cat_image_urls = ['https://tinyurl.com/wtz4m6f','https://tinyurl.com/vk6mzr2','https://tinyurl.com/w726hp5','https://tinyurl.com/ve62dvt','https://tinyurl.com/u6axr8d','https://tinyurl.com/yx88l5wj','https://tinyurl.com/v8pmnwh','https://tinyurl.com/y8at23ko','https://tinyurl.com/y8zqpsxn','https://tinyurl.com/ybdo9ure','https://tinyurl.com/y9mph4jx','https://tinyurl.com/yctxkx2y','https://tinyurl.com/yblfre26']
@client.command('catpic')
async def catpic(ctx):
    random_image_url = random.choice(cat_image_urls)
    embed = discord.Embed(title="You Asked?", description="Cats are just wonderful!",color=int("E0FFF5",16))
    embed.set_image(url=random_image_url)
    await ctx.send(embed=embed)

@client.command('invite')
async def invite(ctx):
    await ctx.send('invite? no this bot is for ***GAMERS*** not you casuals! Hear me out ill give you my invite if you can guess the number! `1-5`')
    randomnumber = random.choice(list(range(1,6)))
    print(randomnumber)
    message = await client.wait_for('message', check=lambda msg: msg.author == ctx.author)
    newmessage = int(message.content)
    print(newmessage)
    if newmessage == int(randomnumber):
        await ctx.send('Here `https://discordapp.com/api/oauth2/authorize?client_id=704739466857939084&permissions=8&scope=bot` stupid stupid')
    elif newmessage < int(randomnumber):
        await ctx.send('You Guessed Too Low!')
        await ctx.send(f'The Number Was {randomnumber}')
    elif newmessage > int(randomnumber):
        await ctx.send('You Guessed Too High!')
        await ctx.send(f'The Number Was {randomnumber}')


@client.event
async def on_member_ban(guild, member):
    logchannel = client.get_channel(698749218013184181)
    await logchannel.send(member.name + " was banned from the server. What a fricking nerd. The nerve of some people LEARN FROM THEIR MISTAKE!")



@client.event
async def on_member_kick(guild, member):
    logchannel = client.get_channel(698749218013184181)
    await logchannel.send(member.name + " was kicked from the server. What a fricking nerd. The nerve of some people LEARN FROM THEIR MISTAKE!")




fruck_image = ['https://tinyurl.com/y8gvkwsp']
@client.command('fruck')
async def fruck(ctx):
    randomimage_url = random.choice(fruck_image)
    embed = discord.Embed(title="Fruck.", description="These Nerds Are Stupid.",color=int("E0FFF5",16))
    embed.set_image(url=randomimage_url)
    await ctx.send(embed=embed)

@client.command('pog')
async def pog(ctx):
    await ctx.send('<:pog:699028854257483777>')


@client.command(name = 'say')
async def say(ctx, discord : discord.TextChannel):
    channel = ctx.message.channel_mentions[0]
    sendin = ctx.guild.get_channel(channel.id)
    print(sendin)
    await ctx.send("What Would You Like Me To Say?")
    say = await client.wait_for('message', check=lambda msg: msg.author == ctx.author)
    await sendin.send(say.content)


#@client.command('help')
#def help(ctx):
   #await ctx.send()


@client.command('count')
async def count(ctx):
    embed = discord.Embed(title="Messages Sent:", description=int(messagecount), color=int("E0FFF5",16))
    await ctx.send(embed=embed)

#@client.event('on_message')
#async def on_message(message):
    #messagecount =+ int(1)
















@client.event
async def on_ready():
    print ("Bot up and running!")
client.run("NzA0NzM5NDY2ODU3OTM5MDg0.XqhiCA.sIEVynUoeguMjS8Se9q_HMUPj1w")

