import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print("Bot is running.")

    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)
    
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()