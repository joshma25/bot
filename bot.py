import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print ('Bot is ready')

@bot.event
async def on_member_join(member):
    print(f'{member} joined the server')

@bot.event
async def on_member_remove(member):
    print(f'{member} left the server')

@bot.command()
async def hi(ctx):
    await ctx.send('Wassup baby')

@bot.command()
async def magic8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\n {random.choice(responses)}')

@bot.command()
async def magicconch(ctx, *, question):
    responses = ["Maybe someday", "Nothing", "Neither", "I don't think so", "No", "Yes", "Try asking again"]
    if question == "Can I have something to eat?":
        await ctx.send(f'Question: {question}\n No')
    elif question == "Can't you say anything but no?":
        await ctx.send(f'Question: {question}\n Try asking again')
    else:
        await ctx.send(f'Question: {question}\n {random.choice(responses)}')

@bot.command()
async def commands(ctx):
    await ctx.send("Commands: .hi \n .magic8ball *question* \n .magicconch *question*").j

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    await voice.disconnect()

@bot.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    if song_there:
        os.remove("song.mp3")
    await ctx.send("beep bop boop boop")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()



bot.run('#code goes here')
