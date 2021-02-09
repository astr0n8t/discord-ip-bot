# bot.py
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni
import os
import discord
from time import sleep


TOKEN = "ENTER_TOKEN_HERE"
client = discord.Client()

def getIP():
    return ni.ifaddresses('wlp58s0')[AF_INET][0]['addr']

def getIPInfo():
    ip_address = getIP()
    info = "Enter info here"
    return info


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
        

@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith('!ip-bot'):
        return

    ip_info = getIPInfo()
    sent = await message.channel.send(ip_info)

    while True:
        if ip_info != getIPInfo():
            ip_info = getIPInfo()
            await sent.edit(content=ip_info)
        sleep(60)

client.run(TOKEN)

