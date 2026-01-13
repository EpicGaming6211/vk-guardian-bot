@commands.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            ctx.bot.reload_extension(f"cogs.{file[:-3]}")
    await ctx.send("🔁 All cogs reloaded!")
