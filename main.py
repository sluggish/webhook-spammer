import discord
from discord import Webhook

import aiohttp
import asyncio

async def send_webhook_msg(webhook, amount: int, username, message):
        async with aiohttp.ClientSession() as session:
            web = Webhook.from_url(webhook, session=session)
            for msg in range(amount + 1):
                 await web.send(message, username=username)
                 print("Sent {} messages".format(msg))


async def main():
    webhook = input("Webhook URL to spam: ")
    amount = int(input("Amount of messages to send: "))
    username = input("Username to send webhook as: ")
    message = input("Message to send to webhook: ")

    await send_webhook_msg(webhook, amount, username, message)

asyncio.run(main())