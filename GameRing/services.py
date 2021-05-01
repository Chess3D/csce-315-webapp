import os
import requests
import json
from riotwatcher import RiotWatcher, LolWatcher
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
def undo_checkin_participant(tournament_url, participant_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.participants.undo_check_in(tournament_url, participant_id)
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
def reopen_match(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.reopen(tournament_url, match_id)


#match API POST
#mark match as underway
#sets underway_at to current time and highlights match in bracket
#returns match details
def mark_match_underway(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.mark_as_underway(tournament_url, match_id)


#match API POST
#unmark match as underway
#sets underway_at to null and unhighlights match
#returns match details


def unmark_match_underway(tournament_url, match_id):
    challonge.api.set_credentials(API_USERS['challonge'], API_KEYS['challonge'])
    return challonge.matches.unmark_as_underway(tournament_url, match_id)


'''
Riot API Begin
'''

#verifies that the riot id exists
#takes riot id
#returns True if the id exists
#returns False if the id does not exist
def verify_account(gameName, tagLine):
    api_key = API_KEYS['riot']
    riot = RiotWatcher(api_key)
    try:
        riot.account.by_riot_id('americas', gameName, tagLine)
        return True
    except requests.exceptions.HTTPError:
        return False


def get_puuid(gameName, tagLine):
    api_key = 'RGAPI-61fe3148-00b0-481a-863e-fc7044015e94'
    riot = RiotWatcher(api_key)
    account_info = riot.account.by_riot_id('americas', gameName, tagLine)
    puuid = account_info["puuid"]
    return puuid


#gets the match id for the most recent match on a player's match history
#takes riot id
#returns the single match's id
#returns none if list is empty
def get_lol_match_id(gameName, tagLine):
    puuid = get_puuid(gameName, tagLine)
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=1&api_key=' + API_KEYS["riot"]
    match_id = requests.get(url).json()
    if len(match_id) == 0:
        return None
    else:
        return match_id[0]


#finds league of legends match information from a participant's riot id
#takes riot id
#returns the dictionary of match information
#returns none of match id is not found
def get_lol_match_info(gameName, tagLine):
    match_id = get_lol_match_id(gameName, tagLine)
    if match_id is None:
        return None
    else:
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + API_KEYS["riot"]
        match_info = requests.get(url).json()
        return match_info


#finds team's match id in relation to team captain's puuid
#match_info is the dictionary of match info and puuid is a puuid
#returns a team's id for the specific match
#returns None if not found
def find_team_id(match_info, puuid):
    participant_list = match_info["info"]["participants"]
    for p in participant_list:
        if p["puuid"] == puuid:
            return p["teamId"]
        else:
            return None


#finds the winning team captain's puuid in lol_match_info
#match_info is a dictionary of match info
#team1_puuid and team2_puuid are puuids
#returns winning team captain's puuid
#returns None otherwise
def find_winner_id(match_info, team1_puuid, team2_puuid):
    team1_id = find_team_id(match_info, team1_puuid)
    if (match_info["teams"][0]["win"] == True) and (match_info["teams"][0]["teamId"] == team1_id):
        return team1_puuid
    elif (match_info["teams"][0]["win"] == False) and (match_info["teams"][0]["teamId"] == team1_id):
        return team2_puuid
    else:
        return None


#gets the winning team's name
#team1 and team 2 are dictionaries that contains
#the team name and the team captain's Riot ID in the following format
# {"teamName": "<name>", "gameName": "<game name>", "tagLine: "<tag line>"}
#Returns the winning team's name
#Returns not if the match was not found or if winning team captain's puuid does not match
def get_winner(team1, team2):
    team1_match_info = get_lol_match_info(team1["gameName"], team1["tagLine"])
    team2_match_info = get_lol_match_info(team2["gameName"], team2["tagLine"])

    if int(team1_match_info["metadata"]["matchId"]) == int(team2_match_info["metadata"]["matchId"]):
        team1_puuid = get_puuid(team1["gameName"], team1["tagLine"])
        team2_puuid = get_puuid(team2["gameName"], team2["tagLine"])
        winner_id = find_winner_id(team1_match_info, team1_puuid, team2_puuid)
        if winner_id == team1_puuid:
            return team1["teamName"]
        elif winner_id == team2_puuid:
            return team2_puuid
        else:
            return None
    else:
        return None