import os
import requests
import json

#tournament API GET
def get_tournaments():
    url = 'https://api.challonge.com/v1/tournaments/'
    r = requests.get(url, headers={'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp'})
    tournaments = r.json()
    tournament_list = []
    for i  in range(len(tournaments['tournament'])):
        tournament_list.append(tournaments['tournament'][i])
    return tournament_list

#tournament API POST
def create_tournament(parameters):
    url = 'https://api.challonge.com/v1/tournaments.json'
    data = {'api_key' : '7bG0Ob124vNhDgKA0oktDfuRgiC5jKziYPTF3NUp',
            'name' : parameters['name'],
            'game_name' : parameters['tournamentGameName'],
            'tournament_type' : parameters['tournamentType'],
            'grand_finals_modifer' : parameters['tournamentGrandFinalsMod'],
            'signup_cap' : parameters['tournamentSignUpCap'],
            'start_at' : parameters['tournamentStartDate'],
            'hold_third_place_match' : parameters['tournamentThirdPlaceMatch'],
            'show_rounds' : parameters['tournamentShowRounds'],
            'private' : 'true',
            'description' : parameters['tournamentDescription']
            }
    r = requests.post(url, data)
    return r.json()

#tournament API DELETE
def delete_tournament(tournamentid)
    url = 'https://api.challonge.com/v1/tournaments/' + tournamentid + '.json'
    r = requests.delete(url)
    return r.josn()