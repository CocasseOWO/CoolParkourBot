from itertools import product
import time
import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix='_', help_command=None, )


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='_help'))
    print("bot démarré avec le nom de {0.user}".format(client))


@client.command()
async def ibf(ctx):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    await ctx.send('How many ticks do you want to bruteforce ?')
    inputs = await client.wait_for('message', check=check)
    inputs = int(inputs.content)
    if inputs < 10:
        await ctx.send('What goal speed do you want ?')
        goal = await client.wait_for('message', check=check)
        goal = float(goal.content)
        await ctx.send('What speed precision do you need ?')
        precision = await client.wait_for('message', check=check)
        precision = int(precision.content)

        await ctx.send('Running...')
        start_time = time.time()

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

        functions_list = [stop, sprint, walkback, sneakback, sneak]

        if precision == 5:
            pr = 0.00001
        elif precision == 6:
            pr = 0.000001
        elif precision == 7:
            pr = 0.0000001
        elif precision == 8:
            pr = 0.00000001
        elif precision == 9:
            pr = 0.000000001
        elif precision == 10:
            pr = 0.0000000001
        elif precision == 11:
            pr = 0.00000000001
        elif precision == 12:
            pr = 0.000000000001
        elif precision == 13:
            pr = 0.0000000000001
        elif precision == 14:
            pr = 0.00000000000001
        elif precision == 15:
            pr = 0.000000000000001
        elif precision == 16:
            pr = 0.0000000000000001
        else:
            await ctx.send('Precision have to be between 5 and 16')

        def functions_product(f, start=0):
            for func in f:
                start = func(start)
            return start

        for i in product(functions_list, repeat=int(inputs)):
            if abs(functions_product(i) - goal) < float(pr):
                await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
        await ctx.send("--- Results took %s seconds to generate ---" % (time.time() - start_time))
        await ctx.send('Done !')

    else:
        await ctx.send('Ticks number have to be between 0 and 9 !, if you want to calculate more ticks, you can run the program in your own computer (https://anonfiles.com/n6C0van5y9/bruteforce_straight_py)')


@client.command()
async def inputbruteforce(ctx):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    await ctx.send('How many ticks do you want to bruteforce ?')
    inputs = await client.wait_for('message', check=check)
    inputs = int(inputs.content)

    if inputs < 10:
        await ctx.send('What goal speed do you want ?')
        goal = await client.wait_for('message', check=check)
        goal = float(goal.content)
        await ctx.send('What speed precision do you need ?')
        precision = await client.wait_for('message', check=check)
        precision = int(precision.content)

        await ctx.send('Running...')
        start_time = time.time()

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

        functions_list = [stop, sprint, walkback, sneakback, sneak]

        if precision == 5:
            pr = 0.00001
        elif precision == 6:
            pr = 0.000001
        elif precision == 7:
            pr = 0.0000001
        elif precision == 8:
            pr = 0.00000001
        elif precision == 9:
            pr = 0.000000001
        elif precision == 10:
            pr = 0.0000000001
        elif precision == 11:
            pr = 0.00000000001
        elif precision == 12:
            pr = 0.000000000001
        elif precision == 13:
            pr = 0.0000000000001
        elif precision == 14:
            pr = 0.00000000000001
        elif precision == 15:
            pr = 0.000000000000001
        elif precision == 16:
            pr = 0.0000000000000001
        else:
            await ctx.send('Precision have to be between 5 and 16')

        def functions_product(f, start=0):
            for func in f:
                start = func(start)
            return start

        for i in product(functions_list, repeat=int(inputs)):
            if abs(functions_product(i) - goal) < float(pr):
                await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
        await ctx.send("--- Results took %s seconds to generate ---" % (time.time() - start_time))
        await ctx.send('Done !')
    else:
        await ctx.send('Ticks number have to be between 0 and 9 !, if you want to calculate more ticks, you can run the program in your own computer (https://anonfiles.com/n6C0van5y9/bruteforce_straight_py)')


