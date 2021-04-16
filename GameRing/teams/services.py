import os
import requests
import json
'''
NOTE: What is referred to as a 'participant' is a team.
      Members of said team are stored in our database.
'''
#participants API GET
#returns a list of participants and their information for a single tournament
def get_participants(tournamentURL):
    url = 'https://api.challonge.com/v1/tournaments/' + ournamentURL + '/participants.json'
    r = requests.get(url, headers={'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp'})
    participants = r.json()
    participant_list = []

    for i  in range(len(participants['participant'])):
        participant_list.append(participants['participant'][i])
    return participant_list

#participants API GET
#requires tournament url and participant id
#returns a single participant as a json object
def get_participant(tournamentURL, participantID):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/' + participantID + '.json'
    r = requests.get(url)
    return r.json()

#participants API POST
#parameters is a dictionary, currently only contains name of the participant
#returns json object of participant's information
def add_participant(parameters):
    url = 'https://api.challonge.com/v1/tournaments.json'
    data = {'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
            'name' : parameters['name']}
    r = requests.post(url, data)
    return r.json()

#participants API DELETE
#if tournament has not started, participant is removed from the tournament
#if tournament has started, participant is marked as inactive, ff'ing remaining matches
#returns json object of participant
def remove_participant(tournamentURL, participantID):
    url = url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/' + participantID + '.json'
    r = requests.delete(url)
    return r.json()