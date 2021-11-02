import discord
from discord.ext import commands
from discord.ext.commands import errors
class guildEvent(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Welcome to {member.guild.name}.")
        embed = discord.Embed( title = f"Welcome, {member}! hope you have a great time at {member.guild.name}.", color = 0x283747)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx):
      if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
        await ctx.send(f"Sorry, that's not a valid argument. Please try again with a different argument.")
      if isinstance(err, errors.CommandIN
  
def setup(bot):
  bot.add_cog(guildEvent(client)
                           
