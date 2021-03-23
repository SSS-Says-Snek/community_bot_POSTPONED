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

    @commands.command(help='COMING SOON!', brief='- removes a string... FROM A STRING????')
    async def remove_string(self, ctx):
        pass

    @commands.command(help='COMING SOON!', brief='- checks if it is a palindrome')
    async def is_palindrome(self, ctx, *, string_to_palindrome):
        if string_to_palindrome == string_to_palindrome[::-1]:
            await ctx.send('OMG ITS A **`PALINDROME`**')
        else:
            await ctx.send('Bruh Y U So Dumb it\'s not a **`palindrome`**')

    # TODOURGENT: Prepare for deprecation. RIP command, you've been a good boy
    @commands.command(help='COMING SOON!', brief='- Plays a Guessing Game with your microphone!')
    async def speech_recog_guess(self, ctx):
        async def recognize_speech_from_mic(recognizer, microphone):
            """Transcribe speech from recorded from `microphone`.

                Returns a dictionary with three keys:
                "success": a boolean indicating whether or not the API request was successful

                "error": `None` if no error occurred, otherwise a string containing
                        an error message if the API could not be reached or
                        speech was unrecognizable
                "transcription": `None` if speech could not be transcribed,
                        otherwise a string containing the transcribed text
                """

            # this will check that Recognizer and Microphone are appropriate types
            if not isinstance(recognizer, sr.Recognizer):
                await ctx.send('**`PYTHONERROR 1431:`** **recognizer** must be **RECOGNIZER** instance')
            if not isinstance(microphone, sr.Microphone):
                await ctx.send('**`PYTHONERROR 1431:`** **microphone** must be **MICROPHONE** instance')

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            response = {
                "success": True,
                "error": None,
                "transcription": None,
            }

            try:
                response["transcription"] = recognizer.recognize_google(audio)
            except sr.RequestError:
                # API says No U or become offline
                response["success"] = False
                response["error"] = "API unavailable"
            except sr.UnknownValueError:
                # Yur speech so bad that speech recognization gave up
                response["error"] = "Unable to recognize speech"

            return response

        WORDS = ['apple', 'banana', 'grape', 'orange', 'mango', 'lemon', 'delicious', 'apartment', 'cheese', 'ketchup',
                 'dinosaur', 'python']
        NUM_GUESSES = 6
        PROMPT_LIMIT = 5

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        word = random.choice(WORDS)

        instructions = (
            f"I'm thinking of one of these words: \n"
            f"{WORDS}\n"
            f"You have {NUM_GUESSES} tries to guess which one.\n"
        )

        await ctx.send(instructions)
        time.sleep(3)

        for i in range(NUM_GUESSES):
            # get guess from user
            # if transcription is return, break loop and continue
            # if no transcription and API says No U, break and continue
            # if API request succeed but no transcription,
            # reprompt user to say guess again. Do this up to PROMPT_LIMIT times
            for _ in range(PROMPT_LIMIT):
                await ctx.send(f"Guess {i + 1}. Speak!")
                guess = await recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                await ctx.send("I didn't catch that. What did you say?\n")

            if guess["error"]:
                await ctx.send("**`ERROR ???:`** {}".format(guess["error"]))
                break

            await ctx.send(f"You said: **`{guess['transcription']}`**")

            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = i < NUM_GUESSES - 1

            if guess["transcription"].lower() in WORDS:
                if guess_is_correct:
                    await ctx.send("**`CORRECT!!`** You win!".format(word))
                    break
                elif user_has_more_attempts:
                    await ctx.send("**`Incorrect.`** Try again.\n")
                else:
                    await ctx.send(f"Sorry, you ***_`LOSE!`_***\nI was thinking of {word}")
                    break
            elif guess["transcription"].lower() == 'cancel':
                break
            else:
                await ctx.send(f"**`{guess['transcription']}`** is not in **`AVAILABLE WORDS`**. Try again!")


def setup(bot):
    bot.add_cog(ExtraFunCommands(bot))
