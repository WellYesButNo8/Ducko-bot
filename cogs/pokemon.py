from discord import ui
import discord
from discord.ext import commands
import requests
from utils.Pagination import Paginator as pg 

class pokebutton(ui.Button):
    def __init__(self, label=label, row=row, **kwargs):
        super().__init__(label, row, pokemon, **kwargs)

class Abilities(pokebutton):
    def callback(self, interaction):
        view=self.view
        embed=discord.Embed(title="Abilities", description="all potential abilities this pokemon has")
        for ability in pokemon.abilities:
            embed.add_field(name=ability, description=None, inline=True)
        
class Pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    
    
    @commands.command()
    async def stat(self, pokemon): 
        view=discord.ui.View()
        poke=requests.get("https://pokeapi.co/api/v2/pokemon/{pokemon}/")
        abilites = Abilities(style=discord.ButtonStyle.grey, label="Abilities", pokemon=poke)
        view.add(abilities)
        sprite=requests.get("")
        pokembed=discord.Embed(title=poke.name, description="Pokemon number {poke.id}")
        await ctx.send(embed=pokembed, view=view)
        
    


def setup(bot):
  bot.add_cog(Pokemon(bot))

