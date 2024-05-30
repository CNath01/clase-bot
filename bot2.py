import discord
from discord.ext import commands
import random

# Configuración de intents para obtener el contenido de los mensajes
intents = discord.Intents.default()
intents.message_content = True

intents.members = True


# Crear una instancia del bot con el prefijo de comando '$'
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except ValueError:
        await ctx.send('Format has to be in NdN!')
        return
    
    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(f'Resultados: {result}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
# Ejecutar el bot con el token
bot.run("token")
