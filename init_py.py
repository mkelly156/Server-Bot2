#!/usr/bin/env python
# coding: utf-8

# In[2]:


import discord
from discord.ext import commands, tasks
import aiohttp
import os
import requests
import random
import wikipedia


# In[3]:


client = commands.Bot(command_prefix="?", help_command=None)


# In[4]:


from discord.voice_client import VoiceClient
import youtube_dl


# In[5]:


import asyncio
import nest_asyncio
import async_timeout
nest_asyncio.apply()
songs = asyncio.Queue()
play_next_song = asyncio.Event()
queues = {}


# In[9]:


if __name__ == "__main__":
    for file in os.listdir("Cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"Cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


# In[5]:


client.event
async def on_ready():
    print('Doppio is here!')


# In[ ]:


client.run('{token here}')

