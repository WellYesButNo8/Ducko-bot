import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'waka')

@bot.event
async def on_ready():
  activity = discord.Activity(type = discord.ActivityType.competing, name = "in The Hunger Games!", state = "Hunting down the girl from district 11", party = [13, 24])
  await bot.change_presence(activity = discord.Game(name = "with Matches"))
  print("Bot is ready")
extentions = ['cogs.guildEvent', 'cogs.music', 'cogs.reddit', 'cogs.apis', 'cogs.pokemon']
for i in extentions:
  bot.load_extention(i)
  pass
bot.run(token)
