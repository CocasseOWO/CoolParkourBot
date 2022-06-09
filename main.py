from itertools import product
import time
import discord
from discord.ext import commands
#from webserver import keep_alive
#import os

client = commands.Bot(command_prefix='_', help_command=None, )


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='_help'))
    print("bot démarré avec le nom de {0.user}".format(client))


# sprint
def sprint(x):
    return ((x * 0.6 * 0.91) + (0.1 * (1.3 * 0.98) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))


# stop
def stop(x):
    return ((x * 0.6 * 0.91) + (0.1 * (0 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))


# walkback
def walkback(x):
    return ((x * 0.6 * 0.91) + (0.1 * (1 * 0.98) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))


# sneak
def sneak(x):
    return ((x * 0.6 * 0.91) + (0.1 * (0.3 * 0.98) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))


# sneakback
def sneakback(x):
    return ((x * 0.6 * 0.91) + (0.1 * (0.3 * 0.98) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))


# walkback45
def walkback45(x):
    return ((x * 0.6 * 0.91) + (0.1 * (1 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))


# sprint45
def sprint45(x):
    return ((x * 0.6 * 0.91) + (0.1 * (1.3 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))


# sneak45
def sneak45(x):
    return ((x * 0.6 * 0.91) + (
            0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))


# sneakback45
def sneakback45(x):
    return ((x * 0.6 * 0.91) + (
            0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))



@client.command()
async def ibf(ctx, inputs, goal, precision):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    inputs = int(inputs)
    precision = int(precision)
    goal = float(goal)
    await ctx.send('Running...')
    async with ctx.typing():
        start_time = time.time()
        rn = 0
        functions_list = [stop, sprint, walkback, sneakback, sneak,]

        if inputs < 10:

            if 6 <= precision <= 16:
                pr = 1 / 10 ** precision
            else:
                await ctx.send('Precision have to be between 6 and 16')

            def functions_product(f, start=0):
                for func in f:
                    start = func(start)
                return start

            for i in product(functions_list, repeat=int(inputs)):
                if abs(functions_product(i) - goal) < float(pr):
                    await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
                    rn = rn + 1
            if rn == 0:
                await ctx.send(
                    "--- Results took %s seconds to generate but sadly, nothing was found :(" % (
                                time.time() - start_time))
            else:
                await ctx.send("--- Results took %s seconds to generate" % (time.time() - start_time))
        else:
            await ctx.send('Ticks number have to be between 0 and 9 !')
    await ctx.send('Done !')



@client.command()
async def ibf45(ctx, inputs, goal, precision):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    inputs = int(inputs)
    precision = int(precision)
    goal = float(goal)
    await ctx.send('Running...')
    async with ctx.typing():
        start_time = time.time()
        rn = 0
        functions_list = [stop, sneak45, sneakback45, sprint45, walkback45]

        if inputs < 10:

            if 6 <= precision <= 16:
                pr = 1 / 10 ** precision
            else:
                await ctx.send('Precision have to be between 6 and 16')

            def functions_product(f, start=0):
                for func in f:
                    start = func(start)
                return start

            for i in product(functions_list, repeat=int(inputs)):
                if abs(functions_product(i) - goal) < float(pr):
                    await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
                    rn = rn + 1
            if rn == 0:
                await ctx.send(
                    "--- Results took %s seconds to generate but sadly, nothing was found :(" % (
                                time.time() - start_time))
            else:
                await ctx.send("--- Results took %s seconds to generate" % (time.time() - start_time))
        else:
            await ctx.send('Ticks number have to be between 0 and 9 !')
    await ctx.send('Done !')



@client.command()
async def help(ctx):
    embed = discord.Embed(title=" ", color=0xff7b00)
    embed.set_author(name="Help", icon_url="https://s2.coinmarketcap.com/static/img/coins/200x200/14481.png")
    embed.add_field(name="_ibf", value="Bruteforce all possible inputs for a straight momentum.",
                    inline=True)
    embed.add_field(name="_ibf45",
                    value="Bruteforce all possible inputs for a facing 45 momentum.", inline=True)
    embed.set_footer(text="Made by Cocasse")
    await ctx.send(embed=embed)




#keep_alive()

client.run('TOKEN_HERE')
