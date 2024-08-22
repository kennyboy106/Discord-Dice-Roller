# Kenneth Tang
# August 6th, 2024

# Import libraries
import asyncio
import os
import sys
import traceback
import sqlite3

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

if __name__ == '__main__':
    
    # Create the database in pwd. This returns a Connection object which represents the connection to the on-disk database
    con = sqlite3.connect('dice_sets.db')
    # Create a cursor which allows us to execute SQL statements and fetch results from SQL queries
    cur = con.cursor()
    # Create a table using the execute command. If already exists, dont create it and just use it.
    cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
    # Check that the table is created
    res = cur.execute("SELECT name FROM sqlite_master")
    # Print table name in the tuple that is returned
    print(res.fetchone())
    # Add stuff to the database
    cur.execute("""
        INSERT INTO movie VALUES
                ('Monty Python and the Holy Grail', 1975, 8.2),
                ('And Now for Something Completely Different', 1971, 7.5)
    """)
    # Save the entry to the database
    con.commit()
    # Check to see what scores we have
    res = cur.execute("SELECT score FROM movie")
    scores = res.fetchall()
    for tup in scores:
        print(tup[0])

    # Insert more data, securely
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    # Make sure to use execute many
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()
    # Make sure it was added
    res = cur.execute("SELECT score FROM movie")
    for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
        print(row)
    
    # Close the database and open it again to test if it was written to disk
    con.close()
    new_con = sqlite3.connect('dice_sets.db')
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
    title, year = res.fetchone()
    print(f"{title} created in {year}")
    new_con.close()






