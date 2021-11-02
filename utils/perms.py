import discord
from discord.ext import commands
from discord.ext.commands import errors


class Checks():
  
  def owner_check(ctx):
    return ctx.author.id in owners

  def check_admin(ctx):
    return ctx.author.guild_permissions.administrator

  def edit_guild(ctx):
    return ctx.author.guild_permissions.manage_guild

  def mod_check(ctx):
    if ctx.author.guild_permissions.ban_members and ctx.author.guild_permissions.kick_members == True:
      return True
    else: 
      return False
  
  def role_check(ctx, role):
    return ctx.author.has_role(role)
  
  def edit_roles(ctx):
    return ctx.author.guild_permissions.manage_roles
  
  def all_mention(ctx):
    return ctx.author.guild_permissions.mention_everyone
  
  def delete_msg(ctx):
    return ctx.author.guild_permissions.manage_messages

  


  

  
