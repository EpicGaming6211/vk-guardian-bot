import discord
from discord.ext import commands
from utils.modlog import send_log

class AntiNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for log in channel.guild.audit_logs(limit=1):
            await channel.guild.ban(log.user, reason="Anti-nuke")
            embed = discord.Embed(title="🚨 Anti-Nuke Triggered")
            await send_log(channel.guild, embed)

def setup(bot):
    bot.add_cog(AntiNuke(bot))
