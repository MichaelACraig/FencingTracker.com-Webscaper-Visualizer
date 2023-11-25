from bs4 import BeautifulSoup
import requests

#Header element necessary for website access
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

#BeautifulSoup Basic Script
url = "https://fencingtracker.com/p/100309761/Johnathan-Ballou/history"

result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

#Variables for easier assignment
#Pulls NAME; Finds the first item labeled under h1
NAME = doc.find('h1')
print(NAME.text)

#Pulls CLUB AFFILIATIONS
CLUBS = doc.find('h2')
print(CLUBS.text)

#Pulls Win/Loss Statistics Table
statsTable = doc.find('table')

#Stats Variable Creation
rows = statsTable.find_all('tr')

ATWins = ""
ATLosses = ""
winRatio = ""
poolWins = ""
poolLosses = ""
poolWinRatio = ""
DEWins = ""
DELosses = ""
DEWinRatio = ""

statsArray = [
    ATWins,
    ATLosses,
    winRatio,
    poolWins,
    poolLosses,
    poolWinRatio,
    DEWins,
    DELosses,
    DEWinRatio
]

#Proper parsing for all Variables; Populates statsArray
index = 0
for row in rows:
    cells = row.find_all('td')
    if cells:
        last_cell = cells[-1]
        statsArray[index] = last_cell.text
        print(statsArray[index])
        index += 1

#Reset index for tidiness
index = 0


#Variable Creation for competitionTables; Parsing for all elements in each competition table
competitionTables = doc.find_all('table')
competitionDict = {}

#Loop through all tables except the first three since irrelevant for collection
for competitionTable in competitionTables[3:]:
    print(competitionTable)
    
