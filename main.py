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




responseT = page_to_scrape.find_element(By.ID, "novosti")
    
    
    # Get the size of the element
    height = responseT.size['height']
    width = responseT.size['width']

    # Set a larger window size (you can adjust these values as needed)
    # Here we set a fixed width that is larger than what might be needed.
    desired_width = max(width + 100, 1200)  # Ensure at least 1200px width
    page_to_scrape.set_window_size(desired_width, height + 100)  # Adding some extra space

    # Scroll to make sure the element is visible in case it's off-screen
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT)

    # Take a screenshot of the entire element
    responseT.screenshot('sip-nova-obavestenja.png')
