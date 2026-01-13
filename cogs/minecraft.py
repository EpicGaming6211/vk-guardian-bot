from discord.ext import commands
from mcstatus import JavaServer
import json

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = json.load(open("config.json"))

    @commands.hybrid_command(description="Check Minecraft server status")
    async def mc(self, ctx):
        server = JavaServer.lookup(
            f"{self.config['minecraft']['ip']}:{self.config['minecraft']['port']}"
        )
        status = server.status()
        await ctx.reply(
            f"🟢 **Online:** {status.players.online} players"
        )

def setup(bot):
    bot.add_cog(Minecraft(bot))
