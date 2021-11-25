import discord
from discord.ext import commands, tasks
import youtube_dl as yt

# class for error handling

class VoiceNotPresent():
  pass



class music(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  
  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("Please join a voice channel, then use this command again.")
    
    vc = ctx.author.voice.channel
    if ctx.voice_client is None:
      await vc.connect()
    else:
      await ctx.voice_client.move_to(vc)
    
   
  @tasks.loop(seconds = 5.0)
  async def vc_empty(self, ctx):
    voice_channel = ctx.voice.channel
    if voice_channel.members is None:
      vc.disconnect()
    else:
      pass
      
  
