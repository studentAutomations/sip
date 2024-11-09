import requests
from bs4 import BeautifulSoup

sip_url = "https://sip.elfak.ni.ac.rs/"

# get website contents and parse html
response = requests.get(sip_url)
html = BeautifulSoup(response.text, 'html.parser')

newText = html.find('section', {"id" : "novosti"})

# create markdown string of courses
novosti_markdown = newText.text

# write markdown file
with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_markdown)