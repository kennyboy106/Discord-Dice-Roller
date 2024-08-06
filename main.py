# Kenneth Tang
# August 6th, 2024

# Import libraries
import asyncio
import os
import sys
import traceback

try:
    import discord
    from discord.ext import commands
    # from dotenv import load_dotenv

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