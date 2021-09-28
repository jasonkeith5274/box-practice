from boxsdk import OAuth2
from boxsdk import Client
from bs4 import BeautifulSoup
import requests

# we are able to get the clinet id and client secret from the box developer console
# we used Oauth2 to authenticate this script
# the access token and refresh token were found from postman in order to allow the ability to read/write files in the box api


def store_tokens(access_token, refresh_token):
    print("got here")

oauth = OAuth2(
    client_id='11q0xp0s0mm49kgltxsg7rwm2c6br39c',
    client_secret='B86RdW6OdujcTJ2ekqn4LPsNnPAoCoHN',
    access_token='jJt9ROjmUOQpXLDi9Wm5bwhQIXjBvJA6',
    refresh_token='4jFDe3POdCq6p38tHmGTwC4wjOtae6jjihU0TzpRCgusrCm1EjNKYJAoK6BoKLAE',
)

# create a client using the authentication defined above
client = Client(oauth)

# create a user to contian the client data and print the user id
user = client.user().get()
print('The current user ID is {0}'.format(user.id))

###################################################################################
# we will begin to scrape the financial statements of apple (AAPL) using beautiful soup to scrape the html
# after we scrape the file and get all desired information we will build a .json file to store all the data found 
# I need to inspect source of the webpage to determine what tags I need to passs to beautiful soup

# get the page from the SEC, page will store all the html code in the content modifier 
page = requests.get('https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019321000065/aapl-20210626.htm')
# we will use the html parser from beautiful soup 
soup = BeautifulSoup(page.content, 'html.parser')

f = open("apple.txt", "w")
f.write(str(soup.prettify))



###################################################################################
# the folder_id is pre-determined by looking in the url inside of my box account (this is the fintech folder id)
folder_id = '146705961376'

# upload a predefined file inside of our directory to the fintech folder in my personal box
# new_file = client.folder(folder_id).upload('/home/wavy-j/fintech/box-practice/files/test2.pdf')
# print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))