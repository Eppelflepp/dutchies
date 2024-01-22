import nextcord
from nextcord.ext import commands

import os
import time

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="nl!", intents=intents)

@bot.event
async def on_ready():
  print("Bot is ready!")

@bot.slash_command(description="pong")
async def ping(ctx):
    start_time = time.monotonic()
    message = await ctx.send("Pong!")
    end_time = time.monotonic()
    await message.edit(content=f"Pong! :ping_pong: Response time: {round((end_time - start_time) * 1000)} ms")

@bot.slash_command(description="Pakt de avatar")
async def avatar(ctx, user: nextcord.Member = None):
    user = user or ctx.user
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)

@bot.slash_command(name="userinfo", description="Krijg alle informatie van een gebruiker")
async def userinfo(ctx: nextcord.Interaction, user: nextcord.Member = None):
    if user is None:
        user = ctx.user

    # Get information about the user
    username = str(user)
    created_at = user.created_at.strftime("%Y-%m-%d \n*%H:%M:%S*  UTC")
    joined_at = user.joined_at.strftime("%Y-%m-%d \n*%H:%M:%S*  UTC")
    roles = [role.mention for role in user.roles if role != ctx.guild.default_role]
    if len(roles) == 0:
        roles = ["None"]
    user_id = str(user.id)
    avatar_url = user.avatar.url


    embed = nextcord.Embed(title="Gebruikersinformatie", color=0x00ff00)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Gebruikersnaam", value=username, inline=False)
    embed.add_field(name="Account aangemaakt op", value=created_at, inline=False)
    embed.add_field(name="Deze server toegetreden op", value=joined_at, inline=False)
    embed.add_field(name="Rollen", value=", ".join(roles), inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="Gebruikers-ID", value=user_id, inline=False)
    embed.add_field(name="Activiteit", value=user.activity, inline=False)
    await ctx.send(embed=embed)
  

@bot.event
async def on_member_join(member):
    embed=nextcord.Embed(color=0xA020F0, title="Welkom!", description=f"Hallo {member.mention} en welkom in THE DUTCHIES OF DISCORD! Lees de ⁠<#1184470686652182648> en kijk vooral in ⁠<#1184431727154839584>, en zeg dan gezellig hoi in ⁠<#1184158687783288844> :)")
    embed.set_footer(text=f"Member: {member}")
    await bot.get_channel(1198927933985792030).send(embed=embed)

@bot.event
async def on_member_remove(member):
  embed=nextcord.Embed(color=0xA020F0, description=f"jammer, notthepresidentofamerica heeft de server verlaten. Doeg.. Er zitten nog {member.guild.member_count} members in de server")
  await bot.get_channel(1198927933985792030).send(embed=embed)

@bot.command()
async def sex(ctx, member: nextcord.Member):
  await ctx.send(f"*{ctx.member.mention} sexes {member.mention}*")
  
bot.run(os.environ['TOKEN'])
