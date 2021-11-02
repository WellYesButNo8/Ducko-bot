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
      #Invalid arg error throws are dealt with adequately
      if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
        await ctx.send(f"Sorry, that's not a valid argument. Please try again with a different argument.")
      #Weird API errors dealt with. Nothing to really do about it but eh
      if isinstance(err, errors.CommandInvokeError):
        await ctx.send("There was an error processing this command. Please try again in a bit.")
      #loginfailure error dealt with
      if isinstance(err, errors.LoginFailure):
        bot.run(token) #trying to log in again
      # invalid discord data
      if isinstance(err, errors.InvalidData):
        await ctx.send("Recieved invalid data from discord. Try again later.")
  
def setup(bot):
  bot.add_cog(guildEvent(client)
                           
