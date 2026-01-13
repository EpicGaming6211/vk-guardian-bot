from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="View server rules")
    async def rules(self, ctx):
        await ctx.reply(
            "📜 **Server Rules**\n"
            "1️⃣ Be respectful\n"
            "2️⃣ No spam\n"
            "3️⃣ Follow Discord TOS"
        )

def setup(bot):
    bot.add_cog(Rules(bot))
