
import os
from dhooks import Webhook, Embed
import discord
from discord import Webhook


# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 

embed = Embed(
    color=0xFF4545,
    timestamp='now'
)

image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'

embed.set_author(name='Computer Science')
embed.add_field(name='Nova obaveštenja', value='https://cs.elfak.ni.ac.rs/nastava/')
embed.set_footer(text='Elektronski Fakultet')
embed.set_thumbnail(image1)

hook.send(embed=embed, file=discord.File(f, filename='1.png')
