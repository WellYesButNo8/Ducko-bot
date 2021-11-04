#I have too little cogs lol
import discord
from discord.ext import commands

class mod(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
   
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member):
    mod = Checks.mod_check(ctx.author)
    if mod == True:
      await member.kick()
      await ctx.send(f"Kicked member {member}.")
    else:
      await ctx.send(f"You don't have the permissions to kick {member}.")
      
      
   @commands.command()
   @commands.has_permissions(ban_members=True)
   async def ban(self, ctx, member, reason):
        await Guild.ban(member, reason=reason)
        await ctx.send(f"Successfully banned {member} for {reason}")
        
    @commands.command()
    async def ratecheck(self, ctx, member, msgnum = 500):
      #no check here, anyone can use this as it's just a checking command to see how much a user has been active. I added it to moderation as a tool.
      async with ctx.channel.typing():
      counter = 0
      async for message in channel.history(limit=msgnum):
        if message.author == member:
          counter += 1
        else:
          pass
      await ctx.send(f"User {member} has sent {counter} out of the past {msgnum} messages or {msgnum/counter} of the past {msgnum} messages.")
       
  
   @commands.command()
    @commands.has_permissions(manage_guild=True)
   async def newrole(self, ctx, rolename, color):
      await ctx.guild.create_role(name=rolename,colour=discord.Color(color), hoist = True)
      await ctx.send("Role created.")
      
   
   @commands.command()
   @commands.has_permissions(manage_guild=True)
   async def editrole(self, ctx, role: discord.Role, attr, arg):
      if attr == "perms":
        await ctx.send("Sorry, you're unable to change permissions with a command. Kind of useless but sorry ¯\_(ツ)_/¯")
      elif attr == "display":
        if role.hoist == True:
          role.edit(hoist = False)
          await ctx.send("Role display changed.")
        else:
          role.edit(hoist = True)
          await ctx.send("Role display changed.")       
      elif attr == "name":
        role.edit(name=arg)
      
      elif attr == "color":
        role.edit(color=arg)
      else: 
        await ctx.send("sorry, not an option")
        
        
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def hoist(self, ctx, role, num: int):
        await guild.edit_role_positions(role.position += num)
        await ctx.send(f"raised role {role}'s position by {num}")
      else:
        await ctx.send("Sorry, you don't have permission") 
     
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def nick(self, ctx, member, name):
      mod = Checks.mod_check(ctx.author)
      if member == ctx.author or mod == True:
          member.edit(nick=name)
        
def setup(bot):
  bot.add_cog(mod(bot))
