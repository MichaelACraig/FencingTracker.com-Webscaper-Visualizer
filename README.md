# FencingTracker.com Webscraper
Webscraping script for FencingTracker.com <br>
Utilizes BeautifulSoup4 Library to scrape user data (All-time Statistics) into .csv format to be utilized by a multitude of different use cases <br>

SETUP/INSTALL:
Set up in a Virtual Enviornment (python3 -m venv venv) and activate (venv/Scripts/activate) and install libraries below: <br>
    1. BeautifulSoup4 (pip3 install beautifulsoup4) <br>
    2. Requests (pip3 install requests) <br>
    3. Pyvis (pip3 inbstall pyvis) <br>

WALKTHROUGH: <br>
  1. Lines 199-201 in scraper.py: Route your directory to you are currently storing your repo instance and link to Data file so files can be written <br>
      - Files are already written for you, so no need and runtime is really wrong, but if you want to update the Data (i.e FencingTracker updates) do step 1 <br>
  2. Uncomment commands and run scraper.py <br>
  3. Line 81 in visualizer.py: Route your directory to you are currently storing your repo instance and link to Data file so files can be written <br>
  4. Uncomment command and run visualizer.py <br>       
