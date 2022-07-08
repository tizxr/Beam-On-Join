import discord
from discord.ext import commands
import requests
import json
from dhooks import Webhook
import random
from random import randint
import string
from time import sleep


Intents = discord.Intents.default()
Intents.members = True
Intents.presences = True
tizxr = commands.Bot(command_prefix="!", intents=Intents)
@tizxr.event
async def on_ready():
    print(f"Logged In As: {tizxr.user.name}")

@tizxr.event
async def on_member_join(member):
  channel = tizxr.get_channel(LOGGING CHANNEL HERE!)
  check = requests.get(f"https://verify.eryn.io/api/user/{member.id}")
  if check.status_code==200:
    username = requests.get(f"https://verify.eryn.io/api/user/{member.id}").json()["robloxUsername"]
    idx = requests.get(f"https://verify.eryn.io/api/user/{member.id}").json()["robloxId"]
    avatar_link = f"https://www.roblox.com/headshot-thumbnail/image?userId={idx}&width=420&height=420&format=png"
    if_termed = requests.get(f"https://users.roblox.com/v1/users/{idx}").json()["isBanned"]
    description = requests.get(f"https://users.roblox.com/v1/users/{idx}").json()["description"]
    pin = randint(1111, 9999)
    cookie =  "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" +  ''.join(random.choices("ABCDEF" + string.digits, k=732))
    embed=discord.Embed(title="**You Just Got Beamed!** ", description="You Just Got Beamed, We Now Have Your Cookies , Passwords, Personal Data")
    embed.set_thumbnail(url=f"{avatar_link}")
    embed.add_field(name="Your Username: ", value=f"{username}", inline=False)
    embed.add_field(name="Your Password:", value="|| Stored In Our DataBases! ||", inline=True)
    embed.add_field(name="Your Description:", value=f"```{description}```", inline=True)
    embed.set_footer(text="You Have Got Beamed, Made By tizxr#3313")
    await member.send(embed=embed)
    embed1=discord.Embed(title=f"**{member.name} Just Got Beamed! We Now Have His Information: **", description="This awesome tool is made by us beamers, to buy some premium features please DM me!", color=0x004cff)
    embed1.set_thumbnail(url=f"{avatar_link}")
    embed1.add_field(name="His Roblox Username:", value=f"*{username}*", inline=True)
    embed1.add_field(name="His Password", value="||**Saved in database **||", inline=True)
    embed1.add_field(name="His Roblox Pin:", value=f"||*{pin}*||", inline=True)
    embed1.add_field(name=f"Terminated: ", value=f"{if_termed}", inline=True)
    embed1.add_field(name=f"Account Recovery  Code:", value=f"||{randint(111111, 999999)}||", inline=False)
    embed1.add_field(name=f"Ip: ", value=f"||{randint(11, 123)}.{randint(100, 250)}.{randint(210, 300)}.{randint(100, 200)}||", inline=False)
    embed1.add_field(name=f"Cookie: ", value=f"{cookie}", inline=False)
    embed1.set_footer(text="You Have Got Beamed, Made By tizxr#33313")
    await channel.send(embed=embed1)
    sleep(1)
    await member.ban(reason="Got Beamed GG")
  else:
    await channel.send("User Could Not Get Beamed, He is too much secuirty!!!")
    await member.ban(reason="Got Beamed GG")
      


@tizxr.command()
async def uwu(ctx):
    await ctx.send("uwuwuuwuwuuwuwuwuw")


tizxr.run("token here")
