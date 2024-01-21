# FencingTracker.com Webscraper
Webscraping script for FencingTracker.com <br>
Utilizes BeautifulSoup4 Library to scrape user data (All-time Statistics) into .csv format to be utilized by a multitude of different use cases <br>

SETUP/INSTALL:
Set up in a Virtual Enviornment (python3 -m venv venv) and activate (venv/Scripts/activate) and install libraries below: <br>
    1. BeautifulSoup4 (pip3 install beautifulsoup4) <br>
    2. Requests (pip3 install requests) <br>
    3. Pyvis (pip3 inbstall pyvis) <br>

WALKTHROUGH: <br>
    **ALL FILES ARE ALREADY CREATED; PLEASE REMOVE ALL DATA FROM YOUR OUTPUTS FILE IF YOU WISH TO FOLLOW THESE STEPS**<br>

  1. Lines 199-201 in scraper.py: Route your directory to you are currently storing your repo instance where the Outputs file is stored and link to Data file so files can be written <br>
      - Files are already written for you, so no need and runtime is really long, but if you want to update the Data (i.e FencingTracker updates) do step 1 <br>
  2. Uncomment commands and run scraper.py <br>
  3. Line 81 in visualizer.py: Route your directory to you are currently storing your repo instance where the Outputs file is stored and link to Data file so files can be written <br>
  4. Uncomment command and run visualizer.py. Using pyvis for formalities sake and practice with visualizer; Also takes a long time to load. Files are already outputted for you in Outputs <br>
  5. Line 81 in regionFilter.py: Route directory to where you are currently storing your repo instance where the Outputs is stored. <br>
  6. Uncomment command and run regionFilter.py to retrieve Regional Data and Two Club Fencer Data       
