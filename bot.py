
#Command + . to stop process.
#pip3 install discord, pip3 install python-dotenv
import os, discord, random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

#Bot Commands (LATER):

#Variables
TOKEN = ""
GUILD = "teaching"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

#THIS CODE HAPPENS WHENEVER THE CODE IS RUN.
@bot.event
async def on_ready():
    #Looks for the specific server the bot is in.
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    #Prints the bot connecting and the server's id.
    print(f'{bot.user} is connected to the following guild:)\n'
    f'{guild.name}(id: {guild.id})\n')   
    #Print Guild Members:
    print("Guild Members:")
    #Loop through guild members to send a dm!
    for member in guild.members:
        print(f'- {member.name}')
        #if(member.name == "gnarzy"):
        #    await member.create_dm()
        #    await member.dm_channel.send('Hi')

#Prints something when someone joins your server!
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Welcome {member.name}!')


@bot.event
async def on_message(message):
    #Makes sure that the bot does not reply to itself.
    if message.author == bot.user:
        return
    #Lines that the bot can say.
    lines = [
        "hbd!","ඞ","Happy Birthday!"
    ]
    #Sends message if you say "Happy Birthday!"
    if message.content == 'Happy Birthday!':
        response = random.choice(lines)
        await message.channel.send(response)
    await bot.process_commands(message)

#Used for resetting server to basic text and voice channel.
@bot.command(name="reset",help="Resets the server.")
async def nuke(ctx):
    for i in ctx.guild.channels:
        await i.delete()
    await ctx.guild.create_text_channel('general-chat')
    await ctx.guild.create_voice_channel('general-vc')

#Creates 20 channels, spams @everyone ping.
@bot.command(name="nuke",help="Nukes server.")
async def nuke(ctx):
    for i in ctx.guild.channels:
        await i.delete()
    for i in range(0,20):
        await ctx.guild.create_text_channel('nuke-channel-'+str(i))
    for i in range(0,100):
        for channel in ctx.guild.channels: 
            await channel.send("@everyone " + str(ctx.author) + " has just nuked the server.")

#Spams message given to a specific person.
@bot.command(name="spam",help="Spams a message to a user in the server.")
async def spam(ctx, name, message):
    found = False
    for member in ctx.guild.members:
        if(member.name == name):
            found = True
            for times in range(5):
                await member.create_dm()
                await member.dm_channel.send(str(message))
    if(found):
        await ctx.channel.send("Spammed the user.")
    else:
        await ctx.channel.send("Could not find the user.")
    
bot.run(TOKEN)