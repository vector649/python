import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True


token = 'ODY0ODQ3MjI4MTM3MjQyNjQ1.YO7Zvw.tkhAuCR1jGGgzHpaPDljdbu45GM'

bot = commands.Bot(command_prefix=('!'),intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Я запущен!")
    

slova = ["педик","нытик","лоускилл","сынок ёбанный", "петушара", "дырявый", "говноед", "терпила"]
    
@bot.command()
async def Засри(ctx):
    await ctx.send('Володя '+slova[random.randint(0,len(slova)-1)])



@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = '''Команды
1.Apex''',
    )
    await ctx.send(embed = embed)


users = ['DEDEC#5463','Kwaha#9054','voyager#9625','クラシック#9950']

@bot.command()
async def Apex(ctx):
    mentioned = []
    my_name = ctx.message.author.id
    result = ''
    for guild in bot.guilds:
        for member in guild.members:
            if str(member) in users and not str(member) in mentioned and member.id!=my_name:
                mentioned.append(str(member))
                result+=member.mention+","
    result = result[0:len(result)-1]
    await ctx.send(result)
                

    

bot.run(token)
