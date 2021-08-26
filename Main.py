import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from AStarAlgorithm import AStarAlgorithm

G = nx.Graph()


#-----------------------------------------------------------------------------------------------------#
#------------------------------USER INITIAL INPUT FOR GRID CONFIGURATION------------------------------#
#-----------------------------------------------------------------------------------------------------#
rows = int(input("Please enter how many rows in your grid: "))
columns = int(input("Please enter how many columns in your grid: "))
cells = np.empty([rows,columns], dtype=str)
number_of_cells = rows*columns
print("You have " + str(number_of_cells) + " cells in your grid. Please enter what you want to assign to them")
print("Enter 'Q' for Quarantine zone")
print("Enter 'V' for Vaccination zone")
print("Enter 'P' for Playground zone")
print("Enter 'N' for None")

for i in range(0, rows):
   for j in range(0, columns):
        cells[i][j] = input("enter zone type for cell " + str(i) + "," + str(j) + ": ")
#-----------------------------------------------------------------------------------------------------#
#------------------------------USER INITIAL INPUT FOR GRID CONFIGURATION------------------------------#
#-----------------------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------------------#
#----------------------------------------POPULATING THE MAP-------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
#the zones
for i in range(rows):
   for j in range(columns):
       G.add_node(cells[i][j]+str(i)+str(j), pos=(i+0.5,j+0.5))

#the coordinates
for i in range(rows+1):
    for j in range(columns+1):
        G.add_node((i,j), pos=(i,j), isQuarantine=False, isStart=False, isEnd=False)

#checking if a coordinate belongs to a quarantine zone
for i in range(rows):
    for j in range(columns):
        if(cells[i][j])=='Q':
            G.nodes[(i,j)]['isQuarantine'] = True
            G.nodes[(i,j+1)]['isQuarantine'] = True
            G.nodes[(i+1,j)]['isQuarantine'] = True
            G.nodes[(i+1,j+1)]['isQuarantine'] = True
#-----------------------------------------------------------------------------------------------------#
#----------------------------------------POPULATING THE MAP-------------------------------------------#
#-----------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------#
#------------------------------USER INITIAL INPUT FOR THEIR COORDINATES-------------------------------#
#-----------------------------------------------------------------------------------------------------#
#starting coordinates input
print("Please enter the starting coordinate")
startingX = int(input("Enter the x value: "))
startingY = int(input("Enter the y value: "))

startingCoordinates = (startingX, startingY)

#ending coordinates input
print("Please enter the ending coordinate")
endingX = int(input("Enter the x value: "))
endingY = int(input("Enter the y value: "))

endingCoordinates = (endingX, endingY)


#if the starting point is quarantine. We have already arrived at our destination
if G.nodes[(startingX,startingY)]['isQuarantine']==True:
    print("You have already arrived at your destination. Goodbye")
    exit()
   
#a print statement, just to tell the user that their destination is not the quarantine zone
if G.nodes[(endingX,endingY)]['isQuarantine']==False:
    print("Your destination is not a quarantine zone")

