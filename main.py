import os
import discord
from core.Sage import Sage
from utils.config import whCL, TOKEN
from discord.ext.commands import Context
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import time
import json
import requests
try:
    import asyncio
    import jishaku, cogs
    import traceback
    from utils.Tools import *
    from discord import Webhook
except ModuleNotFoundError:
    #os.system("pip install tasksio && pip install httpx && pip install psutil && pip install requests && pip install git+https://github.com/PythonistaGuild/Wavelink")
    os.system("pip install git+https://github.com/Gorialis/jishaku")
    os.system("pip install git+https://github.com/Rapptz/discord-ext-menus")


os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

intents = discord.Intents.default()
intents.invites = True
intents.guilds = True
invites = {}
user_invites = {}
SageUrl = "https://discord.com/oauth2/authorize?client_id=1014955247564755075"
# File to store invite data
INVITE_DATA_FILE = 'invite_data.json'

# Dictionary to store invite information
user_invites = {}

# Load invite data from file
def load_invite_data():
    global user_invites
    if os.path.isfile(INVITE_DATA_FILE):
        with open(INVITE_DATA_FILE, 'r') as f:
            user_invites.update(json.load(f))

# Save invite data to file
def save_invite_data():
    with open(INVITE_DATA_FILE, 'w') as f:
        json.dump(user_invites, f, indent=4)
        
client = Sage()

@client.event
async def on_invite_create(invite):
    if invite.guild.id not in invites:
        invites[invite.guild.id] = []
    invites[invite.guild.id].append(invite)

@client.event
async def on_invite_delete(invite):
    if invite.guild.id in invites:
        invites[invite.guild.id] = [i for i in invites[invite.guild.id] if i.code != invite.code]

# ... rest of the code ...}  # Use a dictionary to store invites

token = TOKEN
    
client = Sage()
tree = client.tree
serverLink = "https://discord.com/invite/alwaysontop"

@client.event
async def on_command_completion(context: Context) -> None:

    full_command_name = context.command.qualified_name
    split = full_command_name.split("\n")
    executed_command = str(split[0])
    hacker = discord.SyncWebhook.from_url(f"{whCL}")
    if not context.message.content.startswith("."):
        pcmd = f"`.{context.message.content}`"
    else:
        pcmd = f"`{context.message.content}`"
    if context.guild is not None:
        try:

            embed = discord.Embed(color=0x2f3136)
            embed.set_author(
                name=
                f"Executed {executed_command} Command By : {context.author}",
                icon_url=f"{context.author.avatar}")
            embed.set_thumbnail(url=f"{context.author.avatar}")
            embed.add_field(
                name="Command Name :",
                value=f"{executed_command}",
                inline=False)
            embed.add_field(
                name="Command Content :",
                value="{}".format(pcmd),
                inline=False)
            embed.add_field(
                name="Command Executed By :",
                value=
                f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
                inline=False)
            embed.add_field(
                name="Command Executed In :",
                value=
                f"{context.guild.name}  | ID: [{context.guild.id}](https://discord.com/users/{context.author.id})",
                inline=False)
            embed.add_field(
                name=
                "Command Executed In Channel :",
                value=
                f"{context.channel.name}  | ID: [{context.channel.id}](https://discord.com/channel/{context.channel.id})",
                inline=False)
            embed.set_footer(text=f"Thank you for choosing  {client.user.name}",
                             icon_url=client.user.display_avatar.url)
            hacker.send(embed=embed)
        except:
            print('Error logging the command to webhook')
    else:
        try:

            embed1 = discord.Embed(color=0x2f3136)
            embed1.set_author(
                name=
                f"Executed {executed_command} Command By : {context.author}",
                icon_url=f"{context.author.avatar}")
            embed1.set_thumbnail(url=f"{context.author.avatar}")
            embed1.add_field(
                name="Command Name :",
                value=f"{executed_command}",
                inline=False)
            embed1.add_field(
                name="Command Executed By :",
                value=
                f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
                inline=False)
            embed1.set_footer(text=f"Thank you for choosing  {client.user.name}",
                              icon_url=client.user.display_avatar.url)
            hacker.send(embed=embed1)
        except:
            print('Command Successful')


@client.event
async def on_ready():
    load_invite_data()
    print("Loaded & Online!")
    print(f"Logged in as: {client.user}")
    print(f"Connected to: {len(client.guilds)} guilds")
    print(f"Connected to: {len(client.users)} users")
    print("</> Made By Team Sage!")
    time.sleep(1)
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print (e)
    try:
        with open("restart.txt", "r") as f:
            channel_id, message_id = [int(x) for x in f.read().split("\n")]
        channel = client.get_channel(channel_id)
        msg = await channel.fetch_message(message_id)
        await msg.edit(embed=discord.Embed(
            description=f"<a:SageCheck:1249381496565797017> | {client.user} has Restarted Successfully!",
            color=discord.Colour(0x00FF00)

        ))
        os.remove("restart.txt")
    except Exception as e:
        print(f"Error during restart message update: {e}")    
