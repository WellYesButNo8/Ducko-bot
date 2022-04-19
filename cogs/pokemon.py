from discord import ui
import discord
from discord.ext import commands
import requests

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
        poke=requests.get("https://pokeapi.co/api/v2/pokemon/{pokemon}/")
        sprite=requests.get("")
        pokembed=discord.Embed(title=poke.name, description="Pokemon number {poke.id}")
        pokembed.add_field(name="{poke.name}'s potential abilities",description=poke.abilities,inline=False)