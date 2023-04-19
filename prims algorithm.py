#global variables
vertexList = []
numVertices = 0

#get the number of vertices in the network
validNumVertices = False
while not validNumVertices:
    numVertices = input("Enter the number of vertices in the network:  ")
    try:
        numVertices = int(numVertices)
    except:
        print("\nThe number of vertices must be a positive integer.")
    else:
        if numVertices <3:
            print("\nThere must be more than 3 vertices in the network.\n")
        else:
            validNumVertics = True

#fill vertexList with letters (starting from A) for each vertex in the network
for num in range(numVertices):
    vertexList.append(chr(65 + num))

#get the arcs in the network
def getConnections(firstVertexList):
    connections = []
    secondVertexList = firstVertexList[:]
    for firstVertex in firstVertexList:
        del secondVertexList[0]
        for secondVertex in secondVertexList:
            if firstVertex != secondVertex:
                validInput = False
                while not validInput:
                    connection = input("\nEnter the length of the connection between " + firstVertex + " and " + secondVertex + ".\nEnter 0 if there is no connection between the two verticies.  ")
                    try:
                        connection = float(connection)
                    except:
                        print("\nYou must enter a postive number.")
                    else:
                        if connection > 100*100:
                            print("Sorry, that length is too large")
                        else:
                            validInput = True
                            if connection != 0:
                                connections.append([firstVertex,secondVertex,connection])

    if validConnections(connections):
        return (connections)
    else:
        print("\nYou must re-enter the connections.")
        return getConnections(firstVertexList)

#check if the connections are valid
def validConnections(originalConnections):
    connections = originalConnections[:]
    if len(connections) == 0:
        print("\nThere cannot be 0 connections")
        return False

    connectedVertices = []
    connectedVertices.append(connections[0][0])
    connectedVertices.append(connections[0][1])
    del connections[0]

    for connection in connections:
        if (connection[0] in connectedVertices) and (connection[1] not in connectedVertices):
            connectedVertices.append(connection[1])
        elif (connection [1] in connectedVertices) and (connection[0] not in connectedVertices):
            connectedVertices.append(connection[0])

    connected = True
    for vertex in vertexList:
        if vertex not in connectedVertices:
            print ("\nVertex " + vertex + " is not connected")
            connected = False

    if not connected:
        return False

    return True

#find the minimum arc (to be the starting arc)
def findMinLen(connections):
    minArcLen = 100**100
    minArcVertices = []
    minArcIndex = 0
    verticesInRoute = []
    arcsInRoute = []
    index = 0

    for connection in connections:
        if connection[2] < minArcLen:
            minArcLen = connection[2]
            minArcVertices = [connection[0], connection[1]]
            minArcIndex = index
        index += 1

    verticesInRoute.append(minArcVertices[0])
    verticesInRoute.append(minArcVertices[1])

    minArc = minArcVertices[0] + minArcVertices[1]
    arcsInRoute.append(minArc)

    del connections[minArcIndex]

    return (minArcLen, verticesInRoute, arcsInRoute, connections)

#find the minimum spanning tree
def findRoute (totalLength, verticesInRoute, arcsInRoute, remainingConnections):
    while len(verticesInRoute) < numVertices:
        tempMinArcLen = 100**100
        tempMinArcVertices = []
        tempMinArc = ""
        tempIndex = 0
        
        for vertexInRoute in verticesInRoute:
            for connection in remainingConnections:
                if ((vertexInRoute == connection[0]) and (connection[1] not in verticesInRoute)) or ((vertexInRoute == connection[1]) and (connection[0] not in verticesInRoute)):
                    if connection[2] < tempMinArcLen:
                        tempMinArcLen = connection[2]
                        tempMinArcVertices = [connection[0],connection[1]]
                        tempMinArcIndex = tempIndex
            tempIndex += 1

        totalLength += tempMinArcLen
        if tempMinArcVertices[0] in verticiesInRoute:
            verticesInRoute.append(tempMinArcVertices[1])
        else:
            verticesInRoute.append(tempMinArcVertices[0])
        del remainingConnections[tempMinArcIndex]
        tempMinArc = tempMinArcVertices[0] + tempMinArcVertices[1]
        arcsInRoute.append(tempMinArc)

    return (totalLength, arcsInRoute)

#main program
connections = getConnections(vertexList)
minArcLen, verticesInRoute, arcsInRoute, remainingConnections = findMinLen(connections)
totalLength, arcsInRoute = findRoute(minArcLen, verticesInRoute, arcsInRoute, remainingConnections)

print("\nThe minimum spanning tree contains the following arcs:")
for arc in arcsInRoute:
    print(arc)
print("\nTotal Length of Minimum Spanning Tree:", totalLength) 
input ("\nPress Enter to Exit")
