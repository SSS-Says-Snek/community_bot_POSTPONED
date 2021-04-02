"""
Part of the Core Cog Files, slash.py handles all the new logic for the new slash commands feature.
Since the slash commands feature is so new, some things might not work (especially "this interaction failed"), but that's OK.
I kind of ctrl-c ctrl-v this code, so I might not be that good at making slashes...
"""

from cogs.constants import *
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from cogs.BuiltInCogs import check_failure_reason

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

    @cog_ext.cog_slash(name="clear", description="Clears some messages in the channel",
                       options=[
                           create_option(name="messages", description="The number of messages to clear", option_type=4, required=True)
                       ], guild_ids=guilds)
    async def clear(self, ctx: SlashContext, messages: int):
        num_purge_actions, remainder = divmod(messages, 100)
        if isinstance(ctx.channel, discord.TextChannel) and ctx.author.roles:
            for _ in range(num_purge_actions):
                await ctx.channel.purge(limit=100)
            await ctx.channel.purge(limit=remainder)
            cleared_embed = discord.Embed(color=discord.Color.green(),
                                          description=f"Successfully cleared {str(messages)} "
                                                      f"{f'message' if messages == 1 else 'messages'}!")
            cleared_embed.set_author(name=f"Cleared {str(messages)} {f'message' if messages == 1 else 'messages'}", icon_url=CHECK_MARK)
            await ctx.send(embeds=[cleared_embed])


def setup(bot):
    bot.add_cog(Slash(bot))
