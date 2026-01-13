import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="🤖 VK Guardian Commands",
            color=discord.Color.blurple()
        )

        for cog in self.bot.cogs.values():
            cmds = [f"`{c.name}`" for c in cog.get_commands()]
            if cmds:
                embed.add_field(
                    name=cog.qualified_name,
                    value=" ".join(cmds),
                    inline=False
                )

        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
