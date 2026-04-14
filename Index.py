import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!congrats'):
        file = discord.File(r'C:\Users\theca\Documents\Projects\LSXD Discord Bot\Pictures\angry-congrats.gif', filename="angry-congrats.gif")
        embed = discord.Embed()
        embed.set_image(url="attachment://angry-congrats.gif")
        await message.channel.send(file=file, embed=embed)

    if message.content.startswith('!status'):
        images = [
            r"C:\Users\theca\Documents\Projects\LSXD Discord Bot\Pictures\Its joever.png", 
            r"C:\Users\theca\Documents\Projects\LSXD Discord Bot\Pictures\barack.png"
        ]

        chosen = random.choice(images)
        file= discord.File(chosen, filename="content.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://content.png")

        await message.channel.send(file=file, embed=embed)

    if message.content.startswith('!login'):
        file = discord.File(r'C:\Users\theca\Documents\Projects\LSXD Discord Bot\Pictures\login.gif', filename="login.gif")
        embed = discord.Embed()
        embed.set_image(url="attachment://login.gif")
        await message.channel.send(file=file, embed=embed)

    if message.content.startswith('!mygm'):
        file = discord.File(r'C:\Users\theca\Documents\Projects\LSXD Discord Bot\Pictures\mygm.png', filename="mygm.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://mygm.png")
        await message.channel.send(file=file, embed=embed)

client.run('')