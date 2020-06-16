import discord
import random
from discord.ext import commands

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
    await bot.close()

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
    await ctx.send("Commands: .hi \n .magic8ball *question* \n .magicconch *question*")
    await bot.close()

bot.run('NzE4NjI2Mzg5OTg4ODY4MTM3.Xtrngw.PdakAJlzDzZq1mZuKdUKRp2_W7A')