import discord
from discord.ext import commands
import requests
import json

class ApiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    #animal commands
    @commands.command()
    async def axolotl(self):
        axolotlurl=requests.get("https://axoltlapi.herokuapp.com/").text
        url_info=json.loads(axolotlurl)
        for i in url_info["url"]:
            embed=discord.Embed(title="Axolotl pics!", url=i)
        

def setup(bot):
  bot.add_cog(ApiCommands(bot))