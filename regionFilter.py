import csv
import shutil

#Lists containing all US states and their respective regions
USStates = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
            'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
            'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
            'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
            'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
            'Wisconsin', 'Wyoming']

Midwest = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota',
           'Ohio', 'South Dakota', 'Wisconsin']

West = ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico',
        'Oregon', 'Utah', 'Washington', 'Wyoming']

South = ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi',
         'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia']

North = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania',
         'Rhode Island', 'Vermont']

def regionFilter(inputFile,edgeCaseFile,outputFile):
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
    with open(outputFile, 'w', newline='') as csvOutput:    
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
            for state in USStates:
                if state in USStates and state in row['CLUBS']:
                    #If the person is in the US, place them in their respective region
                    if state in Midwest:
                        row['Region'] = 'Midwest'

                    elif state in West:
                        row['Region'] = 'West'

                    elif state in South:
                        row['Region'] = 'South'

                    #Else clause: Person is in the Northern region of the US
                    else:
                        row['Region'] = 'North'    

                    #Write the row to the .csv file
                    csvWriter.writerow(row)
                    continue

    print("Complete")         

regionFilter("/Users/michaelcraig/Desktop/Projects/FencingTracker.com-Webscaper-Visualizer/Outputs/ScrapedData.csv","/Users/michaelcraig/Desktop/Projects/FencingTracker.com-Webscaper-Visualizer/Outputs/TwoClubFencers.csv", "/Users/michaelcraig/Desktop/Projects/FencingTracker.com-Webscaper-Visualizer/Outputs/RegionData.csv")