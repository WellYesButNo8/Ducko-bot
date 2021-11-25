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
  
   @commands.command()
   async def play(self,ctx,url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
    
   
  @commands.command()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.message.add_reaction("⏸")
    await ctx.send("Music paused.")
    
  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.pause()
    await ctx.message.add_reaction("⏯")
    await ctx.send("Music resumed.")
  
  
  
  
  
  
  
  
      
  
