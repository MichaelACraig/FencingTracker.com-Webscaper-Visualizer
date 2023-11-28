from bs4 import BeautifulSoup
import csv
import pandas
import requests

#Pulls the name data from the top 50 clubs on FencingTracker
def pullLargestClubs():
    url = "https://www.fencingtracker.com/largestclubs"

    #Layered hyperlinks from the starting URL. Below shows hyperlink path for data collection:
    #Largest Clubs -> Club's rating -> Club's Members -> Individual Member Info -> /history to access Bout History
    # 4 Hyperlinks to move through Club's Members needs to loop through all members

    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')

    #Pulls all hyperlink data from the url webpage; Slices the top 50
    clubLinks = [link['href'] for link in doc.find_all('a', href=True)][:50]

    for clubLink in clubLinks:
        #First layer; Club URL from largestClubs page
        clubURL = "https://fencingtracker.com" + clubLink
        clubResponse = requests.get(clubURL)
        clubSoup = BeautifulSoup(clubResponse.text, 'html.parser')

        #Second Layer; Club Ratings Page from Club URL
        ratingLink = clubSoup.find('a', {'id': ''})

        #Third Layer; Names Page from Club Ratings Page
        #Needs to be looped!
            #Fourth layer: Name with access to the /history



#Main scraping method; Pulls URLs in .csv created in pullLinks to generate data from FencingTracker
def scrapeAndExport(url, outputFile):
    #Header element necessary for website access
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    #BeautifulSoup Basic Script
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")

    #Variables for easier assignment
    #Pulls NAME; Finds the first item labeled under h1
    NAME = doc.find('h1')

    #Pulls CLUB AFFILIATIONS
    CLUBS = doc.find('h2')

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

    #Placeholders for the stats; Shows variable to index representation
    statsArray = [
        NAME.text, #.text is needed to remove HTML tags
        CLUBS.text,
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
    index = 2
    for row in rows:
        cells = row.find_all('td')
        if cells:
            last_cell = cells[-1]
            statsArray[index] = last_cell.text
            index += 1

    #Reset index for tidiness
    index = 0

    #.csv file creation
    with open(outputFile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['NAME', 'CLUBS', 'ATWins', 'ATLosses', 'winRatio', 'poolWins', 'poolLosses', 'poolWinRatio', 'DEWins', 'DELosses', 'DEWinRatio'])
        writer.writerow(statsArray)

#Example Call 
scrapeAndExport('www.fencingtracker.com/p/100309761/Johnathan-Ballou/history',
        '/Users/michelecraig/Desktop/My Project Files/Python/FencingTrackerCSVOutputs/output.csv')