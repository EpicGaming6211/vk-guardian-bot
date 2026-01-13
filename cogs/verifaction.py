import random
from discord.ext import commands

codes = {}

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="Start verification")
    async def verify(self, ctx):
        code = random.randint(100000, 999999)
        codes[ctx.author.id] = code
        await ctx.author.send(f"🔐 Code: `{code}`")
        await ctx.reply("📩 Check your DMs")

    @commands.hybrid_command(description="Submit verification code")
    async def verifycode(self, ctx, code: int):
        if codes.get(ctx.author.id) == code:
            role = discord.utils.get(ctx.guild.roles, name="Verified")
            await ctx.author.add_roles(role)
            await ctx.reply("✅ Verified!")
            del codes[ctx.author.id]
        else:
            await ctx.reply("❌ Invalid code")

def setup(bot):
    bot.add_cog(Verification(bot))
