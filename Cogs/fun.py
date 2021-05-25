{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import discord\n",
    "from discord.ext import commands, tasks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class fun:\n",
    "    def __init__(self, bot):\n",
    "        self.bot = bot\n",
    "        \n",
    "    def setup(bot):\n",
    "        bot.add_cog(fun(bot))\n",
    "        \n",
    "@commands.command(aliases=['8ball'])\n",
    "async def eightball(ctx, *, question):\n",
    "    responses= ['It is certain.',\n",
    "                'It is decidedly so.',\n",
    "                'Without a doubt',\n",
    "                'Yes, definitely',\n",
    "                'You may rely on it',\n",
    "                'As I see it',\n",
    "                'Yes',\n",
    "                'Most likely',\n",
    "                'Outlook good',\n",
    "                'Signs point to yes',\n",
    "                \"Don't count on it\",\n",
    "                'My reply is no',\n",
    "                'My sources say no',\n",
    "                'Outlook not so good',\n",
    "                'Very doubtful',\n",
    "                'Reply hazy',\n",
    "                'Try again',\n",
    "                'Ask again later']\n",
    "    await ctx.send(f'{random.choice(responses)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command\n",
    "async def parrot(ctx, *args):\n",
    "    await ctx.send(' '.join(args))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command\n",
    "async def slap(ctx, member:discord.User=None):\n",
    "    if (member == ctx.message.author or member == None):\n",
    "        embed=discord.Embed(description= f\"{ctx.message.author.mention} stabs themselves!\")\n",
    "    else:\n",
    "         embed=discord.Embed(description= f\"{ctx.message.author.mention} slaps {member.mention}!\")\n",
    "         embed.set_image(url=\"https://i.ytimg.com/vi/yCx1eAELN1s/maxresdefault.jpg\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
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
