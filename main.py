import requests
from bs4 import BeautifulSoup

sip_url = "https://sip.elfak.ni.ac.rs/"

response = requests.get(sip_url)
html = BeautifulSoup(response.text, 'html.parser')

newText = html.find('section', {"id" : "novosti"})


novosti_markdown = newText.text


with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_markdown)
