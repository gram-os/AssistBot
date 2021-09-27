import os
import discord
import nasa
import random
import helper_func
import asyncio
import typing
import nacl

from keep_alive import keep_alive
from discord.ext import commands
from replit import db

BOT_TOKEN = os.environ['BOT_TOKEN']

client = discord.Client()

animal_path = 'assets/animal-pics/'
animal_pics = os.listdir(animal_path)

banned_words = set(["fuck","fucking", "shit", "damn", "ass", "coochie", "dick", "nazi", "bitch", "pussy", "crap", "cummies","bussy","bicho","puñeta", "fk","crapper", "craptastic", "shitter", ])

horny_jail=[]

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print("Bot is online")

async def joinVC(ctx):
  if not ctx.message.author.voice:
    await ctx.send("You need to be connected to a voice channel!")
    return
  else:
    channel=ctx.author.voice.channel
  await channel.connect()

async def leaveVC(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_connected():
    await ctx.voice_client.disconnect()
  else:
    await ctx.send("The bot is not connected to a voice channel...")

@bot.command(name='whos-that-animal', help = 'Responds with a random animal pic')
async def whos_that_animal(ctx):

  index=random.randrange(0,len(animal_pics))
  if (index==6):
    if random.randrange(0,100) == 50:
      response = discord.File(animal_path+animal_pics[index])
      await ctx.send(response)
    else:
      index=random.randrange(0,len(animal_pics))
  response = discord.File(animal_path+animal_pics[index])
  await ctx.send(file = response)

@bot.command(name='hello', help='Says hello!')
async def hello(ctx):
  await ctx.send('hewwo mr obama...')

@bot.command(name='F', help='Bot-sensei dispenses wisdom')
async def inspire(ctx):
  quote = helper_func.get_quote()
  await ctx.send(quote)

@bot.command(name='hurt-me-daddy', help='Bot-sensei dispenses punishment')
async def insult(ctx):
  insult = helper_func.get_insult()
  await ctx.send(insult)

@bot.command(name='tsp', help='Sends NASA Space Pic of the Day')
async def space_pic(ctx):
  apod = nasa.getAPOD()
  text = apod.printAPOD()
  await ctx.send(text)

@bot.command(name='lib', help='Trigger the libs')
async def lib(ctx):
  await ctx.send("listen to this you snowflake: https://youtu.be/PdYLRTGmQ3c")

@bot.command(name='dox-me', help='Expose your personal info')
async def doxxed(ctx):
  await ctx.send("no..")

@bot.command(name='caught', help='Wow, you really did that')
async def caught8k(ctx):
  await ctx.send("📸 caught in 8k, my dude. smh")

@bot.command(name='cuomo', help='oof gov. cuomo')
async def cuomo(ctx):
  await ctx.send("you've gabbaed your last goo governor cuomo 😈")

@bot.command(name='samuel', help='samuel')
async def samuel(ctx):
  file = discord.File('assets/samuel.jpg')
  await ctx.send(file=file)

@bot.command(name='bonk', help='horny bonk someone')
async def bonk(ctx, member:typing.Optional[discord.Member]):
  animated_emoji=discord.utils.get(ctx.guild.emojis,name='BonkDOGE')
  regular_emoji=discord.utils.get(ctx.guild.emojis,name='BONK')

  if member:
    if animated_emoji: 
      await ctx.send(f"{member.mention}\n{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}")
    elif regular_emoji:
      await ctx.send(f"{member.mention}\n{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}")
    else:
      await ctx.send("BONK")
  else:
    if animated_emoji: 
      await ctx.send(f"{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}{animated_emoji}")
    elif regular_emoji:
      await ctx.send(f"{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}{regular_emoji}")
    else:
      await ctx.send("BONK")


async def flashVC(ctx, target:typing.Optional[discord.Member]):
  og_channel = target.voice.channel
  channel = discord.utils.get(ctx.guild.voice_channels, name = "warzone")

  if ctx.author.voice:
    if target:
      if not channel:
        channel = target.voice.channel
      await target.move_to(channel)
      voice = await channel.connect()
      voice.play(discord.FFmpegPCMAudio('assets/flashbang_sound_effect.mp3'))
      await asyncio.sleep(8)
      await ctx.guild.voice_client.disconnect()
      await target.move_to(og_channel)
  else:
    print(f"{target} was not connected to VC")

@bot.command(name='flashbang', help='flash a mf. make sure to pick a target TW: Loud scawy noise')
async def flash(ctx, member:typing.Optional[discord.Member]):
  pic = discord.File('assets/think-fast.gif')

  if member:
    await ctx.send(f"{member.mention}")
    await ctx.send(file=pic)
    await flashVC(ctx,member)
  else:
    await ctx.send("You gotta target someone, pal")
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(file=pic)
    await flashVC(ctx,ctx.author)

@bot.command(name='titties', help='send pics of titties')
async def titties(ctx):
  author = ctx.author.name
  pic = discord.File('assets/caught-in.gif')

  await ctx.send('Looking for titty pics online...')
  await asyncio.sleep(2)

  await ctx.send('Titties has been acquired!')
  await ctx.send('Sending titties')
  await asyncio.sleep(1)

  await ctx.send('3')
  await asyncio.sleep(1)
  await ctx.send('2')
  await asyncio.sleep(1)
  await ctx.send('1')
  await asyncio.sleep(1)

  if author in db.keys():
    if db[author] < 10:
      await ctx.send(file=pic)
      db[author] = db[author]+1
      print(author + "+" + str(db[author]))
  else:
    await ctx.send(file=pic)
    db[author] = 1
  
  if db[author] == 3:
    await ctx.send("They say 3rd times the charm, but...")
    await ctx.send("give up bro...")
  elif db[author]<10 and db[author]>3:
    await ctx.send("Please stop")
  
  if db[author] >= 10:
    await ctx.send("Fine.")
    await ctx.send("Here ya go: <https://bit.ly/3nIziyz>")

    await ctx.send("Imma reset that counter for ya ;)")
    del db[author]

@bot.command(name='banish', help='Send a homie to horny jail')
async def banish(ctx, member:typing.Optional[discord.Member]):
  weeb_role = discord.utils.get(ctx.guild.roles, name="Weeb")
  
  if member:
    await ctx.send(f"{member.mention}. You have been banished to horny jail! Reflect upon your sins and repent.")
    await bonk(ctx,member)
    await start_horny_timer(ctx, weeb_role, member)
    await ctx.send(f"{member.mention}. You have been forgiven...")

  else:
    db_key=ctx.author.name+"-horny-miss"
    
    if db_key in db.keys():
      db[db_key]+=1
      await ctx.send('You must signal the prisoner\nThis waste of time will not go unnoticed!')
      if db[db_key] == 10:
        await ctx.send('Now suffer the consecuences of your actions!')
        await start_horny_timer(ctx, weeb_role, ctx.author)
        db[db_key] = 1
    else:
      await ctx.send('You must signal the prisoner\nThis waste of time will not go unnoticed!')
      db[db_key]=1

async def start_horny_timer(ctx, role, member):
  timer = 60
  embed = discord.Embed(title="Banished!", description=f"{member.mention} has been banished ", colour=discord.Colour.light_gray())
  embed.add_field(name="Time sentence:", value=f"{timer} seconds", inline=False)
  await member.send(embed=embed)
  await ctx.send(embed=embed)

  await member.send(file=discord.File('assets/baka-dead.mp4'))

  await member.remove_roles(role)
  await asyncio.sleep(timer)
  await member.add_roles(role)

@bot.listen('on_message')
async def fuck_it(message):
  msg = helper_func.clean_message(message.content)

  if "king" in msg:
    await message.channel.send("you dropped this 👑")

  if "republican" in msg:
    await message.channel.send("ewwww 🤢🤮🤧😷")
  
  if banned_words.intersection(msg):
    await message.channel.send('Watch your language!')

  if "huh" in msg:
    await message.channel.send(file=discord.File('assets/animal-pics/huh_wuh.png'))

keep_alive()
bot.run(BOT_TOKEN, reconnect=True)