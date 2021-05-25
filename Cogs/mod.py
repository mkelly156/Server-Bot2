{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import discord\n",
    "from discord.ext import commands\n",
    "\n",
    "class Mod:\n",
    "    def __init__(self, bot):\n",
    "        self.bot = bot\n",
    "    def setup(bot):\n",
    "        bot.add_cog(mod(bot))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "@commands.command()\n",
    "async def kick(ctx, member : discord.Member, *, reason=None):\n",
    "    await member.kick(reason=reason)\n",
    "    \n",
    "@kick.error\n",
    "async def kick_error(error, ctx):\n",
    "    if isinstance(error, commands.MissingPermissions):\n",
    "        await ctx.channel.send(\"Looks like you aren't an admin!\")\n",
    "    elif isinstance (error, commands.BadArgument):\n",
    "        await ctx.channel.send(\"Can't find them\")\n",
    "\n",
    "@commands.command()\n",
    "async def ban(ctx, member : discord.Member, *, reason=None):\n",
    "    await member.ban(reason=reason)\n",
    "    await ctx.send(f'Banned{member.mention}')\n",
    "\n",
    "@commands.command()\n",
    "async def unban(ctx, *, member):\n",
    "    banned_users= await ctx.guild.bans()\n",
    "    member_name, member_discriminator=member.split('#')\n",
    "    \n",
    "    for ban_entry in banned_users:\n",
    "        user=ban_entry.user\n",
    "        \n",
    "        if (user.name, user.discriminator)== (member_name, member_discriminator):\n",
    "            await ctx.guild.unban(user)\n",
    "            await ctx.send(f'Unbanned{user.name}#{user.discriminator}')\n",
    "            \n",
    "@commands.command(pass_context = True)\n",
    "async def mute(ctx, member: discord.Member):\n",
    "    if ctx.message.author.server_permissions.administrator:\n",
    "        role = discord.utils.get(member.server.roles, name='Muted')\n",
    "        await bot.add_roles(member, role)"
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