@client.command()
async def ibf45(ctx):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    await ctx.send('How many ticks do you want to bruteforce ?')
    inputs = await client.wait_for('message', check=check)
    inputs = int(inputs.content)

    if inputs < 10:
        await ctx.send('What goal speed do you want ?')
        goal = await client.wait_for('message', check=check)
        goal = float(goal.content)
        await ctx.send('What speed precision do you need ?')
        precision = await client.wait_for('message', check=check)
        precision = int(precision.content)

        await ctx.send('Running...')
        start_time = time.time()

        # sneak45
        def sneak45(x):
            return ((x * 0.6 * 0.91) + (
                    0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # sneakback45
        def sneakback45(x):
            return ((x * 0.6 * 0.91) + (
                    0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))

        # sprint45
        def sprint45(x):
            return ((x * 0.6 * 0.91) + (0.1 * (1.3 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # stop
        def stop(x):
            return ((x * 0.6 * 0.91) + (0.1 * (0 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # walkback45
        def walkback45(x):
            return ((x * 0.6 * 0.91) + (0.1 * (1 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))

        functions_list = [stop, sprint45, walkback45, sneak45, sneakback45]

        if precision == 5:
            pr = 0.00001
        elif precision == 6:
            pr = 0.000001
        elif precision == 7:
            pr = 0.0000001
        elif precision == 8:
            pr = 0.00000001
        elif precision == 9:
            pr = 0.000000001
        elif precision == 10:
            pr = 0.0000000001
        elif precision == 11:
            pr = 0.00000000001
        elif precision == 12:
            pr = 0.000000000001
        elif precision == 13:
            pr = 0.0000000000001
        elif precision == 14:
            pr = 0.00000000000001
        elif precision == 15:
            pr = 0.000000000000001
        elif precision == 16:
            pr = 0.0000000000000001
        else:
            await ctx.send('Precision have to be between 5 and 16')

        def functions_product(f, start=0):
            for func in f:
                start = func(start)
            return start

        for i in product(functions_list, repeat=int(inputs)):
            if abs(functions_product(i) - goal) < float(pr):
                await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
        await ctx.send("--- Results took %s seconds to generate ---" % (time.time() - start_time))
        await ctx.send('Done !')
    else:
        await ctx.send('Ticks number have to be between 0 and 9 !, if you want to calculate more ticks, you can run the program in your own computer (https://anonfiles.com/l5D6v6n4y1/bruteforce_45_py)')


@client.command()
async def inputbruteforce45(ctx):
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    await ctx.send('How many ticks do you want to bruteforce ?')
    inputs = await client.wait_for('message', check=check)
    inputs = int(inputs.content)

    if inputs < 10:
        await ctx.send('What goal speed do you want ?')
        goal = await client.wait_for('message', check=check)
        goal = float(goal.content)
        await ctx.send('What speed precision do you need ?')
        precision = await client.wait_for('message', check=check)
        precision = int(precision.content)

        await ctx.send('Running...')
        start_time = time.time()

        # sneak45
        def sneak45(x):
            return ((x * 0.6 * 0.91) + (
                    0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # sneakback45
        def sneakback45(x):
            return ((x * 0.6 * 0.91) + (
                    0.1 * (0.3 * 1.38592929113) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))

        # sprint45
        def sprint45(x):
            return ((x * 0.6 * 0.91) + (0.1 * (1.3 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # stop
        def stop(x):
            return ((x * 0.6 * 0.91) + (0.1 * (0 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / 0.6) ** 3))

        # walkback45
        def walkback45(x):
            return ((x * 0.6 * 0.91) + (0.1 * (1 * 1) * ((1 + 0.2 * 0) * (1 - 0.15 * 0)) * (0.6 / -0.6) ** 3))

        functions_list = [stop, sprint45, walkback45, sneak45, sneakback45]

        if precision == 5:
            pr = 0.00001
        elif precision == 6:
            pr = 0.000001
        elif precision == 7:
            pr = 0.0000001
        elif precision == 8:
            pr = 0.00000001
        elif precision == 9:
            pr = 0.000000001
        elif precision == 10:
            pr = 0.0000000001
        elif precision == 11:
            pr = 0.00000000001
        elif precision == 12:
            pr = 0.000000000001
        elif precision == 13:
            pr = 0.0000000000001
        elif precision == 14:
            pr = 0.00000000000001
        elif precision == 15:
            pr = 0.000000000000001
        elif precision == 16:
            pr = 0.0000000000000001
        else:
            await ctx.send('Precision have to be between 5 and 16')

        def functions_product(f, start=0):
            for func in f:
                start = func(start)
            return start

        for i in product(functions_list, repeat=int(inputs)):
            if abs(functions_product(i) - goal) < float(pr):
                await ctx.send(f'{[f.__name__ for f in i]}: {functions_product(i)}')
        await ctx.send("--- Results took %s seconds to generate ---" % (time.time() - start_time))
        await ctx.send('Done !')
    else:
        await ctx.send('Ticks number have to be between 0 and 9 !, if you want to calculate more ticks, you can run the program in your own computer (https://anonfiles.com/l5D6v6n4y1/bruteforce_45_py)')

@client.command()
async def help(ctx):
    embed = discord.Embed(title=" ", color=0xff7b00)
    embed.set_author(name="Help", icon_url="https://s2.coinmarketcap.com/static/img/coins/200x200/14481.png")
    embed.add_field(name="_inputbruteforce (_ibf)", value="Bruteforce all possible inputs for a straight momentum.",
                    inline=True)
    embed.add_field(name="_inputbruteforce45 (_ibf45)",
                    value="Bruteforce all possible inputs for a facing 45 momentum.", inline=True)
    embed.set_footer(text="Made by Cocasse")
    await ctx.send(embed=embed)


keep_alive()

client.run('TOKEN_HERE')