@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the bot was mentioned
    if client.user in message.mentions:
        data = getConfig(message.guild.id)
        prefix = data["prefix"]
        embed = discord.Embed(
            color=0x2f3136,
            title='<:SageLogo:1251339156945240124> Sage here!',
            description=f" Hey! **{message.author}**, i am **[Sage](https://discord.com/oauth2/authorize?client_id=1014955247564755075)** a Multipurpose Discord Automation Bot. Sage Provides You High **Security** And **Auto Moderation** Features Also it has So Many Useful Commands like Giveaway, Ticket and More.. \n **[Support](https://discord.com/invite/alwaysontop) | [Get Sage!](https://discord.com/oauth2/authorize?client_id=1014955247564755075)**\n\n<a:SageDot:1250872356503552001> Prefix for this Server is `{prefix}`**\n**<a:SageDot:1250872356503552001> Total Commands: `{len(set(client.walk_commands()))}`**\n**<a:SageDot:1250872356503552001> Use `{prefix}help` For Checking My Commands.**\n**<a:SageDot:1250872356503552001> Thanks For Pinging Me.",

        )
        embed.set_thumbnail(url=client.user.display_avatar.url)
        embed.set_footer(text=f"</> Made By Team Sage!", icon_url=client.user.display_avatar.url)
        embed.set_author(name=message.author.name, icon_url=message.author.display_avatar.url)
        await message.reply(embed=embed)

    await client.process_commands(message)

@client.command()
async def invites(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    total_invites = 0
    for invite in await ctx.guild.invites():
        if invite.inviter == member:
            total_invites += invite.uses

    await ctx.send(f"{member.name} has {total_invites} invites.")

@client.event
async def on_guild_join(guild):
    async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
        if entry.target.id == client.user.id:
            inviter = entry.user
            inviter_id = str(inviter.id)  # Use string as JSON keys must be strings
            if inviter_id not in user_invites:
                user_invites[inviter_id] = []
            user_invites[inviter_id].append({
                'guild_id': guild.id,
                'guild_name': guild.name,
                'member_count': guild.member_count
            })
            save_invite_data()
            break

@client.event
async def on_guild_remove(guild):
    # Remove the guild from the user_invites dictionary
    for inviter_id, guilds in user_invites.items():
        user_invites[inviter_id] = [g for g in guilds if g['guild_id'] != guild.id]
    save_invite_data()

@client.command()
async def botinvites(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    member_id = str(member.id)  # Use string as JSON keys must be strings
    if member_id not in user_invites or not user_invites[member_id]:
        embed = discord.Embed(
            title="No Invites Found", 
            description=f"**{member.display_name}** has not invited Sage to any servers.\nUse the Button below to Add **Sage.**", 
            color=0x2f3136
        )
        embed.set_author(name=f"Sage Invites of {member.name}", icon_url=member.display_avatar.url)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text="Add Sage Now!", icon_url=client.user.display_avatar.url)
        
        class InviteButton(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(discord.ui.Button(label='Add Sage Now!',  url=SageUrl))
        
        await ctx.reply(embed=embed, view=InviteButton())
        return

    invited_guilds = user_invites[member_id]
    embed = discord.Embed(
        description=f"**{member.display_name}** has invited **[Sage]({SageUrl})** to `{len(invited_guilds)}` Servers.", 
        color=0x2f3136
    )

    for guild_info in invited_guilds:
        embed.add_field(
            name=f"<:SageServerinv:1257257105170366474> {guild_info['guild_name']}",
            value=f"<:Sagelink:1257255148124901457> **[Server Link](https://discord.com/channels/{guild_info['guild_id']})**\n<:SageSupport:1253257818270728202> **Total Member: {guild_info['member_count']}**",
            inline=False
        )

    embed.set_author(name=f"Sage Invites of {member.name}", icon_url=member.display_avatar.url)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text="Add Sage Now!", icon_url=client.user.display_avatar.url)

    
    
    class InviteButton(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(discord.ui.Button(label='Add More!',  url=SageUrl))
        
    await ctx.reply(embed=embed, view=InviteButton())
    
async def main():
    async with client:
        os.system("cls")
        await client.load_extension("cogs")
        await client.load_extension("jishaku")
        await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
