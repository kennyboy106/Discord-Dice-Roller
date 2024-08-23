# Kenneth Tang
# August 6th, 2024

# Import libraries
import asyncio
import os
import sys
import traceback
import logging
import sqlite3
from dotenv import load_dotenv

try:
    import discord    
    from discord.ext import commands
    
# If failed to get any import, quit. This also stops the docker container
except Exception as e:
    print(f"Error importing libraries: {e}")
    print(traceback.format_exc())
    sys.exit(1)

'''
The plan is to create a discord bot that uses SQL database to 
provide users in the server to roll custom dice.

Requirements:
    1. Users must be able to select which die they want to roll
    2. The die data shall be stored using SQL
    3. Handle multiple input from users or multiple users at the same time
    4. Create dice sets per user that can be rolled
    5. Command should look like:
        /roll 10d6 2d20 ...etc
        /bag # shows what sets are in a players bag
        /bag add/remove
    6. Customizable output of results. Maybe default to individual rolls & total
'''

if __name__ == '__main__':

    # Load environment variables from .env file
    load_dotenv()
    if not os.environ['DISCORD_TOKEN']:
        raise Exception("DISCORD_TOKEN not found in .env file, please add it")
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    # Logging
    if os.environ['LOGGING'] == 'TRUE' and os.environ['LOGGING_LEVEL']:
        handler = logging.FileHandler(filename='dicebot.log', encoding='utf-8', mode='w')
        discord.utils.setup_logging(handler=handler, root=False, level=getattr(logging, os.getenv("LOGGING_LEVEL")))



    # intents = discord.Intents.default()
    # intents.message_content = True

    # client = discord.Client(intents=intents)

    # @client.event
    # async def on_ready():
    #     print(f"We have logged in as {client.user}")
    
    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return
    #     if message.content.startswith("$hello"):
    #         await message.channel.send("Hello!")
    
    # client.run(DISCORD_TOKEN)
