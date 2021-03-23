"""
Part of the Core Cog Files, slash.py handles all the new logic for the new slash commands feature.
Since the slash commands feature is so new, some things might not work (especially "this interaction failed"), but that's OK.
I kind of ctrl-c ctrl-v this code, so I might not be that good at making slashes...
"""

from cogs.constants import *
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

guilds = [COMMUNITY_ID, 794887114013540383]


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", description="Checks the bot latency. What else?", guild_ids=guilds)
    async def ping(self, ctx: SlashContext):
        await ctx.respond()
        bot_latency = self.bot.latency * 1000
        embed = discord.Embed(color=BOT_COLOR, title="Latency", description=f"Pong! Bot reaction time: {round(bot_latency)} milliseconds")
        if bot_latency >= 100:
            embed.description = f"**`WARNING 004:`** Pong! Bot reaction time: {round(bot_latency)} milliseconds"
        await ctx.send(embeds=[embed])


def setup(bot):
    bot.add_cog(Slash(bot))
