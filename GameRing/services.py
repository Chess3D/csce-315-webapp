import os
import requests
import json
from riotwatcher import RiotWatcher

'''
Begin challonge API
'''

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
#returns a dictionary
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
#returns a dictionary of tournament information
def delete_tournament(tournamentid):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentid + '.json'
    r = requests.delete(url)
    return r.json()


#tournament API PUT
#update tournament information
#returns dictionary of tournament information
def update_tournament(tournamentid, fields, updated_values): #this needs to be reworked I think
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentid + '.json'
    data = {}
    for i in range(fields):
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
#returns a single participant as a dictionary
def get_participant(tournamentURL, participantID):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/' + participantID + '.json'
    r = requests.get(url)
    return r.json()

#participants API POST
#parameters is a dictionary, currently only contains name of the participant
#returns dictionary of participant's information
def add_participant(parameters):
    url = 'https://api.challonge.com/v1/tournaments.json'
    data = {'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
            'name' : parameters['name']}
    r = requests.post(url, data)
    return r.json()

#participants API DELETE
#if tournament has not started, participant is removed from the tournament
#if tournament has started, participant is marked as inactive, ff'ing remaining matches
#returns dictionary of participant information
def remove_participant(tournamentURL, participantID):
    url = url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/' + participantID + '.json'
    r = requests.delete(url)
    return r.json()


'''
Riot API Begin
'''
#Riot API
#GET most recent match from Riot ID might change how this works if it's easier
#returns match id
def get_match(gameName, tagLine):
    api_key = 'RGAPI-cbf487de-6523-4f82-83b7-9d9c3f9b3663'
    riot = RiotWatcher(api_key)
    account_info = riot.account.by_riot_id('americas', gameName, tagLine)
    puuid = account_info["puuid"]
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=1&api_key=' + api_key
    match = get(url).json()
    return match[0]

#Riot API
#GET most recent match information
#returns dictionary of match information
def get_match_info(matchid):
    api_key = 'RGAPI-cbf487de-6523-4f82-83b7-9d9c3f9b3663'
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + matchid + '?api_key=' + api_key
    match_info = get(url).json()
    return match_info

#Riot API
#GET Verify account
def verify_account(gameName, tagLine):
    api_key = 'RGAPI-940a6874-2d97-4823-919c-dd329df7ffc5'
    riot = RiotWatcher(api_key)
    try:
        account_info = riot.account.by_riot_id('americas', gameName, tagLine)
        return True
    except exceptions.HTTPError:
        return False
    print(type(account_info))
    return True
