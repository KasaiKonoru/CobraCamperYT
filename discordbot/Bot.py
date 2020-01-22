import asyncio

import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Tatsuka'), status=discord.Status.online)
        await asyncio.sleep(4)
        await client.change_presence(activity=discord.Game('Gaming'), status=discord.Status.online)
        await asyncio.sleep(4)
        await client.change_presence(activity=discord.Game('Discord'), status=discord.Status.online)
        await asyncio.sleep(2)

client.run('NjYyNjc2NTcyNjAzNjc4Nzkx.Xih5Ag.x38fBX8_xTi6n1Ho7okqTMzayjA')
