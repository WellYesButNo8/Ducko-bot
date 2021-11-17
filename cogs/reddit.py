import discord
from discord.ext import commands
import praw

reddit = praw.Reddit( client_id= client_id, client_secret = client_secret, user_agent = user_agent, username = username, password = password)

class Reddit(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  
  @commands.command(aliases = ['dankmemes', "Memes", "Meme", "Dankmeme", "Dankmemes", "r/Memes", description = "Provides)
  async def meme(self, ctx):
        subreddit = reddit.subreddit('memes')
        top = subreddit.top(limit = 50)
        for submission in top:
          topsubs = []
          topsubs.append(submission)
        ransub = random.choice(tobsubs)
        embed = discord.Embed(title = ransub.title, url = ransub.url, color = 0xD3500)
        embed.set_footer(text = f"Requested by {ctx.author.display_name)
        await ctx.send(embed = embed)


def setup(bot):
  bot.add_cog(Reddit(bot))
  