G.nodes[startingCoordinates]['isStart']==True
G.nodes[endingCoordinates]['isEnd']==True
#-----------------------------------------------------------------------------------------------------#
#------------------------------USER INITIAL INPUT FOR GRID CONFIGURATION------------------------------#
#-----------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------#
#------------------------------ADDING EDGES FOR THE GRAPH MATPLOTLIB GUI------------------------------#
#-----------------------------------------------------------------------------------------------------#
#horizontally
for i in range(rows):
    for j in range(columns):
        if j == 0:
            if(cells[i][j]=='Q'):
                G.add_edge((i,j), (i+1, j), weight=0)
            if(cells[i][j]=='V'):
                G.add_edge((i,j), (i+1, j), weight=2)        
            if(cells[i][j]=='P'):
                G.add_edge((i,j), (i+1, j), weight=3)   
            if(cells[i][j]=='N'):
                G.add_edge((i,j), (i+1, j), weight=1)

        elif j == (columns-1):
            if(cells[i][j-1]=='Q' and cells[i][j]=='Q'):
                G.add_edge((i,j), (i+1, j), weight=0)
            if((cells[i][j-1]=='Q' and cells[i][j]=='V') or (cells[i][j-1]=='V' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=1)
            if((cells[i][j-1]=='Q' and cells[i][j]=='P') or (cells[i][j-1]=='P' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=1.5)
            if((cells[i][j-1]=='Q' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=0.5)

            if(cells[i][j-1]=='V' and cells[i][j]=='V'):
                G.add_edge((i,j), (i+1, j), weight=2)
            if((cells[i][j-1]=='V' and cells[i][j]=='P') or (cells[i][j-1]=='P' and cells[i][j]=='V')):
                G.add_edge((i,j), (i+1, j), weight=2.5)
            if((cells[i][j-1]=='V' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='V')):
                G.add_edge((i,j), (i+1, j), weight=1)

            if((cells[i][j-1]=='P' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='P')):
                G.add_edge((i,j), (i+1, j), weight=2)

            if((cells[i][j-1]=='N' and cells[i][j]=='N')):
                G.add_edge((i,j),(i+1,j), weight=1)  


            if(cells[i][j]=='Q'):
                G.add_edge((i,j+1), (i+1, j+1), weight=0)
            if(cells[i][j]=='V'):
                G.add_edge((i,j+1), (i+1, j+1), weight=2)           
            if(cells[i][j]=='P'):
                G.add_edge((i,j+1), (i+1, j+1), weight=3)
            if(cells[i][j]=='N'):
                G.add_edge((i,j+1), (i+1, j+1), weight=1)

        else:
            if(cells[i][j-1]=='Q' and cells[i][j]=='Q'):
                G.add_edge((i,j), (i+1, j), weight=0)
            if((cells[i][j-1]=='Q' and cells[i][j]=='V') or (cells[i][j-1]=='V' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=1)
            if((cells[i][j-1]=='Q' and cells[i][j]=='P') or (cells[i][j-1]=='P' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=1.5)
            if((cells[i][j-1]=='Q' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='Q')):
                G.add_edge((i,j), (i+1, j), weight=0.5)


            if(cells[i][j-1]=='V' and cells[i][j]=='V'):
                G.add_edge((i,j), (i+1, j), weight=2)
            if((cells[i][j-1]=='V' and cells[i][j]=='P') or (cells[i][j-1]=='P' and cells[i][j]=='V')):
                G.add_edge((i,j), (i+1, j), weight=2.5)
            if((cells[i][j-1]=='V' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='V')):
                G.add_edge((i,j), (i+1, j), weight=1)

            if((cells[i][j-1]=='P' and cells[i][j]=='N') or (cells[i][j-1]=='N' and cells[i][j]=='P')):
                G.add_edge((i,j), (i+1, j), weight=2)

            
            if((cells[i][j-1]=='N' and cells[i][j]=='N')):
                G.add_edge((i,j),(i+1,j), weight=1)  


#vertically
for i in range(rows):
    for j in range(columns):
        if i == 0:
            if(cells[i][j]=='Q'):
                G.add_edge((i,j), (i, j+1), weight=0)
            if(cells[i][j]=='V'):
                G.add_edge((i,j), (i, j+1), weight=2)           
            if(cells[i][j]=='P'):
                G.add_edge((i,j), (i, j+1), weight=3)
            if(cells[i][j]=='N'):
                G.add_edge((i,j), (i, j+1), weight=1)          
       
        elif i == (rows-1):
            if(cells[i][j]=='Q'):
                G.add_edge((i+1,j), (i+1, j+1), weight=0)
            if(cells[i][j]=='V'):
                G.add_edge((i+1,j), (i+1, j+1), weight=2)           
            if(cells[i][j]=='P'):
                G.add_edge((i+1,j), (i+1, j+1), weight=3)
            if(cells[i][j]=='N'):
                G.add_edge((i+1,j), (i+1, j+1), weight=1) 

            if(cells[i][j]=='Q' and cells[i-1][j]=='Q'):
                G.add_edge((i,j),(i,j+1), weight=0)
            if((cells[i][j]=='Q' and cells[i-1][j]=='V') or (cells[i][j]=='V' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=1)
            if((cells[i][j]=='Q' and cells[i-1][j]=='P') or (cells[i][j]=='P' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=1.5)
            if((cells[i][j]=='Q' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=0.5)     

            if((cells[i][j]=='V' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=2)            
            if((cells[i][j]=='V' and cells[i-1][j]=='P') or (cells[i][j]=='P' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=2.5)     
            if((cells[i][j]=='V' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=1.5)   

            if((cells[i][j]=='P' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='P')):
                G.add_edge((i,j),(i,j+1), weight=2)  

            if(cells[i][j]=='N' and cells[i-1][j]=='N'):
                G.add_edge((i,j),(i,j+1), weight=1) 
        else:
            if(cells[i][j]=='Q' and cells[i-1][j]=='Q'):
                G.add_edge((i,j),(i,j+1), weight=0)
            if((cells[i][j]=='Q' and cells[i-1][j]=='V') or (cells[i][j]=='V' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=1)
            if((cells[i][j]=='Q' and cells[i-1][j]=='P') or (cells[i][j]=='P' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=1.5)
            if((cells[i][j]=='Q' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='Q')):
                G.add_edge((i,j),(i,j+1), weight=0.5)     

            if((cells[i][j]=='V' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=2)            
            if((cells[i][j]=='V' and cells[i-1][j]=='P') or (cells[i][j]=='P' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=2.5)     
            if((cells[i][j]=='V' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='V')):
                G.add_edge((i,j),(i,j+1), weight=1.5)   
            if((cells[i][j]=='P' and cells[i-1][j]=='N') or (cells[i][j]=='N' and cells[i-1][j]=='P')):
                G.add_edge((i,j),(i,j+1), weight=2)      
            if(cells[i][j]=='N' and cells[i-1][j]=='N'):
                G.add_edge((i,j),(i,j+1), weight=1) 
#-----------------------------------------------------------------------------------------------------#
#------------------------------ADDING EDGES FOR THE GRAPH MATPLOTLIB GUI------------------------------#
#-----------------------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------------------#
#------------------------------CLEANING UP GRAPH DICTIONARY-------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
myGraphDict = nx.to_dict_of_dicts(G, G.nodes)
quarantineCoordinatesBoolDict= nx.get_node_attributes(G, 'isQuarantine')

#only keep nodes that have an edge
for elem in list(myGraphDict):
    if type(elem)==str:
        myGraphDict.pop(elem)

#get a list of all the possible 
quarantineCoordinatesList = []
for k,v in quarantineCoordinatesBoolDict.items():
    if v==True:
        quarantineCoordinatesList.append(k)


#-----------------------------------------------------------------------------------------------------#
#------------------------------CLEANING UP GRAPH DICTIONARY-------------------------------------------#
#-----------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------#
#----------------------Get the closest quarantine place-----------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
def closestQuarantinePlace(startingCoordinates, quarantineCoordinates):
    a = np.array(startingCoordinates)
    currentMinimumCoordinate = quarantineCoordinates[0]
    currentMinimumCoordinateNumpy = np.array(quarantineCoordinates[0])
    currentMinimumDistance = np.linalg.norm(a-currentMinimumCoordinateNumpy)

    for elem in quarantineCoordinates:
        elemCoordinateNumpy = np.array(elem)
        distance = np.linalg.norm(a-elemCoordinateNumpy)
        if distance < currentMinimumDistance:
            currentMinimumDistance = distance
            currentMinimumCoordinate = elem
        
    return currentMinimumCoordinate

#check the closest quarantine place
closestQuarantinePlaceCoordinate = closestQuarantinePlace(startingCoordinates,quarantineCoordinatesList) 

#-----------------------------------------------------------------------------------------------------#
#----------------------Get the closest quarantine place-----------------------------------------------#
#-----------------------------------------------------------------------------------------------------#





#-----------------------------------------------------------------------------------------------------#
#------------------------------COMPUTING THE ASTAR ALGORITHM------------------------------------------#
#-----------------------------------------------------------------------------------------------------#

AStar = AStarAlgorithm(myGraphDict,startingCoordinates, closestQuarantinePlaceCoordinate)

#the AStar algorithm (for implementation, see AStarAlgorithm.py)
solutionPath = AStar.compute()

#if no path found
if solutionPath == None:
    print("No path is found. Please try again!")
    #exit()

#our solution path
values = []
for elem in solutionPath:
    values.append(elem[3])

#edges that took to get to the solution
newValues = []
for i in range(len(values)-1):
    newValues.append((values[i], values[i+1]))



#-----------------------------------------------------------------------------------------------------#
#--------------SOME DISPLAY ADJUSTMENTS TO MAKE GUI LOOK NICE-----------------------------------------#
#-----------------------------------------------------------------------------------------------------#

for e in G.edges():
    G[e[0]][e[1]]['color'] = 'grey'
    G[e[0]][e[1]]['width'] = 2
for e in G.edges():
    if e in newValues:
        G[e[0]][e[1]]['color'] = 'green'
        G[e[0]][e[1]]['width'] = 8

colorsIndex = {}


for index, value in enumerate(list(G.nodes())):
    if value==startingCoordinates:
        colorsIndex[index] =startingCoordinates
    elif value==closestQuarantinePlaceCoordinate:
        colorsIndex[index] = closestQuarantinePlaceCoordinate

colors = ['pink']*len(G.nodes())

for i in range(len(G.nodes)):
    if i in colorsIndex:
        if colorsIndex[i] ==startingCoordinates:
            colors[i] = '#34ebe5'
        if colorsIndex[i] ==closestQuarantinePlaceCoordinate:
            colors[i] = '#ff7300'
    else:
        colors[i] = 'pink'



edge_color_list = [G[e[0]][e[1]]['color'] for e in G.edges() ]
edge_width = [G[u][v]['width'] for u,v in G.edges()]


values.reverse()

#DISPLAY PATH IN CONSOLE
print('According the A* Algorithm, your best path to the quarantine destination is:')
for elem in values:
    print(str(elem))

#DISPLAY PATH IN GUI
nx.draw(G, nx.get_node_attributes(G,'pos'),edge_color=edge_color_list, width=edge_width,linewidths=1,\
node_size=1000,node_color=colors,alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G, nx.get_node_attributes(G, 'pos'), edge_labels = nx.get_edge_attributes(G, 'weight'))
plt.show()

#-----------------------------------------------------------------------------------------------------#
#--------------SOME DISPLAY ADJUSTMENTS TO MAKE GUI LOOK NICE-----------------------------------------#
#-----------------------------------------------------------------------------------------------------#


