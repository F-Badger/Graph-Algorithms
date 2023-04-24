#global variables
vertexList = []
numVertices = 0

#get the number of vertices in the network
validNumVertices = False
while not validNumVertices:
    numVertices = input("Enter the number of vertices in the network:  ")
    try:
        numVertices = int(numVertices)    #check if the input is an integer
    except:
        print("\nThe number of vertices must be a positive integer.")
    else:
        if numVertices <3:       #check that the input is atleast 3 - if there is 1 vertex, there are no connections, and if there are only 2 vertices, the MST will just be the connection between the vertices
            print("\nThere must be more than 3 vertices in the network.\n")
        else:
            validNumVertices = True

#fill vertexList with letters (starting from A) for each vertex in the network
for num in range(numVertices):
    vertexList.append(chr(65 + num))    #65 is unicode representation of A

#get the arcs in the network
def getConnections(firstVertexList):
    
    connections = []
    secondVertexList = firstVertexList[:]  #make a copy of the vertex list
    
    for firstVertex in firstVertexList:
        
        del secondVertexList[0]   #remove the first element of the second vertex list so that duplicate pairings are avoided (e.g avoid asking for A and B, and then B and A)
        
        for secondVertex in secondVertexList:
            
            if firstVertex != secondVertex:     #don't ask for distance between a vertex and itself
                
                validInput = False 
                while not validInput:
                    connection = input("\nEnter the length of the connection between " + firstVertex + " and " + secondVertex + ".\nEnter 0 if there is no connection between the two vertices.  ")
                    try:
                        connection = float(connection)   #check if input is a number
                    except:
                        print("\nYou must enter a postive number.")
                    else:
                        if connection > 100*100:
                            print("Sorry, that length is too large")
                        else:
                            validInput = True
                            if connection != 0:     #only add the arc to the array if there is a connection
                                connections.append([firstVertex,secondVertex,connection])

    if validConnections(connections):
        return (connections)   #return array of connections if all connections are valid
    else:
        print("\nYou must re-enter the connections.")
        return getConnections(firstVertexList)    #re-get the array of connections if the connections are not valid

#check if the connections are valid
    
def validConnections(originalConnections):
     
    connections = originalConnections[:]  #make a copy of the array of connectionss
    
    if len(connections) == 0:     #check if there are no connections
        print("\nThere cannot be 0 connections")
        return False
    
    connectedVertices = []  #initialise array for list of vertices that are connected in the network

    #add the vertices of the first arc to the list of connected vertices
    connectedVertices.append(connections[0][0])
    connectedVertices.append(connections[0][1])

    del connections[0] #remove the first arc from the connections array since it has already been dealt with

    for connection in connections:
        
        if (connection[0] in connectedVertices) and (connection[1] not in connectedVertices):    #if the first vertex in the arc is already connected and the second is not
            connectedVertices.append(connection[1])        #add the second vertex of the arc to the list of connected vertices
            
        elif (connection [1] in connectedVertices) and (connection[0] not in connectedVertices):  #if the second vertex in the arc is already connected and the first is not
            connectedVertices.append(connection[0])        #add the first vertex of the arc to the list of connected vertices

    connected = True   #assume the network is connected before checking to see if this is false
    
    for vertex in vertexList:
        if vertex not in connectedVertices:    #if a vertex in the network is not in the list of connected vertices
            print ("\nVertex " + vertex + " is not connected")    #tell user what vertex is not connected
            connected = False    #network is not connected

    if not connected:    #if the network is not connected
        return False

    return True   #the connections are valid if it passed checks for no connections and for all vertices being connected

#find the minimum arc (to be the starting arc)

def findMinLen(connections):

    minArcLen = 100**100
    minArcVertices = []
    minArcIndex = 0
    verticesInRoute = []
    arcsInRoute = []
    index = 0

    for connection in connections:
        
        if connection[2] < minArcLen:     #if the length of the arc is lower than the previous minimum

            #update the minimum arc information 
            minArcLen = connection[2]
            minArcVertices = [connection[0], connection[1]]
            minArcIndex = index

        index += 1

    #add the vertecies of the minimum arc to the list of vertices in the network
    verticesInRoute.append(minArcVertices[0])   
    verticesInRoute.append(minArcVertices[1])

    minArc = minArcVertices[0] + minArcVertices[1]   #create a string of the minimum arc
    
    arcsInRoute.append(minArc) #add the minimium arc to the list of arcs in the network

    del connections[minArcIndex]    #remove the minimum arc from the working list of arcs

    return (minArcLen, verticesInRoute, arcsInRoute, connections)    #return the length of the minimum arc, the list of vertices in the route, the list of arcs in the reoute, and the working list of connections

#find the minimum spanning tree
def findRoute (totalLength, verticesInRoute, arcsInRoute, remainingConnections):
    
    while len(verticesInRoute) < numVertices:  #reset the temporary variables for each iterations until every vertex is in the minimum spanning tree
        tempMinArcLen = 100**100
        tempMinArcVertices = []
        tempMinArc = ""
        tempIndex = 0
        
        for vertexInRoute in verticesInRoute:
            
            for connection in remainingConnections:
                
                if ((vertexInRoute == connection[0]) and (connection[1] not in verticesInRoute)) or ((vertexInRoute == connection[1]) and (connection[0] not in verticesInRoute)):    #if one vertex of the arc is in the MST already and the other is not
        
                    if connection[2] < tempMinArcLen:   #if the length of the connection is less than the current smallest

                        #update the minimum arc information
                        tempMinArcLen = connection[2]
                        tempMinArcVertices = [connection[0],connection[1]]
                        tempMinArcIndex = tempIndex
                        
            tempIndex += 1

        totalLength += tempMinArcLen   #add the weight of the new arc to the total weight of the MST
        
        if tempMinArcVertices[0] in verticesInRoute:        #if it is the first vertex of the arc that is already in the MST
            verticesInRoute.append(tempMinArcVertices[1])   #add the second vertex of the arc to the list of vertices in the MST
            
        else:       #if it is not the first vertex of the arc which is already in the MST, it must be the second vertex of the arc
            verticesInRoute.append(tempMinArcVertices[0])   #add the first vertex of the arc to the list of vertices in the MST
            
        del remainingConnections[tempMinArcIndex]  #remove the arc which was just added to the MST from the working list of connections
        
        tempMinArc = tempMinArcVertices[0] + tempMinArcVertices[1]    #create a string of the minimum arc
        
        arcsInRoute.append(tempMinArc)   #add the minimum arc to the list of arcs in the network

    return (totalLength, arcsInRoute)    #return the final weight of the MST and the arcs which are included in it

#main program
connections = getConnections(vertexList)
minArcLen, verticesInRoute, arcsInRoute, remainingConnections = findMinLen(connections)
totalLength, arcsInRoute = findRoute(minArcLen, verticesInRoute, arcsInRoute, remainingConnections)

print("\nThe minimum spanning tree contains the following arcs:")
for arc in arcsInRoute:
    print(arc)
print("\nTotal Length of Minimum Spanning Tree:", totalLength)
input ("Press Enter to exit")
