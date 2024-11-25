import os
from dhooks import Webhook, Embed, File

# Get the webhook URL from environment variable
WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]

for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        color=0x499957,
        timestamp='now'
    )

    hook.send('@everyone Nova obavestenja na SIP-u!')

    image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'
    image2_path = 'path/to/sip-nova-obavestenja.png'  # Local path to the image

    embed.add_field(name='Idi na sajt - ', value='https://cs.elfak.ni.ac.rs/nastava/')
    embed.add_field(name='Vidi obavestenja - ', value='Image attached below.')
    embed.set_footer(text='Elektronski Fakultet')
    embed.set_thumbnail(image1)

    # Send the embed and attach the image
    hook.send(embed=embed, file=File(image2_path, name='sip-nova-obavestenja.png'))