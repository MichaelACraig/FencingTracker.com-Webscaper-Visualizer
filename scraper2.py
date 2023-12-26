from bs4 import BeautifulSoup
import csv
import requests
import os

#Pulls the name data from the top 50 clubs on FencingTracker
def pullLargestClubs(outputCSV):
    #Header element necessary for website access
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    url = "https://www.fencingtracker.com/largestclubs"
    finalLinks = []

    #Layered hyperlinks from the starting URL. Below shows hyperlink path for data collection:
    #Largest Clubs -> Club's rating -> Club's Members -> Individual Member Info -> /history to access Bout History
    # 4 Hyperlinks to move through Club's Members needs to loop through all members

    response = requests.get(url, headers=headers)
    doc = BeautifulSoup(response.text, 'html.parser')

    #Pulls all hyperlink data from the url webpage
    clubLinks = [link['href'] for link in doc.find_all('a', href=True)]

    #Cleans clubLinks array before scraping portion of the algorithm
    excludedClubLinks = [
        "/",
        "#",
        "/login",
        "/signup",
        "/largestclubs",
        "/largestclubs/by-non-competitive",
        "/largestclubs/by-total",
        "/privacy",
        "/contact",
        "/about",
        "/faq",
        "/discord",
        "/topclubs/epee",
        "/topclubs/foil",
        "/topclubs/saber",
        "/np/ranking/dv1me",
        "/np/ranking/dv1wf",
        "/np/ranking/dv1ws",
        "/np/ranking/dv1mf",
        "/np/ranking/dv1ms",
        "/np/ranking/dv1we",
        "/strength/ME/D",
        "/strength/MF/D",
        "/strength/MS/D",
        "/strength/WE/D",
        "/strength/WF/D",
        "/strength/WS/D",
    ]
    cleanClubLinks = [clubLink for clubLink in clubLinks if clubLink not in excludedClubLinks]    
 
    for cleanClubLink in cleanClubLinks:
        #First layer; Club URL from largestClubs page
        clubURL = "https://fencingtracker.com" + cleanClubLink
        clubResponse = requests.get(clubURL, headers=headers)
        clubSoup = BeautifulSoup(clubResponse.text, 'html.parser')

        #Second Layer; Club Ratings Page from Club URL
        secondLayerLinks = [
            "/epee",
            "/foil",
            "/saber",
        ]

        for secondLayerLink in secondLayerLinks:
            secondLayerSearchLink = "https://fencingtracker.com" + cleanClubLink + secondLayerLink
            searchResponse = requests.get(secondLayerSearchLink, headers=headers)

            if searchResponse.status_code == 200:

                #Third Layer; Member page from Club Ratings Page
                    membersSoup = BeautifulSoup(searchResponse.text, 'html.parser')
                    membersLinks = membersSoup.find_all('a')

                    for memberLink in membersLinks:
                        if memberLink not in excludedClubLinks:
                            href = memberLink.get('href')

                            if href is not None and href.startswith("/p/"):
                                finalLinks.append(href)
                                length = len(finalLinks)

                                #Output to CSV file
                                with open(outputCSV, 'w', newline='') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(['URL TAG'])
                                    for link in finalLinks:
                                        writer.writerow([link])

                #FOURTH LAYER IS UNNECESSARY SINCE WE CAN JUST APPEND /history LATER    
            
#Secondary Cleaning; All duplicate files are placed into a set, which is then outputted to a .csv file 
def cleanURLs(inputFile, outputFile):
    with open(inputFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        next(csvReader)

        #Place all items into a set to remove duplicates
        duplicateSet = set()
        for row in csvReader:
            duplicateSet.add(row[0])

        #Output to CSV file
        with open(outputFile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['URL TAG'])
            for link in duplicateSet:
                writer.writerow([link])


#Main Scraping Function; Pulls URLs in .csv created in pullLinks to generate data from FencingTracker
def scrapeAndExport(inputFile, url, outputFile):
    #Header element necessary for website access
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    with open(inputFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        next(csvReader)
        
        for row in csvReader:

            rowContent = ''.join(row)
            urlExtension = url + rowContent + "/history"
            print(urlExtension)

            #BeautifulSoup Basic Script
            result = requests.get(urlExtension, headers=headers)
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

            print("Appending is complete")
            #Reset index for tidiness
            index = 0

            #.csv file creation
            with open(outputFile, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if os.path.getsize(outputFile) == 0:
                    writer.writerow(['NAME', 'CLUBS', 'ATWins', 'ATLosses', 'winRatio', 'poolWins', 'poolLosses', 'poolWinRatio', 'DEWins', 'DELosses', 'DEWinRatio'])
                writer.writerow(statsArray)


#Chain of function calls to run the program; 
#Uncomment at each line for individual cases or uncomment all if you do not have other .csv files since the program will overwrite them

#pullLargestClubs('C:\\Users\\13212\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Outputs\\LargestClubsURLOutputs.csv')
#cleanURLs('C:\\Users\\13212\\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Outputs\\LargestClubsURLOutputs.csv', 'C:\\Users\13212\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Outputs\\CleanedLargestClubsURLOutputs.csv')
#scrapeAndExport('C:\\Users\\13212\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Outputs\\CleanedLargestClubsURLOutputs.csv', 'https://fencingtracker.com', 'C:\\Users\\13212\\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Outputs\\ScrapedData.csv')