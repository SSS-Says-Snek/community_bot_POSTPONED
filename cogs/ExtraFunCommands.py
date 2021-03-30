""""""
import discord
from discord.ext import commands
import speech_recognition as sr
import time
import random


class ExtraFunCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # FIXME: Finish this code (for Daniel!)
    @commands.command(help='COMING SOON!', brief='- DMS a list of all BFB characters')
    async def bfbcharacters(self, ctx):
        """- DMs a list of all BFB characters"""
        # await ctx.message.author.send('**`list of all BFB Characters`**')
        # await ctx.message.author.send('**`')
        await ctx.send('Sorry! Work in Progress! We\'ll notify you when we fix it!')
        brandon = self.bot.get_user(683852333293109269)
        await brandon.send(f"**`WARNING 003:` {ctx.author.name} has used an INCOMPLETE command. Uh Oh!")

    @commands.command(help='COMING SOON!', brief='- Capitalizes your text randomly! I dunno why...')
    async def randomcaps(self, ctx, *, text_to_be_randomly_caps):
        list_of_text = list(text_to_be_randomly_caps)
        reconstructed_text = ''
        for list_char in list_of_text:
            rand_num = random.randint(0, 1)
            if int(rand_num) == 0:
                reconstructed_text += str(list_char).upper()
            else:
                reconstructed_text += str(list_char).lower()
        await ctx.send(reconstructed_text)

    @commands.command(help='COMING SOON!', brief='- Puts spaces in your text. Requires you saying the amount of spaces')
    async def space_text(self, ctx, num_spaces, *, text_to_be_transcribed_into_spaces):
        list_of_text = list(text_to_be_transcribed_into_spaces)
        reconstructed_text = ''
        for list_char in list_of_text:
            reconstructed_text += list_char + str(int(num_spaces) * ' ')
        await ctx.send(reconstructed_text)

    @commands.command(help='COMING SOON!', brief='- turns text into spoilers for you to frustrate people')
    async def spoiler_text(self, ctx, *, text_to_be_spoiled):
        constructed_text = ''
        for string in text_to_be_spoiled:
            constructed_text += rf"\||{string}\||"
        await ctx.send(constructed_text)

    @commands.command(help='COMING SOON!', brief='- checks if it is a palindrome')
    async def is_palindrome(self, ctx, *, string_to_palindrome):
        if string_to_palindrome == string_to_palindrome[::-1]:
            await ctx.send('OMG ITS A **`PALINDROME`**')
        else:
            await ctx.send('Bruh Y U So Dumb it\'s not a **`palindrome`**')


def setup(bot):
    bot.add_cog(ExtraFunCommands(bot))
