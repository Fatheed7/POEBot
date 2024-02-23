import nextcord
import json


async def get_gem(interaction, gem):  # sourcery skip
    gem_file = "json/gems.json"
    with open(gem_file, 'r') as j:
        # Find gem with matching name in json
        data = json.loads(j.read())
        result = [
            x
            for x in data
            if x['name'].lower().strip() == gem.lower().strip()
        ]
        if result:
            title = ""
            if result[0]['isSupport']:
                title = gem.title() + " Support"
            else:
                title = gem.title()
            if result[0]['color'] == "red":
                embed = nextcord.Embed(
                    title=title,
                    color=nextcord.Color.red())
            elif result[0]['color'] == "green":
                embed = nextcord.Embed(
                    title=title,
                    color=nextcord.Color.green())
            else:
                embed = nextcord.Embed(
                    title=title,
                    color=nextcord.Color.blue())
            embed.set_thumbnail(
                url=(result[0]['iconPath']))
            embed.add_field(name="Required Level",
                            value=result[0]['required_lvl'],
                            inline=True)
            embed.add_field(name="Colour",
                            value=result[0]['color'].capitalize(),
                            inline=True)
            embed.add_field(name='\u200b',
                            value='\u200b',
                            inline=True)
            if len(result[0]['gemTags']) > 0:
                tags = ', '.join(result[0]['gemTags'])
                embed.add_field(name="Gem Tags",
                                value=tags,
                                inline=True)
            if result[0]['isSupport']:
                embed.add_field(name="Wiki Link",
                                value="[Click Here](https://pathofexile.fandom"
                                ".com/wiki/" +
                                result[0]['name'].replace(" ", "_") +
                                "_Support)",
                                inline=True)
            else:
                embed.add_field(name="Wiki Link",
                                value="[Click Here](https://pathofexile.fandom"
                                ".com/wiki/" +
                                result[0]['name'].replace(" ", "_")
                                + ")",
                                inline=True)
            embed.add_field(name="-----------------------"
                            "-------------------------",
                            value="",
                            inline=False)
            # Loop over vendor rewards and add to embed
            if len(result[0]['buy']) > 0:
                for item in result[0]['buy']:
                    embed.add_field(name="NPC",
                                    value=item['npc'],
                                    inline=True)
                    embed.add_field(name="Quest",
                                    value=item['quest_name'],
                                    inline=True)
                    embed.add_field(name="Act",
                                    value=item['act'],
                                    inline=True)
                    if len(item['available_to']) > 0:
                        classes_string = ', '.join(item['available_to'])
                        embed.add_field(name="Available To",
                                        value=classes_string,
                                        inline=True)
                    embed.add_field(
                        name="--------------------------"
                             "----------------------",
                        value="",
                        inline=False)
            if len(result[0]['buy']) == 0:
                # check if first word of name is "Awakened"
                if result[0]['name'].split()[0] == "Awakened":
                    embed.add_field(name="Dropped by:",
                                    value="Sirus, Awakener of Worlds,"
                                    "'Al-Hezmin, the Hunter', "
                                    "'Veritania, the Redeemer', "
                                    "'Drox, the Warlord' and "
                                    "'Baran, the Crusader'",
                                    inline=False)
                else:
                    embed.add_field(name="You fucking cunt. This gem "
                                    "is drop only. "
                                    "REEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
                                    value="",
                                    inline=False)
            await interaction.send(embed=embed)
        else:
            await interaction.send(
                "Sorry exile, there are no results for that gem.")
