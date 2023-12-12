# FencingTracker.com Webscraper and Visualizer
Webscraping script for FencingTracker.com

Utilizes BeautifulSoup4 Library to scrape user data (All-time Statistics) into .csv format to be utilized by a multitude of different use cases

SETUP/INSTALL:
Set up in a Virtual Enviornment and install these libraries (python3 -m venv venv)
    1. BeautifulSoup4 (pip3 install beautifulsoup4)
    2. requests (pip3 install requests)


Node structure (Visualizations Sake):
  NAME
  CLUB AFFILIATION

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
-Webscraper does not include unattached members; Find workaround? Might need a dynamic approach to solve (Selenium)
