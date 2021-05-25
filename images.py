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
    "import aiohttp\n",
    "import os\n",
    "import requests\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class images(commands.Cog):\n",
    "    def __init__(self, bot):\n",
    "        self.bot = bot\n",
    "        self.ses = bot.aiohttp_session\n",
    "    def setup(bot):\n",
    "        bot.add_cog(images(bot))\n",
    "        \n",
    "@commands.command       \n",
    "@commands.cooldown(rate=2, per=3)\n",
    "async def dog(ctx):\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        request = await session.get('https://some-random-api.ml/img/dog') # Make a request\n",
    "        dogjson = await request.json() # Convert it to a JSON dictionary\n",
    "        embed = discord.Embed(title=\"Doggo!\", color=discord.Color.purple()) # Create embed\n",
    "        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key\n",
    "        await ctx.send(embed=embed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command(aliases=['image'])\n",
    "@commands.cooldown(rate=2, per=3)\n",
    "async def image(ctx, *, search):\n",
    "    search=search.replace(' ', '')\n",
    "    url= f'https://source.unsplash.com/photos/random/?query={search}&content_filter=high&client_id={id}'\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        if r.status in range(200, 299):\n",
    "                try:\n",
    "                    data = await request.json()\n",
    "                    image_url = data['url'] ['regular']\n",
    "                    embed = discord.Embed(\n",
    "                        title='Snap!',\n",
    "                        color=color,\n",
    "                        description=f'[Link]({image_url})'\n",
    "                    )\n",
    "                    embed.set_image(url=image_url['link'])\n",
    "                    await ctx.send(embed=embed)\n",
    "                except IndexError:\n",
    "                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Image not found.', color=color))\n",
    "        else:\n",
    "            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Response: {r.status}.', color=color))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
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
