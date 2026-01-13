import json
from discord.ext import commands

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = json.load(open("config.json"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(self.config["autorole_id"])
        if role:
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(AutoRole(bot))
