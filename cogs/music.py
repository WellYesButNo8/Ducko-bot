import discord
from discord.ext import commands, tasks
import discordSuperUtils
from discordSuperUtils import MusicManager

MusicManager = MusicManager(bot, client_id=client_id, client_secret=client_secret, spotify_support=True)

  
  class music(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  
  @MusicManager.event()
  async def on_inactivity_disconnect(ctx):
    await ctx.send(f"I have left the channel due to inactivity..")
  
  
    @commands.command()
    async def join(self, ctx):
      embed=discord.Embed(
                    title="Joined Voice Channel",
                    description=f"I have joined {channel.mention}",
                    color=0x00FF00)
        if channel := await self.MusicManager.join(ctx):
            await ctx.send(embed= embed)
    
  
    @commands.command(aliases=["p"])
    async def play(self, ctx, *, query: str):
        if not ctx.voice_client or not ctx.voice_client.is_connected():
            await ctx.send("Join a voice call and use ducko join before using the play command.")

        async with ctx.typing():
            player = await self.MusicManager.create_player(query, ctx.author)

        if player:
            if await self.MusicManager.queue_add(
                players=player, ctx=ctx
            ) and not await self.MusicManager.play(ctx):
                await ctx.send("Added to queue")
        else:
            await ctx.send("Query not found.")
    
   
    @commands.command()
    async def pause(self, ctx):
        if await self.MusicManager.pause(ctx):
            await ctx.send("Player paused.")

    @commands.command()
    async def resume(self, ctx):
        if await self.MusicManager.resume(ctx):
            await ctx.send("Player resumed.")

    @commands.command()
    async def volume(self, ctx, volume: int = None):
        if current_volume := await self.MusicManager.volume(ctx, volume):
            await ctx.send(
                embed=discord.Embed(title="Current Volume", description=f"The current volume is {current_volume}%",color=0x00FF00)
                if volume is None
                else discord.Embed(title="Volume Changed",description=f"Volume has been changed to {current_volume}%",color=0x00FF00))
            
            
      @commands.command()
      async def skip(self, ctx, index: int = None):
        if skipped_player := await self.MusicManager.skip(ctx, index):
            await ctx.send(
                embed=discord.Embed(
                    title=f"Skipped to {index}"
                    if index is not None
                    else "Skipped to Next Song",
                    description=f"Skipped to '{skipped_player}'.",
                    color=0x00FF00,
                )
            )
  
  
  
  
  
  
  
  
      
  
