from discord.ext import commands

afk = {}

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def afk(self, ctx, *, reason="AFK"):
        afk[ctx.author.id] = reason
        await ctx.reply(f"💤 AFK: {reason}")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.id in afk:
            del afk[msg.author.id]
            await msg.channel.send(f"👋 Welcome back {msg.author.mention}")

        for u in msg.mentions:
            if u.id in afk:
                await msg.channel.send(f"💤 {u.name}: {afk[u.id]}")

def setup(bot):
    bot.add_cog(AFK(bot))
