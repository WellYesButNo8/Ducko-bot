#I have too little cogs lol
import discord
from discord.ext import commands
from utils.perms import Checks

class mod(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
   
  @commands.command()
  async def kick(self, ctx, member):
    mod = Checks.mod_check(ctx.author)
    if mod == True:
      await member.kick()
      await ctx.send(f"Kicked member {member}.")
    else:
      await ctx.send(f"You don't have the permissions to kick {member}.")
      
      
   @commands.command()
   async def ban(self, ctx, member, reason):
      mod = Checks.mod_check(ctx.author)
      if mod==True:
        await Guild.ban(member, reason=reason)
        await ctx.send(f"Successfully banned {member} for {reason}")
      else:
        await ctx.send(f"Sorry, you don't have permissions to ban {member}.")
  
   @commands.command()
   async def newrole(self, ctx, rolename, color):
    rolechange = Checks.edit_roles(ctx.author)
    if rolechange == True:
      await ctx.guild.create_role(name=rolename,colour=discord.Color(color), hoist = True)
    else: 
      await ctx.send(f"Sorry, you don't have permissions to create the role {rolename}.")
      
   
   @commands.command()
   async def editrole(self, ctx, role: discord.Role, attr, arg):
     rolechange = Checks.edit_roles(ctx.author)
     if rolechange == True:
      if attr == "perms":
        await ctx.send("Sorry, you're unable to change permissions with a command. Kind of useless but sorry ¯\_(ツ)_/¯")
      elif attr == "display":
        if role.hoist == True:
          role.hoist = False
        else:
          role.hoise = True
       
      elif attr == "name":
        role.name = arg
      
      elif attr == "color":
        role.color = arg
      else: 
        await ctx.send("sorry, not an option")
        
        
    @commands.command()
    async def hoist(self, ctx, role, num: int):
      rolechange = Checks.edit_roles(ctx.author)
      if rolechange == True:
        await guild.edit_role_positions(role.position += num)
        await ctx.send(f"raised role {role}'s position by {num}")
      else:
        await ctx.send("Sorry, you don't have permission") 
        
def setup(bot):
  bot.add_cog(mod(bot))
