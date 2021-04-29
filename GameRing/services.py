import os
import requests
import json
from riotwatcher import RiotWatcher
import challonge

API_USERS = {
    'challonge' : 'GigaV9',
}

API_KEYS = {
    'riot' : 'RGAPI-0f4c9ac1-13f0-4c5f-937e-d0c918cb015f',
    'challonge' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
}



'''
Begin challonge API
'''


#tournament API GET
#returns a list of dictionaries, i think
def get_tournament(tournament_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.show(tournament_id)


#tournament API POST
#parameters is a dictionary
#returns a dictionary
def create_tournament(**parameters):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    print(parameters['url'])
    return challonge.tournaments.create(**parameters)['id']


#tournament API DELETE
#returns a dictionary of tournament information
def delete_tournament(tournamentID):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentID + '.json'
    r = requests.delete(url)
    return r.json()


#tournament API PUT
#update tournament information
#returns dictionary of tournament information
def update_tournament(tournamentID, fields, updated_values): #this needs to be reworked I think
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentID + '.json'
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
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/participants.json'
    r = requests.get(url, headers={'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp'})
    participants = r.json()
    participant_list = []

    for i  in range(len(participants['participant'])):
        participant_list.append(participants['participant'][i])
    return participant_list


#participants API GET
#requires tournament url and participant id
#returns a single participant as a dictionary
def get_participant(tournamentURL, participant_id):
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentURL + '/' + participant_id + '.json'
    r = requests.get(url)
    return r.json()


#participants API POST
#parameters is a dictionary, currently only contains name of the participant
#returns dictionary of participant's information
def add_participant(tournament_url, participant_name):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.create(tournament_url, participant_name)


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
    api_key = API_KEYS['riot']
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
    api_key = API_KEYS['riot']
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + matchid + '?api_key=' + api_key
    match_info = get(url).json()
    return match_info


#Riot API
#GET Verify account
def verify_account(gameName, tagLine):
    api_key = API_KEYS['riot']
    riot = RiotWatcher(api_key)

    try:
        riot.account.by_riot_id('americas', gameName, tagLine)
        return True
    except requests.exceptions.HTTPError:
        return False