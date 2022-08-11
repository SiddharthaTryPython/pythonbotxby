import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+config'):
        await message.channel.send('Check <#997904618854027384> and Make sure to Create Ticket At <#997926422008041594> Enjoy :D')


client.run('OTkwNDM1NzU1NzIzNzIyNzgz.GZX2UZ.WdrtkcXt9vV2coYBBHycyF65W5RMOWeSsFIQmE')
