import os
import discord as dc
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv () 
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

intents = dc.Intents.default()
intents.message_content = True
intents.members = True           

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.event
async def on_member_join ( member ) :
    channel = dc.utils.get ( member.guild.text_channels , name = "welcome" )
    if channel :
        welcome_message = f'welcome { member.mention } join the server !'
        await channel.send ( welcome_message ) 

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)
