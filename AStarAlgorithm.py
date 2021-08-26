import numpy as np



class AStarAlgorithm:
    def __init__(self, graphDict, startCoords, goalCoords):
        self.graphDict = graphDict
        self.startCoords = startCoords
        self.goalCoords = goalCoords

#-----------------------------------------------------------------------------------------------------#
#------------------------------------------HELPER FUNCTIONS-------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
    def __elementAlreadyInOpen(self,element, openList):
        for elem in openList:
            if elem[3]==element:
                return True
        return False


    def __getOldKValue(self,element, openList):
        for elem in openList:
            if elem[3]==element:
                return elem[1]
        return None


    def __removeOldK(self,element, openList):
        for elem in openList:
            if elem[3]==element:
                openList.remove(elem)
        return openList


#-----------------------------------------------------------------------------------------------------#
#------------------------------------------HEURISTIC FUNCTION-----------------------------------------#
#-----------------------------------------------------------------------------------------------------#

    def __getHeuristicValue(self, startCoord, endCoord):
        x1 = startCoord[0]
        y1 = startCoord[1]
        x2 = endCoord[0]
        y2 = endCoord[1]
        return abs(x1-x2)+abs(y1-y2)
    #note: this heuristic is admissible and is hence suited for A* algorithm   

#-----------------------------------------------------------------------------------------------------#
#------------------------------------------A* ALGORITHM-----------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
    def compute(self):

        open = []
        closed = []
        fValuesDict = {}
        gValuesDict = {}
        hValuesDict = {}

        hInitial = self.__getHeuristicValue(self.startCoords, self.goalCoords)
        gInitial = 0
        fInitial = hInitial + gInitial
        previousNode = None
        fValuesDict[self.startCoords] = fInitial
        gValuesDict[self.startCoords] = gInitial
        hValuesDict[self.startCoords] = hInitial

        open.append((fInitial, gInitial, hInitial, self.startCoords, previousNode))

        while len(open) >0:
            open.sort(key=lambda x:x[0])
            current = open.pop(0)
            if current[3] == self.goalCoords:
                path = []
                temp = current
                path.append(temp)
                while(temp[4] != None):
                    path.append(temp[4])
                    temp = temp[4]
                return path

            else:
                closed.append(current[3])

                #generate children
                childrensDictionary = self.graphDict[current[3]] 
                for k,v in childrensDictionary.items():
                    if k not in closed:

                        if self.__elementAlreadyInOpen(k, open):
                            newGValue = v['weight'] + current[1]
                            oldGValue = self.__getOldKValue(k, open)

                            if newGValue < oldGValue:
                                gValue = newGValue
                                hValue = self.__getHeuristicValue(k,self.goalCoords)
                                fValue = gValue + hValue
                                previousNode = current
                                open = self.__removeOldK(k,open)
                                print(str(k) + str(hValue))
                                open.append((fValue, gValue, hValue, k, previousNode))
                        
                        else:
                            gValue = v['weight'] + current[1]
                            hValue = self.__getHeuristicValue(k,self.goalCoords)
                            fValue = gValue + hValue
                            previousNode = current
                            print(str(k) + str(hValue))
                            open.append((fValue, gValue, hValue, k, previousNode))
        return None


