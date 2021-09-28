import sys
from boxsdk import OAuth2
from boxsdk import Client

def store_tokens(access_token, refresh_token):
    print("got here")

oauth = OAuth2(
    client_id='11q0xp0s0mm49kgltxsg7rwm2c6br39c',
    client_secret='B86RdW6OdujcTJ2ekqn4LPsNnPAoCoHN',
    access_token='jJt9ROjmUOQpXLDi9Wm5bwhQIXjBvJA6',
    refresh_token='4jFDe3POdCq6p38tHmGTwC4wjOtae6jjihU0TzpRCgusrCm1EjNKYJAoK6BoKLAE',
)

client = Client(oauth)

user = client.user().get()

print('The current user ID is {0}'.format(user.id))

folder_id = '146705961376'
new_file = client.folder(folder_id).upload('/home/wavy-j/fintech/box-practice/files/test2.pdf')
print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))