import discord
from discord.ext import commands

class CommandsList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_command_text(self):
        return (
            "**🤖 VK Guardian Commands**\n\n"
            "**General**\n"
            "`/commands` `!commands`\n"
            "`/rules`\n"
            "`/afk <reason>`\n\n"
            "**Verification**\n"
            "`/verify_panel`\n"
            "`/verify <code>`\n\n"
            "**Tickets**\n"
            "`/ticket`\n\n"
            "**Minecraft**\n"
            "`/mc`\n\n"
            "**Admin**\n"
            "`!reload`\n"
        )

    # SLASH COMMAND
    @discord.app_commands.command(name="commands", description="Show all bot commands")
    async def slash_commands(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            self.get_command_text(),
            ephemeral=True
        )

    # PREFIX COMMAND
    @commands.command(name="commands")
    async def prefix_commands(self, ctx):
        await ctx.send(self.get_command_text())

def setup(bot):
    bot.add_cog(CommandsList(bot))
