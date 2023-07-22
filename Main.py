import discord
from discord.ext import commands
import os

# Access the token from the environment variable
token = os.environ.get['DISCORD_TOKEN']


intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        text_channel = discord.utils.get(member.guild.text_channels, name='your-text-channel')
        if text_channel is not None:
            await text_channel.send(f"@everyone, {member.name} has joined {after.channel.name} and is now working!")

# Replace 'your-token-goes-here' with your bot's token
bot.run(token)


import os

token = os.environ.get('DISCORD_TOKEN')
print(f"Token: {token}")
