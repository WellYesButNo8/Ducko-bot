import discord
from discord import ui
from discord.ext import commands


class Paginator():
  def __init__(self):
    self.color = 0
    self.ctx = discord.ctx
    self.empty_embed = discord.Embed(title=None, description=None, color=self.color)
    self._pages=[self.empty_embed,] 
    self.current_page=0

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
  
  def _remove_page(self, page:discord.Emed):
    if page not in self._pages:
      #throw error here idk like "page object invalid or not found in list"
    
    #and then i forgot how to take smth out of a list so welp smh

  async def _change_page(self, dir: bool):
    if dir == True:
      #something with lists here it might be `await ctx.send(embed= _pages[{whatever page ur on + 1}]`
      await ctx.send(embed=_pages[{current_page+1}])
    if dir==False:
      #same as going right but for left so subtract 1 
      await ctx.send(embed=_pages[{current_page-1}])

  



  
  

  

    
        
        
      
