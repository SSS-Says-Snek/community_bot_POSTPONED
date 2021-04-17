"""
Part of the Core Cog Files, slash.py handles all the new logic for the new slash commands feature.
Since the slash commands feature is so new, some things might not work (especially "this interaction failed"), but that's OK.
I kind of ctrl-c ctrl-v this code, so I might not be that good at making slashes...
"""

from cogs.constants import *
from cogs.utility import *

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

import os
import arrow

guilds = [COMMUNITY_ID, 794887114013540383]


def is_trusted():
    """checks if the author that called the command is trusted"""

    async def predicate(ctx):
        """the predicate of the command"""
        author_roles = [role for role in ctx.author.roles if role.name != "@everyone"]
        for role in author_roles:
            if role.id in TRUSTED_ROLES:
                return True
        nope_embed = discord.Embed(color=discord.Color.red(),
                                   description="Permission is denied, as you do not have one of the following roles:\n"
                                               f"{FSTRING_NL.join([f'**{discord.utils.get(ctx.guild.roles, id=role_id).name}**' for role_id in TRUSTED_ROLES])}\n"
                                               f"To run this command, you must need one ore more of these roles.")
        nope_embed.set_author(name="Access denied", icon_url=X_MARK)
        await ctx.send(embed=nope_embed)
        return False

    return commands.check(predicate)


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
    @is_trusted()
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

    @cog_ext.cog_slash(name="load_all_cogs", description="Loads all available cogs", guild_ids=guilds)
    @is_trusted()
    async def load_all_cogs(self, ctx: SlashContext):
        # async with ctx.channel.typing():
        load_cog_embed = discord.Embed(color=discord.Color.green(), description='')
        num_errors = 0
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and filename not in SKIP_EXTENSION_LOAD:
                try:
                    self.bot.load_extension(f"cogs.{filename[:-3]}")
                except Exception as e:
                    print("uhoh")
                    print(load_cog_embed.description, type(load_cog_embed.description))
                    load_cog_embed.description += f"**Error** Loading cogs.{filename[:-3]}: {type(e).__name__}\n"
                    num_errors += 1
                    # await ctx.send(f'**`SUCCESS:`** Successfully loaded cogs.{filename[:-3]}')
                else:
                    load_cog_embed.description += f"**Success!** Successfully loaded cogs.{filename[:-3]}\n"
        if num_errors == 0:
            load_cog_embed.set_author(name="Successfully loaded all cogs", icon_url=CHECK_MARK)
        else:
            load_cog_embed.set_author(name=f"{num_errors} {f'error' if num_errors == 1 else 'error'} while loading cogs", icon_url=X_MARK)
        await ctx.send(embeds=[load_cog_embed])

    @cog_ext.cog_slash(name="whois", description="Gives you information about someone",
                       options=[
                           create_option(name="user context", description="The user context", option_type=3, required=False)
                       ], guild_ids=guilds)
    async def whois(self, ctx: SlashContext, *, user_context=None):
        """
        COMING SOON!
        """
        user = None
        error = discord.Embed(color=discord.Color.red(), title="ERROR",
                              description=r'BRUH YOU DUMEHEAD, that user does \*NOT\* exist. Get lost, you useless entity')
        if user_context:
            if is_string_id(user_context):
                user_mode = 'mention'
            elif user_context.isdigit():
                user_mode = 'id'
            elif is_discord_username(user_context):
                user_mode = "username"
            else:
                user_mode = None
                user = None
                error.description = "BRUH YOU DUMEHEAD, we couldn't identify your **QUESTIONABLE** user context. Please try again, " \
                                    "you useless entity\n(either by ID, Username+Discriminator, or by mention)"
                await ctx.send(embed=error)
            if user_mode == 'mention':
                try:
                    user = await self.bot.fetch_user(user_context[3:-1])
                except discord.errors.NotFound:
                    await ctx.send(embed=error)
                    user = None
                else:
                    user = ctx.guild.get_member(int(user_context[3:-1]))
            elif user_mode == 'id':
                try:
                    user = await self.bot.fetch_user(int(user_context))
                except discord.errors.NotFound:
                    await ctx.send(embed=error)
                    user = None
                else:
                    if is_member(ctx.guild, user):
                        user = ctx.guild.get_member(int(user_context))
            elif user_mode == 'username':
                # Only supports members in the server
                username, discriminator = user_context.split("#")
                # Gets user by Username+Discriminator, returns None otherwise
                user = discord.utils.get(self.bot.get_all_members(), name=username, discriminator=discriminator)
                if not user:
                    error.description = 'BRUH YOU DUMEHEAD, that user either:\n' \
                                        'Does \\*NOT\\* share a server with ME, OR\n' \
                                        'Does \\*NOT\\* exist. Get lost, you useless entity'
                    await ctx.send(embed=error)
        else:
            user = ctx.guild.get_member(ctx.author.id)

        if user:

            # Sorry for the poopy code
            cursor.execute("SELECT * FROM members")
            stuff = cursor.fetchall()
            good_members_dict = mysql_to_dict_id_as_key_info_as_dict(stuff, [i[0] for i in cursor.description])
            all_members_info = mysql_to_dict(stuff, [i[0] for i in cursor.description])
            # just some avatar stuff below
            avatar_url_png = str(user.avatar_url_as(static_format='png', size=512))
            avatar_url_jpg = str(user.avatar_url_as(static_format='jpg', size=512))
            avatar_url_web = str(user.avatar_url_as(static_format='webp', size=512))

            time_created = user.created_at.strftime(DEFAULT_DATETIME_FORMAT)
            user_embed = discord.Embed(description=f"{user.mention} ({user.id})",
                                       color=(0x34ebc0 if not isinstance(user, discord.member.Member) else user.color))
            user_embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=avatar_url_png)
            user_embed.set_thumbnail(url=avatar_url_png)
            user_embed.add_field(name="Username", value=discordify(user.name), inline=True)
            user_embed.add_field(name="Time Created (UTC)", value=f"{time_created}\n({arrow.get(user.created_at).humanize(arrow.now())})",
                                 inline=(True if isinstance(user, discord.member.Member) else False))
            trust_id = list(TRUST_COMMENTS.keys())

            if user.id in trust_id:
                trust = TRUST_COMMENTS[user.id]
            else:
                trust = None

            if isinstance(user, discord.member.Member):
                cursor.execute('SELECT overall_infractions FROM members WHERE id=%(id)s', {"id": user.id})
                unnecessarily_compact_infractions = cursor.fetchall()
                infractions = unnecessarily_compact_infractions[0][0]

                if user.id in trust_id:
                    trust = TRUST_COMMENTS[user.id]
                elif 0 <= infractions <= 3:
                    trust = 'High'
                elif 4 <= infractions <= 6:
                    trust = 'Medium'
                elif 7 <= infractions <= 9:
                    trust = 'Medium-Low'
                elif 10 <= infractions <= 12:
                    trust = 'Low'
                elif 13 <= infractions <= 14:
                    trust = 'None'
                else:
                    trust = 'So low that it\'s even lower than your grades and your chances of getting married multiplied'

                time_joined = user.joined_at.strftime(DEFAULT_DATETIME_FORMAT)
                user_embed.add_field(name="Time Joined (UTC)", value=f"{time_joined}\n({arrow.get(user.joined_at).humanize(arrow.now())})",
                                     inline=True)
                if user.nick is not None:
                    user_embed.add_field(name="Nickname", value=discordify(user.nick), inline=False)
                user_roles = user.roles
                user_roles.reverse()
                user_roles_mention = [role.mention for role in user_roles if role.name != '@everyone']
                user_embed.add_field(name=f"Roles ({len(user_roles) - 1})", value='  '.join(user_roles_mention), inline=False)
            if isinstance(user, discord.member.Member):
                cursor.execute("SELECT id, messages_sent FROM members ORDER BY messages_sent DESC")
                messages_sent = cursor.fetchall()
                if messages_sent:
                    messages_sent_dict = dict([(temp[0], temp[1]) for temp in messages_sent])
                    messages_sent_dict_values = list(messages_sent_dict.values())
                    user_messages_sent = messages_sent_dict[user.id]
                    messages_sent_place = messages_sent_dict_values.index(user_messages_sent) + 1
                else:
                    user_messages_sent = "No Data"
                    messages_sent_place = "?"

                date_members_joined_list = sorted(all_members_info["date_joined"])
                cursor.execute("SELECT date_joined FROM members WHERE id=%(id)s", {"id": user.id})
                table_user_date_joined = cursor.fetchall()
                try:
                    table_user_date_joined = table_user_date_joined[0][0]
                except IndexError:
                    pass
                try:
                    xp_place = sorted(all_members_info["xp"], reverse=True).index(good_members_dict[user.id]["xp"]) + 1
                except ValueError:
                    xp_place = '?'
                try:
                    date_joined_place = date_members_joined_list.index(table_user_date_joined) + 1
                except ValueError:
                    date_joined_place = "?"
                user_embed.add_field(name="Server Info", value=f"Trust? {trust}\n"
                                                               f"Messages: {user_messages_sent} "
                                                               f"({inflect_engine.ordinal(messages_sent_place)})\n"
                                                               f"XP: {good_members_dict[user.id]['xp']} "
                                                               f"({inflect_engine.ordinal(xp_place)})\n"
                                                               f"{inflect_engine.ordinal(date_joined_place)} member joined",
                                     inline=True)
            user_embed.add_field(name="Miscellaneous",
                                 value=f"Bot? {user.bot}\nSystem? {user.system}"
                                       f"{f'{FSTRING_NL}Trust? {trust}' if trust and not isinstance(user, discord.member.Member) else ''}",
                                 inline=True)
            user_embed.add_field(name="Avatar as", value=f"[png]({avatar_url_png}) | "
                                                         f"[jpg]({avatar_url_jpg}) | "
                                                         f"[webp]({avatar_url_web})", inline=True)
            if isinstance(user, discord.member.Member):
                user_embed.set_footer(text=f"Made with ♥ in discord.py")
            else:
                user_embed.set_footer(text="Information may be limited when user is not in server | Made with ♥ in discord.py")
            await ctx.send(embed=user_embed)


def setup(bot):
    bot.add_cog(Slash(bot))
