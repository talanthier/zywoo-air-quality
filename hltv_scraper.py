import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


df_match_data = pd.DataFrame(columns = ['URL', 'Match Date', 'Team', 'Team Score', 'Opponent', 'Opponent Score', 'matchType', 'K/D', '+/-', 'Rating'])

player_matches_url ='https://www.hltv.org/stats/players/matches/11893/zywoo?matchType=Lan'

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

driver.get(player_matches_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

matches_table = soup.find('table', attrs={'class':'stats-table no-sort'}).find('tbody')
match_rows = matches_table.find_all('tr')
print(match_rows[0])

data = []
for row in match_rows:
	row_data = row.find_all('td')
	team_info = row_data[1].find_all('span')
	opponent_info = row_data[2].find_all('span')
	row_dict = {'URL' : row_data[0].find('a')['href'], 
				'Match Date' : row_data[0].find('div').text,
				'Team' : team_info[0].text, 
				'Team Score' : team_info[1].text,
				'Opponent' : opponent_info[0].text,
				'Opponent Score' : opponent_info[1].text,
				'Match Type' : row_data[3].text,
				'K/D'  : row_data[4].text, 
				'+/-' : row_data[5].text, 
				'Rating' : row_data[6].text}
	data.append(row_dict)
	#data.append([row_data[0].find('a')['href'], row_data[0].find('div').text, team_info[0].text, team_info[1].text, opponent_info[0].text, opponent_info[1].text, row_data[3].text, row_data[4].text, row_data[5].text, row_data[6].text])

df_match_data = pd.DataFrame(data, columns = ['URL', 'Match Date', 'Team', 'Team Score', 'Opponent', 'Opponent Score', 'matchType', 'K/D', '+/-', 'Rating'])
print(df_match_data)

#df_match_data.to_csv('C:/Users/talan/Documents/Github/zywoo-air-quality/zywoo_matches.csv', index = False)


player_events_url = 'https://www.hltv.org/stats/players/events/11893/zywoo?matchType=Lan'

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

driver.get(player_events_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

events_table = soup.find('table', attrs={'class':'stats-table'}).find('tbody')
event_rows = events_table.find_all('tr')
print(match_rows[0])

event_data = []
for row in event_rows:
	row_data = row.find_all('td')
	row_dict = {'Place' : row_data[0].text,
				'Event Name' : row_data[1].text,
				'Event URL ' : row_data[1].find('a')['href'],
				'Team' : row_data[2].text,
				'Maps' : row_data[3].text,
				'Event KPR-DPR' : row_data[4].text,
				'Event +/-' : row_data[5].text,
				'Event Rating' : row_data[6].text}
	event_data.append(row_dict)

df_events_data = pd.DataFrame(event_data)

df_events_data.to_csv('C:/Users/talan/Documents/Github/zywoo-air-quality/zywoo_events.csv', index = False)
