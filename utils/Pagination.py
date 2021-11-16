import discord
from discord import ui
from discord.ext import commands


class Paginator():
  
  def __init__(self, arg1, arg2 = None, arg3 = None):
    self.arg1 = arg1
    self.arg2 = arg2 or None
    self.arg3 = arg3 or None
    
    
  # embed presets
  @classmethod
  def roleError(self, arg1, arg2=None, arg3 = None):
    newemb = discord.Embed(title = arg1, color = 0xD35400)
    if arg2 not None:
      newemb.add_field(inline = False, name = arg2, value = arg3)
    else:
      pass
    return newemb
  
  @classmethod
  def cmdSuccess(self, arg1):
    newembed = discord.Embed(title = "Command successfully executed.", description = arg1, color = 0xD3500)
    return newembed
 
  @classmethod
  def helpCmd(self, arg1, cat):
    newemb1 = discord.Embed(title = f"Help for {cat} category", description = arg1, color = 0xD3500)
    return newemb1
  

    
        
        
      
