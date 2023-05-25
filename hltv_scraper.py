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
	print(row_data[0].find('a')['href']) # column 0 for date
	print(row_data[0].find('div').text)
	team_info = row_data[1].find_all('span')
	print(team_info[0].text)
	print(team_info[1].text)
	opponent_info = row_data[2].find_all('span')
	print(opponent_info[0].text)
	print(opponent_info[1].text)
	print(row_data[3].text)
	print(row_data[4].text)
	print(row_data[5].text)
	print(row_data[6].text)
	data.append([row_data[0].find('a')['href'], row_data[0].find('div').text, team_info[0].text, team_info[1].text, opponent_info[0].text, opponent_info[1].text, row_data[3].text, row_data[4].text, row_data[5].text, row_data[6].text])

df_match_data = pd.DataFrame(data, columns = ['URL', 'Match Date', 'Team', 'Team Score', 'Opponent', 'Opponent Score', 'matchType', 'K/D', '+/-', 'Rating'])
print(df_match_data)

df_match_data.to_csv('C:/Users/talan/Documents/Github/zywoo-air-quality/zywoo_matches.csv', index = False)
