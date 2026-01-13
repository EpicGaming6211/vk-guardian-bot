from discord.ext import commands

def has_role(role):
    async def predicate(ctx):
        return any(r.name == role for r in ctx.author.roles)
    return commands.check(predicate)
