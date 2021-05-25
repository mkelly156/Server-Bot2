{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import discord\n",
    "from discord.ext import commands, tasks\n",
    "import wikipedia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class math:\n",
    "    def __init__(self, bot):\n",
    "        self.bot = bot\n",
    "        \n",
    "    def setup(bot):\n",
    "        bot.add_cog(math(bot))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command()\n",
    "async def add(ctx, a: int, b:int):\n",
    "    answer= (a+b)\n",
    "    await ctx.send(answer)\n",
    "    \n",
    "@commands.command()\n",
    "async def subtract(ctx, a: int, b:int):\n",
    "    answer= (a-b)\n",
    "    await ctx.send(answer)\n",
    "    \n",
    "@commands.command()\n",
    "async def multiply(ctx, a: int, b:int):\n",
    "    answer= (a*b)\n",
    "    await ctx.send(answer)\n",
    "    \n",
    "@commands.command()\n",
    "async def divide(ctx, a: int, b:int):\n",
    "    answer= (a/b)\n",
    "    await ctx.send(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command()\n",
    "async def Fahrenheit(ctx, int):\n",
    "    answer= (int * (9/5) + 32)\n",
    "    await ctx.send(answer)\n",
    "@commands.command()\n",
    "async def Celsius(ctx, int):\n",
    "    answer= (int - 32) * (5/9)\n",
    "    await ctx.send(answer)\n",
    "@commands.command()\n",
    "async def pounds(ctx, int):\n",
    "    answer= (int / 2.205)\n",
    "    await ctx.send(answer)\n",
    "@commands.command(aliases=['kilogram'])\n",
    "async def kg(ctx, int):\n",
    "    answer= (int * 2.205)\n",
    "    await ctx.send(answer)\n",
    "@commands.command()\n",
    "async def feet(ctx, int):\n",
    "    answer= (int/3.281)\n",
    "    await ctx.send(answer)\n",
    "@commands.command()\n",
    "async def meters(ctx, int):\n",
    "    answer= (int*3.281)\n",
    "    await ctx.send(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-6-fe9f115756ea>, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-6-fe9f115756ea>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    async def definition(ctx, word)\u001b[0m\n\u001b[0m                                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "@commands.command()\n",
    "async def article(ctx, word):\n",
    "    summary= wikipedia.summary(word)\n",
    "    link= \n",
    "    embed=discord.Embed(title= \"\")\n",
    "    await ctx.send(summary)\n",
    "\n",
    "\n",
    "@commands.command()\n",
    "async def definition(ctx, word):\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command()\n",
    "async def translate"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
