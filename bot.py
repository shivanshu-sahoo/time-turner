import os
import re
import discord
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import pymongo
import wtftz
from pymongo import MongoClient
import urllib
from timeZone import UTC_offset
from convertTime import convertTime
import random



load_dotenv()
MONGO = os.getenv('MONGO_URI')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

cluster = MongoClient("mongodb+srv://shivanshu:" + urllib.parse.quote(MONGO) + "@cluster0.qzsh9.mongodb.net/test")
db = cluster["time-turner"]
collection = db["time-turner"]


intents = discord.Intents.all()
client = discord.Client(intents=intents)

# On succesfull connecting to a guild
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# When the bot newly joins a guild 
@client.event
async def on_guild_join(guild):
    for member in guild.members:# for all the members in the server when the bot joins
        print(member.name)
        try:
            await member.create_dm()# create a dm 
            embedVar = discord.Embed(title="Hi {0}!! Welcome to {1}".format(member.name,member.guild.name), description="As you are new, I don't know your timezone yet.", color=random.randint(0, 0xFFFFFF))
            embedVar.add_field(name="Type in the timezone you belong to from the list", value="ANAT AEDT AEST JST WIB BST\n UZT GST MSK EET CET GMT\n CVT AOE ART VET EST CST\n MST PST AKST MST NUT LINT\n NZDT ACDT ACST MMT IST AFT \n IRST NST MART CHADT ACWST NPT", inline=False)
            await member.dm_channel.send(embed=embedVar)
            def check(message):#checks if the user replied
                return message.author.id==member.id
            msg = await client.wait_for('message',check=check)
            reply=msg.content#obstain the content of user reply
            post= {"user_id": member.id, "guild_id":guild.id,"timezone": reply}
            collection.insert_one(post)#post it in database
        except:
            pass

# On addition of a new member to the server 
@client.event
async def on_member_join(member):
    # member_id = member.id
    await member.create_dm()
    embedVar = discord.Embed(title="Hi {0}!! Welcome to {1}".format(member.name,member.guild.name), description="As you are new, I don't know your timezone yet.", color=random.randint(0, 0xFFFFFF))
    embedVar.add_field(name="Type in the timezone you belong to from the list", value="ANAT AEDT AEST JST WIB BST\n UZT GST MSK EET CET GMT\n CVT AOE ART VET EST CST\n MST PST AKST MST NUT LINT\n NZDT ACDT ACST MMT IST AFT \n IRST NST MART CHADT ACWST NPT", inline=False)
    await member.dm_channel.send(embed=embedVar)
    def check(message):
        return message.author.id==member.id
    msg = await client.wait_for('message',check=check)
    reply=msg.content
    post= {"user_id": member.id, "guild_id":member.guild.id,"timezone": reply}
    collection.insert_one(post)

# On receiving a message in the guild
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        content = message.content.lower() #obtain the content of message sent in channel
        content=re.sub('[^A-Za-z0-9: ]+', '', content) #remove special characters
        content = re.findall(r"[^\W\d_]+|\d+(?::\d+)?", content) #separate the string at spaces and numbers

        if any(item in ["am","pm"] for item in content): #if am or pm is found in the content
            if "am" in content:
                index=content.index("am") #find the index of am
                time=content[index-1] #time is present is the previous index of am
            else:
                index=content.index("pm")
                time=content[index-1]
            print(time)
            emoji = '\N{Alarm Clock}'
            # or '\U0001f44d' or '👍'
            await message.add_reaction(emoji)
        timezones=["ANAT", "AEDT", "AEST", "JST" ,"WIB" ,"BST", "UZT", "GST", "MSK" ,"EET", "CET" ,"GMT", "CVT", "AOE", "ART", "VET", "EST", "CST", "MST", "PST", "AKST", "MST", "NUT", "LINT","NZDT", "ACDT", "ACST", "MMT", "IST", "AFT", "IRST", "NST", "MART", "CHADT", "ACWST", "NPT"]
        if message.content.upper() in timezones:
            await message.author.create_dm()
            embedVar = discord.Embed(title="Thanks, now I know your TimeZone", description=" ", color=random.randint(0, 0xFFFFFF))
            await message.author.dm_channel.send(embed=embedVar)

# When a member leaves the guild his data is deleted from the database
@client.event
async def on_member_remove(member):
    collection.find_one_and_delete({"user_id": member.id, "guild_id":member.guild.id})#delete the data from database from someone leaves the server

@client.event
async def on_reaction_add(reaction, user):
    content = reaction.message.content.lower() #obtain the content of message sent in channel
    content=re.sub('[^A-Za-z0-9: ]+', '', content) #remove special characters
    content = re.findall(r"[^\W\d_]+|\d+(?::\d+)?", content) #separate the string at spaces and numbers
    if any(item in ["am","pm"] for item in content): #if am or pm is found in the content
        if "am" in content:
            index=content.index("am") #find the index of am
            time=content[index-1] #time is present is the previous index of am
            period="am"
        else:
            index=content.index("pm")
            time=content[index-1]
            period="pm"
        try:
            user_reacted= collection.find_one({"user_id":user.id,"guild_id":reaction.message.guild.id}) 
            tz_reacted= user_reacted.get("timezone")   
            user_sent= collection.find_one({"user_id":reaction.message.author.id,"guild_id":reaction.message.guild.id}) 
            tz_sent= user_sent.get("timezone")  
            print("tz of user who reacted",tz_reacted) 
            print("tz of user who sent the message",tz_sent) 
            print("here workes the converter")
            time,period,day=convertTime(time,tz_sent,tz_reacted,period)
        except:
            pass

        try:
            embedVar = discord.Embed(title="Hey,The time in {0} is {1} {2} the {3}".format(tz_reacted,time,period,day), description=" ", color=random.randint(0, 0xFFFFFF))

            await user.send(embed=embedVar,delete_after=100)
           
        except:
            pass   

client.run(TOKEN)




