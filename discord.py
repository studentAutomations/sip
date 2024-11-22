import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 

embed = Embed(
    color=0xFF4545,
    timestamp='now'
)

image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'
image2 = '1.png'

embed.set_author(name='Studentski Informacioni Portal')
embed.add_field(name='Nova obaveštenja', value='https://sip.elfak.ni.ac.rs/')
embed.set_footer(text='Elektronski Fakultet')
embed.set_thumbnail(image1)


hook.send(embed=embed, file=image2)
