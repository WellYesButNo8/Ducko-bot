import discord
from discord import ui
from discord.ext import commands


class Paginator():
  
  def __init__(self, ctx, arg1, arg2 = None, arg3 = None):
    self.arg1 = arg1
    self.arg2 = arg2 or None
    self.arg3 = arg3 or None
    self.ctx = commands.Context
    
  # embed presets
  @classmethod # Error embed in case something didn't turn out.
  def roleError(self, arg1, arg2=None, arg3 = None):
    newemb = discord.Embed(title = arg1, color = 0xD35400)
    if arg2 not None:
      newemb.add_field(inline = False, name = arg2, value = arg3)
    else:
      pass
    return newemb
  
  @classmethod
  def cmdSuccess(self, arg1): # creates a command successful embed with whatever title i specify (could be for a command with a name that's a special case)
    newembed = discord.Embed(title = arg1, description = "Command successful.", color = 0xD3500)
    return newembed
 
  @classmethod
  def helpCmd(self, arg1, cat): # creates a help command embed
    newemb1 = discord.Embed(title = f"Help for {cat} category", description = arg1, color = 0xD3500)
    return newemb1
  
  # paginator utils
  @classmethod #adds help commands (new fields in the embed) in the help embed. Honestly it can be used for anything but it's meant for the help command embed.
  def add_help_commands(self, arg1, arg2, embed: discord.Embed):
    embed.add_field(inline = False, name = arg1, value = arg2)
  
  @classmethod # switches one embed with another.
  def switch(self, ctx, embed: discord.Embed, msg: discord.Message):
    await msg.edit(embed = embed)
    
  #that's all my classmethods!
    
  

    
        
        
      
