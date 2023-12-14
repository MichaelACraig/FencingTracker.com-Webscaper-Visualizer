from pyvis.network import Network
import networkx as nx
import csv

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

#Retrieve .csv file and create the graph
def createFirstGraph(inputFile):
    
    #FIRST GRAPH: Cyclic and undirected
    net = Network(height=800, width=800, notebook=True)

    #Create a dictionary that stores the name of a group, and nodes that are in that group; If the group is not in the dictionary, add it
    groups = {}

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
            else:    
                groups[user.CLUBS].append(user.NAME)

            #for group in groups:
                #if group == "Nellya Fencers":
                    #print(groups[group])

            #For every group in the groups dictionary
            for group in groups:
                #For the first node and onward in the group
                for i in range(len(groups[group])):
                    #for the first node + 1 and onward in the group
                    for j in range(i+1, len(groups[group])):
                            #Create an edge between the two nodes
                            net.add_edge(groups[group][i], groups[group][j])
                            print("Edge created")


    net.show("firstGraph.html", notebook=False)


createFirstGraph("C:\\Users\\13212\\Desktop\\ProjectOutputs\\SampleData.csv")