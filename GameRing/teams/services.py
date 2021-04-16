import os
import requests
import json

#participants API GET
def get_participants(tournamentURL):
    url = 'https://api.challonge.com/v1/tournaments/' + str(tournamentURL) + '/participants.json'
    r = requests.get(url, headers={'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp'})
    participants = r.json()
    participant_list = []

    for i  in range(len(participants['participant'])):
        participant_list.append(participants['participant'][i])
    
    return participant_list

#participants API POST
def add_participant(parameters):
    url = 'https://api.challonge.com/v1/tournaments.json'
    data = {'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
            'name' : parameters['name']}
    r = requests.post(url, data)

    return r.json()
