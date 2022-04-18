import discord
from discord import ui
from discord.ext import commands


class Paginator():
  def __init__(self):
    self.color = 0
    self._pages=[]
    self.empty_embed = 

  def _clear(self):
    """
    Clears all pages so the embed is empty
    """
    self.pages = []

  def _new_page(self, title: str, description: str):
    """
    creates a new embed
    """
    return discord.Embed(title=title, description=description, color=self.color)
  
  def _add_page(self, page: discord.Embed):
    self._pages.append(page)



  
  

  

    
        
        
      
