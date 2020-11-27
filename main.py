import requests 
import json
from Model import *
from RequestToServer import *

MyAgent=[]
HisAgent=[]
SizeMap = 0

def BuildMap(data):
    SizeMap = match['height']
    # Map = [[Point() for i in range(SizeMap+1)] for j in range(SizeMap+1)]
    Map = [[Point()*(SizeMap+1)]*(SizeMap+1)]
    for i in range(1,SizeMap+1):
        for j in range(1,SizeMap+1):
            Map[i][j].point = data['points'][i][j]
    for obj in data['treasure']:
        if obj['status'] == 0:
            Map[obj['x']][obj['y']].point = Map[obj['x']][obj['y']].point + point
    for obj in data['obstacles']:
        Map[obj['x']][obj['y']].isBrick = True
    for i in range(1,SizeMap+1):
        for j in range(1,SizeMap+1):
            Map[i][j].visited = data['tiled'][i][j]







if __name__ == "__main__":
    requestToServer = RequestToServer()
    listMatches = requestToServer.getMatches()
    
    if isinstance(listMatches,int):
        exit()
    
    if listMatches.count == 0:
        print ('No match')
        exit()

    matchInfo = MatchInfo(listMatches[0])
    match = requestToServer.getDataMatch(matchInfo.id)
    
    BuildMap(match)

    for obj in match['teams']:
        if obj['teamID'] == match.teamID:
            for ob in obj['agents']:
                MyAgent.append(XY(ob))

    print(Map)