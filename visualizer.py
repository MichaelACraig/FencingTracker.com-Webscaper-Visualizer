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
            #For each row in the .csv file, create a node
            user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

            
            net.add_node(user.NAME, group=user.CLUBS)

            #If there is not a key in the groups dictionary, add it to the dictionary
            if user.CLUBS not in groups:
                groups[user.CLUBS] = [user.NAME]
                visited.append(user.NAME)
            #If there is already a node under the user.NAME and its user.CLUBS
            elif user.NAME in visited and user.NAME not in groups[user.CLUBS]:
                print("Duplicate name in a different club found")

            #If a user is in multiple clubs, add them to the dictionary under the clubs they are in
            elif '/' in user.CLUBS:
                 print('User is in multiple clubs')     
            else:    
                groups[user.CLUBS].append(user.NAME)
                visited.append(user.NAME)

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

createFirstGraph("C:\\Users\\13212\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\Data\\VisualizationData.csv")