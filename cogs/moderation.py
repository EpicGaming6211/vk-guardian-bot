import discord
from discord.ext import commands
from utils.permissions import has_role
from utils.database import log_punishment, get_history
from utils.modlog import send_log

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @has_role("Moderator")
    async def warn(self, ctx, member: discord.Member, *, reason="No reason"):
        log_punishment(member.id, ctx.author.id, "WARN", reason)
        embed = discord.Embed(title="⚠️ Warned", description=reason)
        await send_log(ctx.guild, embed)
        await ctx.reply("⚠️ Warned")

    @commands.hybrid_command()
    @has_role("Moderator")
    async def history(self, ctx, member: discord.Member):
        rows = get_history(member.id)
        if not rows:
            return await ctx.reply("No history")

        embed = discord.Embed(title=f"🧾 {member}")
        for a, r, t in rows[-10:]:
            embed.add_field(name=f"{a} - {t}", value=r, inline=False)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
