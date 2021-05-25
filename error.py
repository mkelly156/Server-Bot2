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
    "class CommandErrorHandler(commands.Cog):\n",
    "    def __init__(self, bot):\n",
    "        self.bot = bot\n",
    "\n",
    "    def setup(bot):\n",
    "        bot.add_cog(CommandErrorHandler(bot))\n",
    "        \n",
    "    @commands.Cog.listener()\n",
    "    async def on_command_error(self, ctx, error):\n",
    "        \"\"\"The event triggered when an error is raised while invoking a command.\n",
    "\n",
    "        Parameters\n",
    "        ------------\n",
    "        ctx: commands.Context\n",
    "            The context used for command invocation.\n",
    "        error: commands.CommandError\n",
    "            The Exception raised.\n",
    "        \"\"\"\n",
    "\n",
    "        # This prevents any commands with local handlers being handled here in on_command_error.\n",
    "        if hasattr(ctx.command, 'on_error'):\n",
    "            return\n",
    "\n",
    "        # This prevents any cogs with an overwritten cog_command_error being handled here.\n",
    "        cog = ctx.cog\n",
    "        if cog:\n",
    "            if cog._get_overridden_method(cog.cog_command_error) is not None:\n",
    "                return\n",
    "\n",
    "        ignored = (commands.CommandNotFound, )\n",
    "\n",
    "        # Allows us to check for original exceptions raised and sent to CommandInvokeError.\n",
    "        # If nothing is found. We keep the exception passed to on_command_error.\n",
    "        error = getattr(error, 'original', error)\n",
    "\n",
    "        # Anything in ignored will return and prevent anything happening.\n",
    "        if isinstance(error, ignored):\n",
    "            return\n",
    "\n",
    "        if isinstance(error, commands.DisabledCommand):\n",
    "            await ctx.send(f'{ctx.command} has been disabled.')\n",
    "\n",
    "        elif isinstance(error, commands.NoPrivateMessage):\n",
    "            try:\n",
    "                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')\n",
    "            except discord.HTTPException:\n",
    "                pass\n",
    "\n",
    "        # For this error example we check to see where it came from...\n",
    "        elif isinstance(error, commands.BadArgument):\n",
    "            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'\n",
    "                await ctx.send('I could not find that member. Please try again.')\n",
    "\n",
    "        else:\n",
    "            # All other Errors not returned come here. And we can just print the default TraceBack.\n",
    "            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)\n",
    "            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)\n"
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
