import json, discord

config = json.load(open("config.json"))

async def send_log(guild, embed):
    channel = guild.get_channel(config["modlog_channel"])
    if channel:
        await channel.send(embed=embed)
