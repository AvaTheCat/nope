from dotenv import load_dotenv
import discord, os, catts as tt
import silly as sy
from discord.ext import commands

load_dotenv()
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "bleh/", intents=intents)

token = os.getenv("dt")

@bot.event
async def on_ready():
    print(f"We have logged in as user {bot.user} successfully!")

@bot.command()
async def silly(ctx, count_bleh = 5):
    await ctx.send("bleh "*count_bleh)

@bot.command(name="pass")
async def password(ctx, a:int):
    pasw = sy.gen_pass(a)
    await ctx.send(f"Generated Password: {pasw}")

@bot.command(description = "Make simple math easy")
async def math(ctx, opp="SUM", num1 = 5, num2 = 5):
    if opp == "SUM":
        await ctx.send(num1+num2)
    elif opp == "MIN":
        await ctx.send(num1-num2)
    elif opp == "MUL":
        await ctx.send(num1*num2)
    elif opp == "DIV":
        await ctx.send(num1/num2)

@bot.command(name="Cats")
async def cats(ctx):
    pics = tt.catCreate()
    await ctx.send(file = pics)

"""@bot.command('RCat')
async def duck(ctx):
    image_url = tt.get_cat_image_url()
    await ctx.send(image_url)
"""

#Comando para activar API de img de anime por busqueda con palabra clave
@bot.command(name = "anime")
async def anime(ctx, a):
    query = a
    anime_data = tt.get_anime_image(query)
    if anime_data:
        for anime in anime_data:
            
            image_url = anime['attributes']['posterImage']['small']
            await ctx.send(f"Image URL: {image_url}")
    else:
        await ctx.send("No se pudieron obtener datos de anime.")

bot.run(token)

##Oh its easy, i lost to time
##Got a fever of a hundred and im feeeling alright
##Made it out of life in prison without even a fine
##Made it out with no convictions, i like to be bright

##I-I-I-I-I will find you in the nightlife
##I-I-I will kill you in my next life
##I-I sell the all new nine to five -i-i-i-ive
##You stole just what I need
##Attacking vertical

##I give permission for the right price
##I'm on a mission, gonna act right -right -right
##Makе no decision per the dеadline
##You got a valid fight attacking vertical

## ASHKFFGDGDHFFJGHGHDHFJFDDFHJHHDFG :3