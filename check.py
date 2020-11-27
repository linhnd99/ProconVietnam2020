import requests
import json
from time import time, sleep

#config
apiUrl = 'http://112.137.129.202:8004/'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiYXNzeXJpYW4iLCJpYXQiOjE2MDY0NzAwMzMsImV4cCI6MTYwNjU1NjQzM30.1Sz-K7fv6iXePwer4EyCwWDtCGFMuhlEcubyhG3gSEs'

# define
INF = 1000000000
delta = [[-1,-1], [-1,1], [1,-1], [1,1], [0,-1], [0,1], [-1,0], [1,0]]
maxScore = -INF 
myPos = []

def creatRequest(url, type, data=None):
    url, result = apiUrl+url, ''
    if type == 'get':
        result = requests.get(url, headers={'Authorization':token})
    elif type == 'post':
        result = requests.post(url, headers={'Authorization':token, 'Content-Type': 'application/json'}, data=json.dumps(data))
    print(result)
    return result.json()
class Procon:
    def __init__(self):
        self.data = creatRequest('matches', 'get')
        print(self.data)
        try:
            self.data = self.data[0]
            self.teamId, self.turn = self.data['teamID'], self.data['id']
            self.match = creatRequest('matches/'+str(self.turn), 'get')
            # print(self.match)
            self.actions = []
        except:
            print('Loi ket noi, kiem tra lai token ...')
    def getHeight(self):
        return int(self.match['height'])
    def getMap(self):
        return self.match['points']
    def getTiled(self):
        for one in myPos:
            self.match['tiled'][one[1]-1][one[0]-1] = self.getTeamId()
        return self.match['tiled']
    def getMyAgents(self):
        for team in self.match['teams']:
            if team['teamID'] == self.teamId:
                return team['agents']
    def  getTeamId(self):
        return self.teamId
    def addActions(self, agentId, x, y, type):
        self.actions.append({"agentID": agentId, "dx": x, "dy": y, "type": type})
    def move(self):
        cmd = {'actions': self.actions}
        creatRequest('matches/' + str(self.turn) + '/action', 'post', cmd)
    def getObstacles(self):
        return self.match['obstacles']
    def getTurn(self): 
        return self.match['turn']
    def getPointTreasure(self,x,y):
        for one in self.match['treasure']:
            if one['x'] == x and one['y'] == y:
                return one['point']
        return 0
    
def isValid(x, y, h):
    return x>0 and y>0 and x<=h and y<=h

def findPath(x, y, points, tiled, teamID, h, obstacles):
    h = int(h)
    delta = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    path = [[[-5, -5] for i in range(h)] for j in range(h)]
    visited = [[0 for i in range(h)] for j in range(h)]
    cost = [[0 for i in range(h)] for j in range(h)]
    score =  [[-10000 for i in range(h)] for j in range(h)]
    result, minCost, totalScore = [], 100000, 0
    S = [[x, y]]
    visited[y][x], cost[y][x], score[y][x] = 1, 0, 0
    origin = [x, y]
    while len(S)>0:
        dau = S.pop(0)
        x, y = dau[0], dau[1]
        if tiled[y][x] != teamID and points[y][x]>0 and origin != [x, y]:
            if (cost[y][x]<minCost) or (cost[y][x]==minCost and score[y][x]>totalScore):
                result = path[y][x]
                minCost = cost[y][x]
                totalScore = score[y][x]
                continue
        for i in delta:
            xM, yM = x+i[0], y+i[1]

            if not isValid(xM, yM, h):
                continue
            if visited[yM][xM] == 1:
                continue
            else:
                visited[y][x] = 1
            if score[y][x]+points[yM][xM] < score[yM][xM]:
                continue
            if tiled[yM][xM] == teamID:
                continue
            if {'x': xM, 'y' : yM} in obstacles:
                continue
            score[yM][xM] = score[y][x]+points[yM][xM]
            cost[yM][xM] = cost[y][x]+1
            S.append([xM, yM])
            if path[y][x] == [-5, -5]:
                path[yM][xM] = [xM, yM]
            else:
                path[yM][xM] = path[y][x]
    return result

# -------- Linh ----------
def findMaxPath(step, x, y, points, tiled, teamID, h, obstacles, score):
    global maxScore
    global nextStep
    if isValid(x,y,h) == False: 
        return
    
    score += points[y-1][x-1] + game.getPointTreasure(y,x)
    if step >= 5:
        if maxScore<score: 
            maxScore=score
            nextStep = path[0]
        else:
            nextStep=nextStep
    else:
        isVisited[x][y] = True
        for next in delta:
            if isValid(x+next[0], y+next[1], h) == False:
                continue
            if {'x':x+next[0],'y':y+next[1]} in obstacles:
                continue
            if isVisited[x+next[0]][y+next[1]] == True or tiled[y+next[1]-1][x+next[0]-1] == teamID:
                continue
            path.append([next[0],next[1]])
            if tiled[y+next[1]-1][x+next[0]-1] != 0 and tiled[y+next[1]-1][x+next[0]-1] != teamID: 
                findMaxPath(step+2, x+next[0], y+next[1], points, tiled, teamID, h, obstacles, score)    
            else:
                findMaxPath(step+1, x+next[0], y+next[1], points, tiled, teamID, h, obstacles, score)
            path.pop()
        isVisited[x][y] = False

def findPath2(x, y, points, tiled, teamID, h, obstacles):
    global maxScore
    global nextStep
    global isVisited
    global path
    maxScore = -INF 
    nextStep=[0, 0]
    isVisited = [[False for i in range(h+1)] for j in range(h+1)]
    path = []
    findMaxPath(1, x, y, points, tiled, teamID, h, obstacles, 0)
    return [x+nextStep[0],y+nextStep[1]]

while True:
    game = Procon()
    myPos = []
    if game is None:
        continue
    print('chạy turn: ' , game.getTurn())
    for i in game.getMyAgents():
        nextMove = findPath2(i['x'], i['y'], game.getMap(), game.getTiled(), game.getTeamId(), game.getHeight(), game.getObstacles())
        type = 'move'
        if game.getTiled()[nextMove[1]-1][nextMove[0]-1] != 0 and game.getTiled()[nextMove[1]-1][nextMove[0]-1] != game.getTeamId():
            type = 'remove'
        print('agent ',i,' ',type,' ',nextMove)
        game.addActions(i['agentID'], nextMove[0]-i['x'], nextMove[1]-i['y'], type)
        myPos.append(nextMove)
    game.move()
    print("Đã chạy")
    sleep(5)
    
