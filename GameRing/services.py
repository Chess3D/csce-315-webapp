import os
import requests
import json
from riotwatcher import RiotWatcher
import challonge
import stripe
from flask import Flask, render_template, jsonify#, requests

API_USERS = {
    'challonge' : 'GigaV9',
}

API_KEYS = {
    'riot' : 'RGAPI-61fe3148-00b0-481a-863e-fc7044015e94',
    'challonge' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
    'stripe_secret_key' : 'sk_test_51IkuARLHCOtCmyr2UnAXwoyEyXov7TxNUDY64DINcawuBeW7zDxdRIm3oEQa6bAuIi1nRxRbNvJT7lFVLRpFCGJx00OOGFgnwY',
    'stripe_public_key' : 'pk_test_51IkuARLHCOtCmyr22HnRg7YnEpjTAHdWrlEJF7z2GzjNCF4mSkqzAVJC4ooyRJ6nCZEkXC7HXQ38ERBwaaEry6I400L2l8Lt6f'
}

'''
Begin challonge API
'''

'''
NOTE: There is a tournament ID and a tournament URL.
      Many of these commands use the tournament URL.
'''
#tournament API GET
#this can take tournament_id or tournament_url as an argument
#returns a list of tournament dictionaries
def get_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.show(tournament_url)

#tournament API POST
#parameters is a dictionary
#returns a dictionary
def create_tournament(**parameters):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    print(parameters['url'])
    return challonge.tournaments.create(**parameters)

#tournament API DELETE
#returns a dictionary of tournament information
def delete_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.destroy(tournament_url)

#tournament API PUT
#update tournament information
#returns dictionary of tournament information
def update_tournament(tournament_url, **params):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.update(tournament_url, **params)

#tournament API POST
#processes checkins
#this should be done before the tournament starts, but after the checkin window
#This marks participants who have not checked in as inactive
#This moves inactive participants to bottom seeds
#This transitions the tournament state from checking_in to checked_in
#might return tournament information
def process_checkins_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.process_check_ins(tournament_url)

#tournament API POST
#aborts tournament check in process
#this is the only way to edit the start_at or check_in_duration
#might return tournament information
def abort_checkin_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.abort_check_in(tournament_url)

#tournament API POST
#starts the tournament
#the tournament must have at least 2 participants
#might return tournament information
def start_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.start(tournament_url)

#tournament API POST
#finalize tournament results
#must have all match scores submitted, renders results permanent
#might return tournament information
def finalize_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.finalize(tournament_url)

#tournament API POST
#clears all scores and attatchments
#participants can be added, edited, or removed after it is cleared.
#might return tournament information
def reset_tournament(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.tournaments.reset(tournament_url)

'''
NOTE: What is referred to as a 'participant' is a team.
      Members of said team are stored in our database.
'''

#participants API GET
#returns a list of participants and their information for a single tournament
def get_participants(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.index(tournament_url)

#participants API GET
#requires tournament url and participant id
#returns a single participant as a dictionary
def get_participant(tournament_url, participant_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.show(tournament_url, participant_id)

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
def remove_participant(tournament_url, participant_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.destroy(tournament_url, participant_id)

#participants API POST
#sets checked_in_at to current time
#might return participant details
def checkin_participant(tournament_url, participant_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.check_in(tournament_url, participant_id)
    #return True

#participants API POST
#sets checked_in_at to null
#might return participant details
def checkin_participant(tournament_url, participant_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.check_in(tournament_url, participant_id)
    #return False

'''
NOTE: Matches refer to each match of a tournament.
      A match can have multiple games.
      The score is updated by passing it as a **param
      in update_match as a comma separated string.
      You must also provide a winnerid, the id of the winning team.
      This id is the participant_id that is from the challonge API.
      EXAMPLE: "3-1,1-3" - I am not 100 on the logistics of the score_csv.

'''

#matches API GET
#returns list of matches for a tournament
def get_matches(tournament_url):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.index(tournament_url)

#match API GET
#returns single match details, participant_id
def get_match(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.show(tournament_url, match_id)

#match API PUT
#returns updated match details
def update_match(tournament_url, match_id, **params):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.update(tournament_url, match_id, **params)

#match API POST
#reopens match, resets matches that follow it
#returns match details
def reopen(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.reopen(tournament_url, match_id)

#match API POST
#mark match as underway
#sets underway_at to current time and highlights match in bracket
#returns match details
def reopen(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.mark_as_underway(tournament_url, match_id)

#match API POST
#unmark match as underway
#sets underway_at to null and unhighlights match
#returns match details

def reopen(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.unmark_as_underway(tournament_url, match_id)

'''
Riot API Begin
'''
#Riot API
#GET most recent match from Riot ID might change how this works if it's easier
#returns match id
def get_lol_match(gameName, tagLine):
    api_key = API_KEYS['riot']
    riot = RiotWatcher(api_key)
    account_info = riot.account.by_riot_id('americas', gameName, tagLine)
    puuid = account_info["puuid"]
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=1&api_key=' + api_key
    match = requests.get(url).json()
    return match[0]


#Riot API
#GET most recent match information
#returns dictionary of match information
def get_lol_match_info(matchid):
    api_key = API_KEYS['riot']
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + matchid + '?api_key=' + api_key
    match_info = requests.get(url).json()
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
