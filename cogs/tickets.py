import discord
from discord.ext import commands
from utils.permissions import has_role

class TicketView(discord.ui.View):
    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.green)
    async def open(self, interaction: discord.Interaction, button):
        guild = interaction.guild
        channel = await guild.create_text_channel(
            f"ticket-{interaction.user.name}"
        )
        await channel.send(f"🎫 Ticket by {interaction.user.mention}")
        await interaction.response.send_message(
            "✅ Ticket created", ephemeral=True
        )

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="Open a support ticket")
    @has_role("Member")
    async def ticket(self, ctx):
        await ctx.reply("🎫 Click below:", view=TicketView())

def setup(bot):
    bot.add_cog(Tickets(bot))
