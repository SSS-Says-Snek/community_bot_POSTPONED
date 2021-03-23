from discord.ext import commands
import math as m
import numpy as np


class MoreMathCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sin(self, ctx, a: int):
        """- takes the sine of x"""
        await ctx.send(f"The answer is about {round(np.sin(np.deg2rad(a)), 4)}")

    @commands.command()
    async def cos(self, ctx, a: int):
        """- takes the cosine of x"""
        await ctx.send(f"The answer is about {round(np.cos(np.deg2rad(a)), 4)}")

    @commands.command()
    async def tan(self, ctx, a: int):
        """- takes the tangent of x"""
        await ctx.send(f"The answer is about {round(np.tan(np.deg2rad(a)), 4)}")

    @commands.command()
    async def arcsin(self, ctx, a: float):
        """- takes the arcsine of x"""
        await ctx.send(f"The answer is about {round(np.arcsin(a), 4)} in radians")

    @commands.command()
    async def arccos(self, ctx, a: float):
        """- takes the arccosine of x"""
        await ctx.send(f"The answer is about {round(np.arccos(a), 4)} in radians")

    @commands.command()
    async def arctan(self, ctx, a: float):
        """- takes the arctangent of x"""
        await ctx.send(f"The answer is about {round(np.arctan(a), 4)} in radians")

    @commands.command()
    async def factorial(self, ctx, a: int):
        """- takes the factorial of x"""
        await ctx.send(f"The answer is {m.factorial(a)}")

    @commands.command()
    async def combination(self, ctx, x: int, y: int):
        """- takes the combination of x and y"""
        await ctx.send(f"Work in Progress!")


def setup(bot):
    bot.add_cog(MoreMathCommands(bot))
