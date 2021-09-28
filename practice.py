from boxsdk import OAuth2
from boxsdk import Client

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

# create a user to contian the client data 
user = client.user().get()

print('The current user ID is {0}'.format(user.id))

# the folder_id is pre-determined by looking in the url inside of my box account (this is the fintech folder id)
folder_id = '146705961376'

# upload a predefined file inside of our directory to the fintech folder in my personal box
new_file = client.folder(folder_id).upload('/home/wavy-j/fintech/box-practice/files/test2.pdf')
print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))