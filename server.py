import requests
import json
import discord
import time

TOKEN='DISCORDTOKEN'

client = discord.Client()

template = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=%s&key=%s'

pewdiepie = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
tseries = 'UCq-Fj5jknLsUf-MWSy4_brA'

api = 'GOOGLEAPITOKEN'

def get_sub(id):
	return int(json.loads(requests.get(template % (id, api)).text)['items'][0]['statistics']['subscriberCount'])

def bundle():

	pew_subs = get_sub(pewdiepie)
	t_subs = get_sub(tseries)

	return 'PewDiePie: %i\nT-Series: %i\nDifference: %i' % (pew_subs, t_subs, pew_subs - t_subs)

print(bundle())

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.channel)

    if message.content.startswith('!pewds'):
        msg = bundle()
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
