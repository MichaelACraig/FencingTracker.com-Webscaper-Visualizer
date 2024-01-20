import csv
import shutil

def regionFilter(inputFile,edgeCaseFile):
    #Create a copy of the currenty .csv file; backup purposes
    backupFile = inputFile.replace('.csv', '_backup.csv')
    shutil.copy(inputFile, backupFile)

    #Read the backupFile to get the fieldnames and place the region column in its respective position
    with open(backupFile, 'r') as csvfile:
            csvReader = csv.DictReader(csvfile)
            data = list(csvReader)

    fieldnames = list(data[0].keys())    
    fieldnames.append('Region')  

    #Edit the inputFile to include the new column
    with open(inputFile, 'w', newline='') as csvOutput:    
        csvWriter = csv.DictWriter(csvOutput, fieldnames=fieldnames)
        csvWriter.writeheader()

        #For every person/row in the .csv file, get the CLUBS information
        #Run a script to check which region they are in, place that region in the new column in its respective row
        for row in data:
            #If the person is apart of two clubs, create a new .csv file that stores that information for later edge-analysis
            if '/' in row['CLUBS']:
                with open(edgeCaseFile, 'a', newline='') as twoClubPeople:
                    twoClubWriter = csv.writer(twoClubPeople)
                    twoClubWriter.writerow([row['NAME'], row['CLUBS']])
                
                #Remove the person from the .csv file     
                continue

            #If the person is not apart of two clubs, continue with the region analysis
            #Separate the US into four regions; West, Midwest, Southern, and Northern regions

            #Using a list of all US states, if a club has a state in its name, assign that state to the person in the region column
            #If the person is in the US, place them in their respective region
                #Using a list for Midwest, West, South, and North regions, if a person's state is in one of these lists, replace the state with the region

            #If the person is not in the US, assign them to the 'Ambiguous' region; Could be International or just an ambiguous club name
            #We will have to manually check these people later




            #Test script
            row['Region'] = 'test'
            csvWriter.writerow(row)
        
    print("Complete")         
            
regionFilter("/Users/michaelcraig/Desktop/Projects/FencingTracker.com-Webscaper-Visualizer/Scraper1Outputs/ScrapedData.csv","/Users/michaelcraig/Desktop/Projects/FencingTracker.com-Webscaper-Visualizer/Scraper1Outputs/EdgeCases.csv")      
