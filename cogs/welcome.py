import json
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = json.load(open("config.json"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ch = member.guild.get_channel(self.config["welcome_channel"])
        if ch:
            await ch.send(f"👋 Welcome {member.mention}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ch = member.guild.get_channel(self.config["welcome_channel"])
        if ch:
            await ch.send(f"😢 {member} left the server")

def setup(bot):
    bot.add_cog(Welcome(bot))
