from itertools import cycle
import os
from dhooks import Webhook, Embed, File

image2_path = 'sip-nova-obavestenja.png'

colors = [0x3498db, 0xe74c3c, 0x2ecc71, 0x9b59b6]
color_cycle = cycle(colors)

WEBHOOK_URL = [os.getenv('PB')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed_color = next(color_cycle) 

    embed = Embed(
        description="**@everyone**\n\n>>> [**SIP link**](https://cs.elfak.ni.ac.rs/nastava/)",
        color=embed_color 
    )
    embed.set_image(url=f"attachment://{image2_path}")  

    hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'), embed=embed)
