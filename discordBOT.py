import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('PB')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

   # hook.send('**@everyone**')
   
     image2_path = 'sip-nova-obavestenja.png' 

  #  hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'))

  #  hook.send('**>>> https://sip.elfak.ni.ac.rs/**')


    embed = Embed(
        description="**@everyone**\n\n>>> [Kliknite ovde za detalje.](https://cs.elfak.ni.ac.rs/nastava/)",
        color=0x3498db
    )
    embed.set_image(url=f"attachment://{image2_path}")  

    
    hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'), embed=embed)
