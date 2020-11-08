"""
haha gonna implement this soon
"""

import discord
from discord.ext import commands  # Imports discord extensions.
import os

os.chdir(r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\Community Bot")
intents = discord.Intents.all()

# NOTE: The below code verifies the "client".
bot = commands.Bot(command_prefix='$', description='- shows this message', intents=intents)


def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)


# NOTE: EMERGENCY CMD
@bot.command()
async def load(ctx, extension):
    """- loads a module. Use in case of emergency. Also good for Debugging."""
    bot.load_extension(extension)


@bot.command()
async def unload(ctx, extension):
    """- unloads a module. Use in case of emergency. Also good for Debugging."""
    bot.unload_extension(extension)


# MinorNote: Hey look, FINALLY. A normal command!
@bot.command()
async def changestatus(ctx, status):
    """- changes the bot status"""
    if status.lower() == 'invisible':
        await bot.change_presence(status=discord.Status.invisible)
        await ctx.send('Bot status set to invisible')
    elif status.lower() == 'online':
        await bot.change_presence(status=discord.Status.online)
        await ctx.send('Bot status set to online')
    elif status.lower() == 'dnd' or status.lower() == 'do_not_disturb':
        await bot.change_presence(status=discord.Status.dnd)
        await ctx.send('Bot status set to do not disturb')
    elif status.lower() == 'idle':
        await bot.change_presence(status=discord.Status.idle)
        await ctx.send('Bot status set to idle')


@bot.command()
async def pythonlogo(ctx):
    # python_file = discord.File(filename=)
    pass

# @bot.command()
# async def commands(ctx, request):
#     if request == 'load':
#         await ctx.send('```Load\nThis command loads a cog. \n\nExample: (pref)load cogs.(cog name)')

# for filename in os.listdir('./cogs'): if filename.endswith('.py'): bot.load_extension(f"cogs.{filename[:-3]}")
extensions = ['cogs.BuiltInCogs']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

    bot.run('NzUzMjk1NzAzMDc3NDIxMDY2.X1kHSw.Wr2GsrjU78H1pqNw92NPmzahicQ')

# NOTE: runs this program. VERY IMPORTANT FOR ME........
# bot.run('NzE5MTk1ODQ2MjYwMDMxNTM5.Xv-9eQ.xIPU-AdK5U-zfW_v_wQ-SrIztoY') # NOTE Aidan's BOT


