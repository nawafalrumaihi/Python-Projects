# write a script that can scrape data from a website and sort it

import requests
from bs4 import BeautifulSoup
import re

# get the data from the website
url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# find the table
table = soup.find('table', attrs={'id': 'per_game_stats'})

# find the headers
headers = table.find_all('th')
headers = [header.text for header in headers]

# find the rows
rows = table.find_all('tr')
rows = [row.text for row in rows]

# find the data
data = table.find_all('td')
data = [data.text for data in data]

# find the players
players = table.find_all('a')
players = [player.text for player in players]

# find the teams
teams = table.find_all('a', attrs={'href': re.compile("^/teams/")})
teams = [team.text for team in teams]

# find the positions
positions = table.find_all('td', attrs={'data-stat': 'pos'})
positions = [position.text for position in positions]

# find the ages
ages = table.find_all('td', attrs={'data-stat': 'age'})
ages = [age.text for age in ages]

# find the games played
games_played = table.find_all('td', attrs={'data-stat': 'g'})
games_played = [game.text for game in games_played]

# find the minutes played
minutes_played = table.find_all('td', attrs={'data-stat': 'mp_per_g'})
minutes_played = [minute.text for minute in minutes_played]

# find the field goals made
field_goals_made = table.find_all('td', attrs={'data-stat': 'fg_per_g'})
field_goals_made = [field_goal.text for field_goal in field_goals_made]

# find the field goals attempted
field_goals_attempted = table.find_all('td', attrs={'data-stat': 'fga_per_g'})
field_goals_attempted = [field_goal.text for field_goal in field_goals_attempted]

# find the field goal percentage
field_goal_percentage = table.find_all('td', attrs={'data-stat': 'fg_pct'})
field_goal_percentage = [field_goal.text for field_goal in field_goal_percentage]

# find the 3-point field goals made
three_point_field_goals_made = table.find_all('td', attrs={'data-stat': 'fg3_per_g'})
three_point_field_goals_made = [three_point_field_goal.text for three_point_field_goal in three_point_field_goals_made]

# print the data
print(headers)
print(rows)
print(data)
print(players)
print(teams)
print(positions)
print(ages)
print(games_played)
print(minutes_played)
print(field_goals_made)
print(field_goals_attempted)
print(field_goal_percentage)
print(three_point_field_goals_made)

# sort the data into dictionaries
player_data = {}
for i in range(len(players)):
    player_data[players[i]] = {
        'Team': teams[i],
        'Position': positions[i],
        'Age': ages[i],
        'Games Played': games_played[i],
        'Minutes Played': minutes_played[i],
        'Field Goals Made': field_goals_made[i],
        'Field Goals Attempted': field_goals_attempted[i],
        'Field Goal Percentage': field_goal_percentage[i],
        '3-Point Field Goals Made': three_point_field_goals_made[i]
    }
