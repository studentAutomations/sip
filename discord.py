import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL)

# Create an embed object for the webhook
embed = Embed(
    color=0xFF4545,
    timestamp='now'
)

# Define your images
image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'
image2 = '1.png'  # Path to the local image file you want to send

# Set up the embed fields and attributes
embed.set_author(name='Studentski Informacioni Portal')
embed.add_field(name='Nova obaveštenja', value='https://sip.elfak.ni.ac.rs/')
embed.set_footer(text='Elektronski Fakultet')
embed.set_thumbnail(image1)

# Send the embed along with the image file
with open(image2, 'rb') as f:  # Open the image file in binary mode
    hook.send(embed=embed, file=f)  # Attach the local image file


