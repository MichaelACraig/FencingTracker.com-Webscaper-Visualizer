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
  6. Uncomment command and run regionFilter.py to retrieve Regional Data and Two Club Fencer Data <br>
  
  <br>
  <br>
  <br>

ANALYSIS WALKTHROUGH: <br>
**IF YOU'RE LOOKING TO REPLICATE THIS ANALYSIS, FOLLOW THESE STEPS, ELSE THEY'RE ALL LOADED FOR YOU**

1. Install Pandoc if using a IDE other than RStudio: https://github.com/jgm/pandoc/releases/tag/3.1.11.1 <br>

2. Install the following packages to your local machine or venv: <br>
    - leaflet <br>
    - htmlwidgets <br>
    - ggplot2 <br>
    - maps <br>
    - sf <br>

2. Set your working directory to where you have your repo stored <br>

3. Unzip geojsonio so it can be used within your working directory
    -EXAMPLE: unzip("C:\\PATH\\MOREPATH\\EVENMOREPATH\\KEEPGOING\\Temp\\RtmpsXQV2B\\downloaded_packages\\geojsonio_0.11.3.zip")

4. Adjust line 14 in code to your geojsonio file in your working directory



