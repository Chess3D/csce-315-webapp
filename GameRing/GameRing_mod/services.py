import os
import requests
import json

#tournament API GET
#returns a list of dictionaries, i think
def get_tournaments():
    url = 'https://api.challonge.com/v1/tournaments/'
    r = requests.get(url, headers={'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp'})
    tournaments = r.json()
    tournament_list = []
    for i  in range(len(tournaments['tournament'])):
        tournament_list.append(tournaments['tournament'][i])
    return tournament_list


#tournament API POST
#parameters is a dictionary
#returns a json object
def create_tournament(parameters):
    url = 'https://api.challonge.com/v1/tournaments.json'
    data = {'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
            'name' : parameters['name'],
            'game_name' : parameters['game_name'],
            'tournament_type' : parameters['tournament_type'],
            'grand_finals_modifier' : parameters['grand_finals_modifier'],
            'signup_cap' : parameters['signup_cap'],
            'start_at' : parameters['start_at'],
            'hold_third_place_match' : parameters['hold_third_place_match'],
            'show_rounds' : parameters['show_rounds'],
            'private' : 'true',
            'description' : parameters['description'],
            'notify_users_when_matches_open' : 'false',
            'notify_users_when_the_tournament_ends' : 'false'
            }
    r = requests.post(url, data)
    return r.json()


#tournament API DELETE
#returns a json object
def delete_tournament(tournamentid):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentid + '.json'
    r = requests.delete(url)
    return r.json()


#tournament API PUT
#update tournament information
#returns json object
def update_tournament(tournamentid, fields, updated_values): #this needs to be reworked I think
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentid + '.json'
    data = {}
    for i in range(fields):l = models.CharFi
        data[fields[i]] = updated_values[i]
    r = requests.put(url, data)
    return r.json()

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