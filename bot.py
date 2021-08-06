#                ._____.           __   
#   ___________  |__\_ |__   _____/  |_ 
#   \____ \__  \ |  || __ \ /  _ \   __\
#   |  |_> > __ \|  || \_\ (  <_> )  |  
#   |   __(____  /__||___  /\____/|__|  
#   |__|       \/        \/             

#This code is horrendous. Just saying.
import os, discord, random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

#____   ____            .__      ___.   .__                 
#\   \ /   /____ _______|__|____ \_ |__ |  |   ____   ______
# \   Y   /\__  \\_  __ \  \__  \ | __ \|  | _/ __ \ /  ___/
#  \     /  / __ \|  | \/  |/ __ \| \_\ \  |_\  ___/ \___ \ 
#   \___/  (____  /__|  |__(____  /___  /____/\___  >____  >
#               \/              \/    \/          \/     \/ 
TOKEN = ""
GUILD = "gnarzy's server"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
#Deletes Default Help Command
bot.remove_command('help')
print("\n\n\n\n\nInitializing Paibot...\n\n\n\n\n")
#Adding all GIF/Images
images = []
for i in range(1,6):
    images.append("assets/paibot"+str(i)+".gif")


#___________                    __          
#\_   _____/__  __ ____   _____/  |_  ______
# |    __)_\  \/ // __ \ /    \   __\/  ___/
# |        \\   /\  ___/|   |  \  |  \___ \ 
#/_______  / \_/  \___  >___|  /__| /____  >
#        \/           \/     \/          \/ 
@bot.event
async def on_ready():
    #Looks for the specific server the bot is in.
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    #Prints the bot connecting and the server's id.
    print(f'{bot.user} is connected to the following server: '
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
    await member.dm_channel.send(f'Paibot welcomes you, {member.name}!')


@bot.event
async def on_message(message):
    #Makes sure that the bot does not reply to itself.
    if message.author == bot.user:
        return
    #Random lines
    lines = ["Paibot is flattered you mentioned Paibot...", 
    "Paibot does not care.",
     "Paibot just doesn't get it...",
     "Paibot is happy for you! Even though Paibot doesn't know what you said!",
     "Paibot is REALLY confused... Paibot hates math..."]
    #Sends message if "Paibot is ever mentioned."
    if "Paibot" in message.content or "paibot" in message.content:
        number = random.randint(0,4)
        await message.channel.send(lines[number])
        await message.channel.send(file=discord.File(images[number]))
    await bot.process_commands(message)



#_________                                           .___      
#\_   ___ \  ____   _____   _____ _____    ____    __| _/______
#/    \  \/ /  _ \ /     \ /     \\__  \  /    \  / __ |/  ___/
#\     \___(  <_> )  Y Y  \  Y Y  \/ __ \|   |  \/ /_/ |\___ \ 
# \______  /\____/|__|_|  /__|_|  (____  /___|  /\____ /____  >
#        \/             \/      \/     \/     \/      \/    \/ 

#Used for help!
@bot.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.light_gray())
    embed.set_author(name="Paibot Help:")
    embed.add_field(name="!reset", value="Used for resetting server to basic text and voice channel.",inline=False)
    embed.add_field(name="!nuke", value="Creates 100 channels, spams @everyone ping since Paibot is taking over.",inline=False)
    embed.add_field(name="!spam <user> <word>", value="Spams a word 5 times to a specific user.",inline=False)
    embed.add_field(name="!paibot",value="If paibot hears it's name, paibout is bound to respond!")
    await member.create_dm()
    await member.dm_channel.send(embed=embed)

#Used for resetting server to basic text and voice channel.
@bot.command()
async def reset(ctx):
    for i in ctx.guild.channels:
        await i.delete()
    await ctx.guild.create_text_channel('general-chat')
    await ctx.guild.create_voice_channel('general-vc')

#Creates 100 channels, spams @everyone ping since Paibot is taking over.
@bot.command()
async def nuke(ctx):
    for i in ctx.guild.channels:
        await i.delete()
    for i in range(100):
        await ctx.guild.create_text_channel('Paibot'+str(i))
    for channel in ctx.guild.channels: 
        await channel.send("@everyone, Paibot's taking over now!")
        await channel.send(file=discord.File("assets/paibotnuke.gif"))

#Spams message given to a specific person.
@bot.command()
async def spam(ctx, name, message):
    found = False
    for member in ctx.guild.members:
        if(member.name == name):
            found = True
            for times in range(5):
                await member.create_dm()
                await member.dm_channel.send(str(message))
    if(found):
        await ctx.channel.send("Paibot spammed the user!")
    else:
        await ctx.channel.send("Paibot can't find that user...")

#Shuts down bot.
@bot.command()
async def shutdown(self,ctx):
    print("shutdown")
    try:
        await self.bot.logout()
    except:
        print("EnvironmentError")
        self.bot.clear()
    else:
        await ctx.send("You do not own this bot!")
bot.run(TOKEN)