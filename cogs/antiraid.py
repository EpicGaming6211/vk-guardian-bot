import time
from discord.ext import commands

joins = []

class AntiRaid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        now = time.time()
        joins.append(now)
        joins[:] = [t for t in joins if now - t < 10]

        if len(joins) >= 5:
            await member.guild.edit(verification_level=3)

def setup(bot):
    bot.add_cog(AntiRaid(bot))
