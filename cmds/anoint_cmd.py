import nextcord
import json


async def get_anoint(interaction, passive):  # sourcery skip
    anoint_file = "json/oil.json"
    with open(anoint_file, 'r') as j:
        # Find gem with matching name in json
        data = json.loads(j.read())
        result = [
            x
            for x in data
            if x['passive'].lower().strip() == passive.lower().strip()
        ]
        if result:
            title = result[0]['passive']
            embed = nextcord.Embed(
                title=title,
                color=nextcord.Color.blue())
            embed.add_field(name="Oil #1",
                            value=result[0]['oil_1'],
                            inline=True)
            embed.add_field(name="Oil #2",
                            value=result[0]['oil_2'],
                            inline=True)
            embed.add_field(name="Oil #3",
                            value=result[0]['oil_3'],
                            inline=True)
            embed.add_field(name="Description",
                            value=result[0]['stats'],
                            inline=True)
            await interaction.send(embed=embed)
        else:
            await interaction.send(
                "Sorry exile, there are no results for that anointment.")
