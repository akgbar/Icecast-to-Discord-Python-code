import discord
from discord.ext import commands

# Your Icecast stream URL
ICECAST_URL = "Your Icecast Stream URL"

# Your Discord bot token
DISCORD_BOT_TOKEN = "Your Bot Token you copied"

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"{bot.user} is now running")

@bot.command()
async def live(ctx, channel_id: int):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()

    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.VoiceChannel):
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(ICECAST_URL))
        await ctx.send(f"Joined {channel.name} and streaming Icecast audio.")
    else:
        await ctx.send("Invalid voice channel ID. Make sure it's a valid voice channel.")

@bot.command()
async def stop(ctx):
    # Stop the stream and disconnect
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        voice_client.stop()
        await voice_client.disconnect()
        await ctx.send("Stream stopped and disconnected.")

bot.run(DISCORD_BOT_TOKEN)
