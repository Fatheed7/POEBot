import os

import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

from cmds import (  # noqa: F401
    gem_cmd, lab_cmd, anoint_cmd)

if os.path.exists("env.py"):
    import env # noqa
TOKEN = os.environ.get('DISCORD_TOKEN')
intents = nextcord.Intents.all()
bot = commands.Bot()
servers = [867600394196484107]


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# POE Gem Command #
@bot.slash_command(guild_ids=servers,
                   description="Search for Skill or Support Gem")
async def gem(
    interaction: Interaction,
    gem: str = SlashOption(
        description="Enter the gem you wish to search for.", required=True)):
    await gem_cmd.get_gem(interaction, gem)


# POE Gem Command #
@bot.slash_command(guild_ids=servers,
                   description="Search for Anointment")
async def anoint(
    interaction: Interaction,
    anointments: str = SlashOption(
        description="Enter the anointment you wish to search for.",
        required=True)):
    await anoint_cmd.get_anoint(interaction, anointments)


# POE Lab Command #
@bot.slash_command(guild_ids=servers,
                   description="Get todays lab layout")
async def lab(
    interaction: nextcord.Interaction,
    text: str = SlashOption(
        description="Choose a difficulty",
        required=True,
        choices={
            "Normal": "normal",
            "Cruel": "cruel",
            "Merciless": "merciless",
            "Uber": "uber"})):
    await lab_cmd.lab_cmd(interaction, text)

@commands.is_owner()
@bot.slash_command(guild_ids=servers,
                   description="Shutdown POE Bot")
async def shutdown(interaction: Interaction):
    await interaction.response.send_message("Shutting down bot", ephemeral=True)
    exit()


bot.run(TOKEN)
