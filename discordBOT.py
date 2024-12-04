import os
from dhooks import Webhook, Embed, File

image2_path = 'sip-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN'), os.getenv('WEBHOOK_OTHER1'), os.getenv('WEBHOOK_OTHER2')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**@everyone**\n\n>>> **[SIP link](https://sip.elfak.ni.ac.rs/)**",
        color=0x3498DB
    )
    embed.set_image(url=f"attachment://{image2_path}")  

    hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'), embed=embed)
