"""
haha gonna implement this soon. SOON. SOON. MAYBE SOON
"""

import discord
from discord.ext import commands  # Imports discord extensions.
from discord_slash import SlashCommand, SlashContext
import json
from cogs.constants import *
from cogs.utility import censor

# NOTE: The below code verifies the "client".
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', description='- shows this message', intents=intents)
slash = SlashCommand(bot, sync_commands=True)
PATH_TO_VARIABLES_JSON = r'C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\Community Bot\cogs\json files\variables.json'

with open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\COMMUNITY_TOKEN.txt") as read_token:
    TOKEN = read_token.read().strip()

print(f"Connecting through bot token {censor(TOKEN, num_letter_censor=6, mode='Normal', words_to_censor=None)}")


def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

    return commands.check(predicate)


def is_shutdown():
    """checks if the bot is shutdown or not"""

    with open(PATH_TO_VARIABLES_JSON) as read_var_json:
        suppress_guild_owner_commands = json.load(read_var_json)["shutdown"]

    def predicate(ctx):
        return not suppress_guild_owner_commands

    return commands.check(predicate)


# NOTE: EMERGENCY CMD
@bot.command()
async def load(ctx, extension):
    """- loads a module. Use in case of emergency. Also, good for Debugging."""
    try:
        bot.load_extension(extension)
    except Exception as e:
        await ctx.send(f"**`ERROR:`** {e}")
    else:
        await ctx.send("Success I guess")


@bot.command()
async def unload(ctx, extension):
    """- unloads a module. Use in case of emergency. Also, good for Debugging."""
    bot.unload_extension(extension)


# MinorNote: Hey look, FINALLY.
#  A normal command!
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
    pass
    # python_file = discord.File(filename=)
    # TODO: You know, ADD THE DANG THING


# @bot.command()
# async def commands(ctx, request):
#     if request == 'load':
#         await ctx.send('```Load\nThis command loads a cog. \n\nExample: (pref)load cogs.(cog name)')

# for filename in os.listdir('./cogs'): if filename.endswith('.py'): bot.load_extension(f"cogs.{filename[:-3]}")
pre_loaded_extensions = [
    'cogs.BuiltInCogs',
    'cogs.core.slash'
]

if __name__ == '__main__':
    for ext in pre_loaded_extensions:
        bot.load_extension(ext)
        print(f"Loading pre-loaded cog: {ext}...")

    print('Finished loading all cogs. Preparing to run bot...')
    # NOTE: runs this program. VERY IMPORTANT FOR ME........
    bot.run(TOKEN)
