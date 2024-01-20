from pyvis.network import Network
import networkx as nx
import csv
import time

"""
#Graph template
g = Network(height=800, width=800, notebook=True, cdn_resources="remote")
g.toggle_hide_edges_on_drag(True)
g.barnes_hut()
g.from_nx(nx.davis_southern_women_graph())
g.show("ex.html", notebook=False)
"""

#test test test

#Create a node class
class User:
    def __init__(self,NAME,CLUBS,ATWins,ATLosses,winRatio,poolWins,poolLosses,poolWinRatio,DEWins,DELosses,DEWinRatio):
        self.NAME = NAME
        self.CLUBS = CLUBS
        self.ATWins = ATWins
        self.ATLosses = ATLosses
        self.winRatio = winRatio
        self.poolWins = poolWins
        self.poolLosses = poolLosses
        self.poolWinRatio = poolWinRatio
        self.DEWins = DEWins
        self.DELosses = DELosses
        self.DEWinRatio = DEWinRatio

def createFirstGraph(inputFile):
    startTime= time.time()

    #FIRST GRAPH: Cyclic and undirected
    net = Network(height=800, width="100%", bgcolor="#222222", font_color="white")
    net.barnes_hut()

    #Create a dictionary that stores the name of a group, and nodes that are in that group; If the group is not in the dictionary, add it
    groups = {}
    visited = []

    with open(inputFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")
        next(csvReader)

        for row in csvReader:

            # Create a user instance from the csv file
            user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

            # If the group has not been created yet, create it
            if user.CLUBS not in groups:
                groups[user.CLUBS] = []

            # If the node has not been created yet, create it and insert it into its respective group; Label it as a visited node
            if user.NAME not in visited:
                groups[user.CLUBS].append(user.NAME)
                net.add_node(user.NAME, group=user.CLUBS)
                visited.append(user.NAME)

            # If the node under that name has been created, but the club is different, it is a different person; add them to their respective group
            elif user.NAME not in groups[user.CLUBS]:
                groups[user.CLUBS].append(user.NAME)
                net.add_node(user.NAME, group=user.CLUBS) 

        #For every group in the groups dictionary
        for group in groups:
            #For the first node and onward in the group
            for i in range(len(groups[group])):
                #for the first node + 1 and onward in the group
                for j in range(i+1, len(groups[group])):
                            #Create edge between nodes
                            net.add_edge(groups[group][i], groups[group][j])
                            
    endTime = time.time()
    elapsed_time = endTime - startTime

    print("Elapsed time: " + str(elapsed_time) + " seconds!")
    print("Edges created: " + str(net.num_edges()))

    net.show("FirstGraph.html", notebook=False)

createFirstGraph("C:\\Users\\13212\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Scraper1Outputs\\VisualizationData.csv")