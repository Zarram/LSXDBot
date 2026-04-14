import discord
import random
import APIKey

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Images hosted on Discord for easy access, ipload to a Discord chat and copy the URL, then add to the dictionary below
IMAGE_URLS = {
    '!congrats': 'https://media.discordapp.net/attachments/818907457253408768/1493600433615147018/angry-congrats.gif?ex=69df8f4d&is=69de3dcd&hm=6bf09ca8067087868d7c76967612fcb125a504f3dec40f816840bd8a6f498cac&=',
    '!login': 'https://media.discordapp.net/attachments/818907457253408768/1493600435485933680/login.gif?ex=69df8f4d&is=69de3dcd&hm=eebeeaaa6c12e669b2716624149899ef57af5b393eb77b2213a21485bbc3f1c1&=',
    '!mygm': 'https://media.discordapp.net/attachments/818907457253408768/1493600436588908735/mygm.png?ex=69df8f4d&is=69de3dcd&hm=b17ef794740230b9d227335d50960adfc0adc7d7faa642d153ea2c1c8cbddd39&=&format=webp&quality=lossless',
    '!cinema': 'https://cdn.discordapp.com/attachments/1457739209606434846/1490516111115026603/GUZr4rVWwAAvGgi.png?ex=69df8b8d&is=69de3a0d&hm=e69e899678befe6a8487d5e428abfd45c9776a13a4ddb990be2fabe1181b8d14&',
}



# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Listen for messages and respond to commands uses ! as the prefix, e.g. !hello, !congrats, !status, !login, !mygm
@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!congrats'):
        await message.channel.send(IMAGE_URLS['!congrats'])

    if message.content.startswith('!status'):
        # For the !status command, we want to randomly choose from a list of images, so we create a separate list for that
        RANDOM_IMAGE_URLS = [
    'https://media.discordapp.net/attachments/818907457253408768/1493600434894667776/Its_joever.png?ex=69df8f4d&is=69de3dcd&hm=b355885b5e3b59254733917aa78ff0e727784e2a2454db2ddc0734f2d4950e99&=&format=webp&quality=lossless',
    'https://media.discordapp.net/attachments/818907457253408768/1493600437750857928/Were_Barack.webp?ex=69df8f4e&is=69de3dce&hm=0c303bb62da89602ac8536861e843e80fdcc84bfcc27b76f99cb99cb13e8bfcb&=&format=webp',
]
        chosen_url = random.choice(RANDOM_IMAGE_URLS)
        await message.channel.send(chosen_url)

    if message.content.startswith('!login'):
        await message.channel.send(IMAGE_URLS['!login'])

    if message.content.startswith('!mygm'):
        await message.channel.send(IMAGE_URLS['!mygm'])

    if message.content.startswith('!cinema'):
        await message.channel.send(IMAGE_URLS['!cinema'])

    if message.content.startswith('!raiddays'):
        await message.channel.send('Wednesday and Monday 20-23 ServerTime! Optionally raid on Sundays as well!')

#For security, the API key is stored in a separate file
token = APIKey.DISCORD_API_KEY

# Run the bot
client.run(token)