#global variables
vertexList = []
numVerticies = 0

#get the number of verticies in the network
validNumVerticies = False
while not validNumVerticies:
    numVerticies = input("Enter the number of verticies in the network:  ")
    try:
        numVerticies = int(numVerticies)
    except:
        print("\nThe number of verticies must be a positive integer.")
    else:
        if numVerticies <3:
            print("\nThere must be more than 3 verticies in the network.\n")
        else:
            validNumVerticies = True

#fill vertexList with letters (starting from A) for each vertex in the network
for num in range(numVerticies):
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

    connectedVerticies = []
    connectedVerticies.append(connections[0][0])
    connectedVerticies.append(connections[0][1])
    del connections[0]

    for connection in connections:
        if (connection[0] in connectedVerticies) and (connection[1] not in connectedVerticies):
            connectedVerticies.append(connection[1])
        elif (connection [1] in connectedVerticies) and (connection[0] not in connectedVerticies):
            connectedVerticies.append(connection[0])

    connected = True
    for vertex in vertexList:
        if vertex not in connectedVerticies:
            print ("\nVertex " + vertex + " is not connected")
            connected = False

    if not connected:
        return False

    return True

#find the minimum arc (to be the starting arc)
def findMinLen(connections):
    minArcLen = 100**100
    minArcVerticies = []
    minArcIndex = 0
    verticiesInRoute = []
    arcsInRoute = []
    index = 0

    for connection in connections:
        if connection[2] < minArcLen:
            minArcLen = connection[2]
            minArcVerticies = [connection[0], connection[1]]
            minArcIndex = index
        index += 1

    verticiesInRoute.append(minArcVerticies[0])
    verticiesInRoute.append(minArcVerticies[1])

    minArc = minArcVerticies[0] + minArcVerticies[1]
    arcsInRoute.append(minArc)

    del connections[minArcIndex]

    return (minArcLen, verticiesInRoute, arcsInRoute, connections)

#find the minimum spanning tree
def findRoute (totalLength, verticiesInRoute, arcsInRoute, remainingConnections):
    while len(verticiesInRoute) < numVerticies:
        tempMinArcLen = 100**100
        tempMinArcVerticies = []
        tempMinArc = ""
        tempIndex = 0
        
        for vertexInRoute in verticiesInRoute:
            for connection in remainingConnections:
                if ((vertexInRoute == connection[0]) and (connection[1] not in verticiesInRoute)) or ((vertexInRoute == connection[1]) and (connection[0] not in verticiesInRoute)):
                    if connection[2] < tempMinArcLen:
                        tempMinArcLen = connection[2]
                        tempMinArcVerticies = [connection[0],connection[1]]
                        tempMinArcIndex = tempIndex
            tempIndex += 1

        totalLength += tempMinArcLen
        if tempMinArcVerticies[0] in verticiesInRoute:
            verticiesInRoute.append(tempMinArcVerticies[1])
        else:
            verticiesInRoute.append(tempMinArcVerticies[0])
        del remainingConnections[tempMinArcIndex]
        tempMinArc = tempMinArcVerticies[0] + tempMinArcVerticies[1]
        arcsInRoute.append(tempMinArc)

    return (totalLength, arcsInRoute)

#main program
connections = getConnections(vertexList)
minArcLen, verticiesInRoute, arcsInRoute, remainingConnections = findMinLen(connections)
totalLength, arcsInRoute = findRoute(minArcLen, verticiesInRoute, arcsInRoute, remainingConnections)

print("\nThe minimum spanning tree contains the following arcs:")
for arc in arcsInRoute:
    print(arc)
print("\nTotal Length of Minimum Spanning Tree:", totalLength) 
