import requests
import time

# Define the URL of the webpage you want to search
url = "https://www.curseforge.com/minecraft/mc-mods/tweakeroo/files"

# Use the requests library to fetch the HTML of the webpage
response = requests.get(url)

# Check if the text "1.19.3" is present in the HTML of the webpage
while True:
    if "1.19.2" in response.text:
    # If the text is found, print "found"
        print("found")
    else:
        print('elsed')
        time.sleep(10)