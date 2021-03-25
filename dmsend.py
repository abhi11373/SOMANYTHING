import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("BOT ONLINE.")
    game = discord.Game('★Game name★')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {msg} to send dm
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    # if you have manage messages permissons you can use this command
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="★★title★★", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/★★invite code★★")
                        await i.send(embed=embed)
                except:
                    pass


client.run('★★TOKEN★★')
