import discord
from discord.ext import commands
import time
import random
from .constants import *


class ExtraCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # FIXME: When importing the cog, this won't load because "something...."
    @commands.command(pass_context=True)
    @commands.has_permissions(add_reactions=True, embed_links=True)
    async def advanced_help(self, ctx, *cog):
        """- Gets all cogs and commands of mine."""
        try:
            if not cog:
                """Cog listing.  What more?"""
                halp = discord.Embed(title='Cog Listing and Uncategorized Commands',
                                     description='Use `$help *cog*` to find out more about them!\n(By The Way, '
                                                 'The Cog Name Must Be in Title Case, Just Like this Sentence.)')
                cogs_desc = ''
                for x in self.bot.cogs:
                    cogs_desc += ('{} - {}'.format(x, self.bot.cogs[x].__doc__) + '\n')
                halp.add_field(name='Cogs', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
                cmds_desc = ''
                for y in self.bot.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{}  {}'.format(y.name, y.help) + '\n')
                halp.add_field(name='Uncategorized Commands', value=cmds_desc[0:len(cmds_desc) - 1], inline=False)
                await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('', embed=halp)
            else:
                """Helps me remind you if you pass too many args."""
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!', description='That is way too many cogs!',
                                         color=discord.Color.red())
                    await ctx.message.author.send('', embed=halp)
                else:
                    """Command listing within a cog."""
                    found = False
                    for x in self.bot.cogs:
                        for y in cog:
                            if x == y:
                                halp = discord.Embed(title=cog[0] + ' Command Listing',
                                                     description=self.bot.cogs[cog[0]].__doc__)
                                for c in self.bot.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name, value=c.help, inline=False)
                                found = True
                    if not found:
                        """Reminds you if that cog doesn't exist."""
                        halp = discord.Embed(title='Error!', description=f"The cog {cog[0]} does not exist.",
                                             color=discord.Color.red())
                    else:
                        await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.author.send('', embed=halp)
        except:
            await ctx.send("Excuse me, I can't send embeds.")

    @commands.command()
    @commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')
    async def old_draw(self, ctx):
        """- old draw version that draws a person for #random-draw"""
        people_enter = ['Brandon Cui', 'Aidan Cui', 'Jason Murong', 'Daniel Collins', 'Daniel Murong', 'Zombix',
                        'FluffyDuck01', 'Lucas Joiner', 'Grayson Bou', 'Anna An']
        rand_reward = ['access to a secret category', 'a random role', 'Discord Dungeons Money',
                       'Villager Bot Money', 'the ability to be immune to slowmode (temporary)',
                       'owner of the server for ? hours', 'Myuu PKC']
        actual_rand_reward = random.randint(1, len(rand_reward))
        lucky_person = random.randint(1, len(people_enter))
        index_person = 1
        index_reward = 1

        time.sleep(0.7)
        await ctx.channel.purge(limit=1)
        time.sleep(0.3)
        for person in people_enter:
            if lucky_person == index_person:
                await ctx.send(f"\nThe lucky winner is {person}!")
                time.sleep(0.8)
                await ctx.send("Choosing random reward...")
                time.sleep(random.randint(1, 3))
                for reward in rand_reward:
                    if actual_rand_reward == index_reward:
                        await ctx.send(f"{person} won {reward.lower()}!")
                        break
                    else:
                        index_reward += 1
                    break
                else:
                    index_person += 1

    @commands.command(help='COMING SOON!', brief='- gives a summary about a user')
    async def old_get_user(self, ctx, user_context):
        # Eww the old get_user.. but oh well
        try:
            try:
                user = await self.bot.fetch_user(int(user_context))
            except discord.errors.NotFound:
                await ctx.send(r'**`ERROR: `** BRUH YOU DUMEHEAD, that user does \*NOT\* exist. Get lost, you useless entity')
        except ValueError:
            try:
                user = await self.bot.fetch_user(user_context[3:-1])
            except discord.errors.NotFound:
                await ctx.send(r'**`ERROR: `** BRUH YOU DUMEHEAD, that user does \*NOT\* exist. Get lost, you useless entity')
        if user:
            time_created = user.created_at
            time_created = time_created.strftime(DEFAULT_DATETIME_FORMAT)
            avatar = user.avatar_url_as(size=512)
            send_to_user = f"**`SUCCESS`** Successfully retrieved user. Here are some basic information...\n" \
                           f"**`USER NAME: `** {user.name}\n" \
                           f"**`USER DISCRIMINATOR: `** {str(user.discriminator)}\n" \
                           f"**`NICKNAME: `** {user.display_name}\n" \
                           f"**`BOT? `** {user.bot}\n" \
                           f"**`TIME CREATED (UTC): `** {time_created}\n"
            # TODOURGENT: How do you find if a person is in a bot guild
            send_to_user += f"**`AVATAR: `** {avatar}"
            await ctx.send(send_to_user)
        else:
            await ctx.send(rf"BRUH YOU DUMBO. {user_context} does \*NOT\* exist. Get lost, you useless entity")


# NOTE: IMPORTANT
def setup(bot):
    bot.add_cog(ExtraCommands(bot))
