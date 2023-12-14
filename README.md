# FencingTracker.com Webscraper
Webscraping script for FencingTracker.com

Visualizer WIP

Utilizes BeautifulSoup4 Library to scrape user data (All-time Statistics) into .csv format to be utilized by a multitude of different use cases

SETUP/INSTALL:
Set up in a Virtual Enviornment (python3 -m venv venv) and activate (venv/Scripts/activate) and install libraries below:
    1. BeautifulSoup4 (pip3 install beautifulsoup4)
    2. Requests (pip3 install requests)
    3. Pyvis (pip3 inbstall pyvis)

WALKTHROUGH:
  1. Lines 199-201 in scraper.py: Route your directory to you are currently storing your repo instance and link to Data file so files can be written
      - Files are already written for you, so no need and runtime is really wrong, but if you want to update the Data (i.e FencingTracker updates) do step 1
  2. Uncomment commands and run scraper.py
  3. Line 81 in visualizer.py: Route your directory to you are currently storing your repo instance and link to Data file so files can be written
  4. Uncomment command and run visualizer.py          


Depending on the graph being visualized, below is what the Node will store in order of hierarchy
  NAME
  CLUB AFFILIATION
  All-Time Win/Loss Statistics

All-time Win/Loss Statistics (Array Implementation):
  Wins
  Losses
  Win Ratio
  Pool Wins
  Pool Losses
  Pool Win Ratio
  DE Wins
  DE Losses
  DE Ratio

Devlog:
-Webscraper is complete and can scrape all data from the /largestclubs page, which includes all competitive members of all clubs
  -Does not include unattached members; Find workaround? Might need a dynamic approach to solve (Selenium)

-Visualizer for first graph is almost complete; Edge Cases
  -If there is a person with the same name and is in a different club, create both nodes and add them to their respective clubs
    -This could result in a much slower runtime, so find a workaround and optimize (think about it)

  -If a person belongs to multiple clubs
    -If a person has a / in their user.CLUBS, count the number of /'s in the name and parse it. Create edges to that node's teammates in both clubs  
