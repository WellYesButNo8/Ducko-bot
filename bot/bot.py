import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'itami')

@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Game(name = "with Matches"))
  print("Bot is ready")
extentions = ['cogs.guildEvent', 'cogs.fun', 'cogs.mod']
for i in extentions:
  bot.load_extention(i)
  pass
bot.run(token)
