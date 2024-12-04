import os
from dhooks import Webhook, Embed, File

# Postavi URL za webhook
WEBHOOK_URL = [os.getenv('PROJECTBOT')]

# Putanja do slike
image2_path = 'sip-nova-obavestenja.png'

for url in WEBHOOK_URL:
    hook = Webhook(url)
    
    # Kreiraj embed
    embed = Embed(
        title="📢 Ažuriranje bota",
        description="Evo najnovijih promena:",
        color=0x7289DA  # Discord plava boja
    )
    
    # Dodaj stavke u embed
    embed.add_field(name="✅", value="Popravljeni su bagovi i greške.", inline=False)
    embed.add_field(name="🤖", value="Dodati su novi botovi.", inline=False)
    embed.add_field(name="✨", value="Poruke bota imaju novi dizajn.", inline=False)
    embed.add_field(name="⏱️", value="Smanjeno je vreme obrade operacija.", inline=False)
    embed.add_field(name="📱", value="Notifikacije za mobilne aplikacije sada imaju novi izgled.", inline=False)
    
    # Dodaj sliku na embed
    embed.set_image(url="attachment://sip-nova-obavestenja.png")
    
    # Pošalji poruku sa slikom
    with File(image2_path, name="sip-nova-obavestenja.png") as file:
        hook.send("@everyone", embed=embed, file=file)
