import discord
from discord.ext import commands
import yt_dlp  
import asyncio
import os
from dotenv import load_dotenv
import ffmpeg
import pkg_resources
import importlib.metadata

print(f"discord.py version: {discord.__version__}")
print(f"yt-dlp version: {yt_dlp.__version__}")
print(f"yt-dlp version: {pkg_resources.get_distribution('yt-dlp').version}")
print(f"yt-dlp version: {importlib.metadata.version('yt-dlp')}")

# Cargar variables de entorno desde el archivo .env
load_dotenv()  # Carga las variables de entorno

# Obtener el token desde las variables de entorno
TOKEN = os.getenv("DISCORD_TOKEN") 

if not TOKEN:
    print("Error: No se pudo cargar el token de Discord. Asegúrate de que el archivo .env esté presente y correcto.")
    exit(1)  # Termina el programa si el token no se carga

# Configuración del bot y el cliente
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=",", intents=intents)  # Aquí defines el cliente como Bot

# Configuración para descargar audio de YouTube
ytdl_opts = {
    'format': 'bestaudio[ext=webm]/bestaudio',
    'noplaylist': True,
    'quiet': True,
    'extractaudio': True,
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    },
}

ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

# Funciones para manejar la conexión de voz y la reproducción de audio
async def join_vc(ctx):
    """Hace que el bot se conecte a un canal de voz"""
    if not ctx.author.voice:
        await ctx.send("¡Debes estar en un canal de voz para usar este comando!")
        return None

    channel = ctx.author.voice.channel
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected():
        return voice_client 

    try:
        voice = await channel.connect()
        return voice
    except discord.errors.ClientException:
        await ctx.send("No pude unirme al canal de voz.")
        return None

async def play_audio(ctx, url):
    """Reproduce audio en un canal de voz sin descargar"""
    voice = await join_vc(ctx)
    if not voice:
        return

    await ctx.send(f"🔍 Buscando en YouTube: {url}")
    print(f"📥 URL recibida: {url}")

    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['url']
            print(f"🎵 URL de audio obtenida: {URL}")

        voice.play(discord.FFmpegPCMAudio(URL, **ffmpeg_opts))
        await ctx.send(f"🎶 Reproduciendo: {info.get('title', 'Desconocido')}")
        print(f"✅ Reproduciendo {info.get('title', 'Desconocido')}")
    except Exception as e:
        print(f"❌ Error al reproducir: {e}")
        await ctx.send("❌ Hubo un problema al reproducir el audio.")

# Eventos y comandos
@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.command()
async def test(ctx):
    await ctx.send("✅ ¡no trabajo causa no trabajo, trabajar aburre pe!")

@client.event
async def on_message(message):
    await client.process_commands(message)  

@client.command()
async def play(ctx, url: str):
    """Comando para reproducir música"""
    print(f"Comando recibido: ,play {url}")
    await ctx.send(f"⏳ Buscando la canción en YouTube pe...")
    await play_audio(ctx, url)

@client.command()
async def p(ctx, url: str):
    """Comando para reproducir música"""
    print(f"Comando recibido: ,play {url}")
    await ctx.send(f"⏳ Buscando la canción en YouTube pe...")
    await play_audio(ctx, url)

@client.command()
async def stop(ctx):
    """Comando para detener la música y desconectar"""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("⏹ Bot desconectado del canal de voz.")
    else:
        await ctx.send("❌ No estoy en un canal de voz.")

# Inicia el bot con el token
client.run(TOKEN)
