#I have too little cogs lol
import discord
from discord.ext import commands

class mod(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
   
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"Kicked member {member}.")
      
   @commands.command()
   @commands.has_permissions(ban_members=True)
   async def ban(self, ctx, member: discord.Member, reason):
    await Guild.ban(member, reason=reason)
    await ctx.send(f"Successfully banned {member} for {reason}")
        
    @commands.command()
    async def ratecheck(self, ctx, member: discord.Member, msgnum: int):
      #no check here, anyone can use this as it's just a checking command to see how much a user has been active. I added it to moderation as a tool.
      if msgnum == None:
        msgnum = 500
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
    async def hoist(self, ctx, role: discord.Role, num: int):
      await guild.edit_role_positions(role.position += num)
      await ctx.send(f"raised role {role}'s position by {num}")
     
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def nick(self, ctx, member: discord.Member, name):
      member.edit(nick=name)
    
    @commands.command()
    @commands.has_permissions(manage_members = True)
    @commands.guild_only
    async def mute(self, ctx, member: discord.Member):
      muterole = next((g for g in ctx.guild.roles if g.name == "Muted"), None)
      if not muterole:
        no_muterole = Paginator.roleError("No Muterole found.", "Are you sure you've created a role called **Muted**?")
        await ctx.send(embed = no_muterole)
      else:
        bot.add_role(muterole)
        mutesuccess = Paginator.cmdSuccess(f"{member} muted until unmuted by a moderator.")
        await ctx.send(
        
def setup(bot):
  bot.add_cog(mod(bot))
