import requests
import json
#config
apiUrl = 'http://112.137.129.202:8004/'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiZmVlbGhhcHB5IiwiaWF0IjoxNjA2MTE0MDE4LCJleHAiOjE2MDYyMDA0MTh9._r2Li99Ty6iqPfOc4ycq4KDaytNwLi7C9wjIgb6yv4A'
def creatRequest(url, type, data=None):
    url, result = apiUrl+url, ''
    if type == 'get':
        result = requests.get(url, headers={'Authorization':token})
    elif type == 'post':
        result = requests.post(url, headers={'Authorization':token, 'Content-Type': 'application/json'}, data=json.dumps(data))
    return result.json()
class Procon:
    def __init__(self):
        self.data = creatRequest('matches', 'get')
        print(self.data)
        try:
            self.data = self.data[0]
            self.teamId, self.turn = self.data['teamID'], self.data['id']
            self.match = creatRequest('matches/'+str(self.turn), 'get')
            print(self.match)
            self.actions = []
        except:
            print('Loi ket noi, kiem tra lai token ...')
    def getHeight(self):
        return self.match['height']
    def getMap(self):
        return self.match['points']
    def getTiled(self):
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

def isValid(x, y, h):
    return x>0 and y>0 and x<=h and y<=h

def findPath(x, y, points, tiled, teamID, h):
    delta = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    path, visited, cost, score = [[[-5, -5] for i in range(h)] for j in range(h)], [[0 for i in range(h)] for j in range(h)], [[0 for i in range(h)] for j in range(h)], [[-10000 for i in range(h)] for j in range(h)]
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
            score[yM][xM] = score[y][x]+points[yM][xM]
            cost[yM][xM] = cost[y][x]+1
            S.append([xM, yM])
            if path[y][x] == [-5, -5]:
                path[yM][xM] = [xM, yM]
            else:
                path[yM][xM] = path[y][x]

    return result
game = Procon()
for i in game.getMyAgents():
    nextMove = findPath(i['x'], i['y'], game.getMap(), game.getTiled(), game.getTeamId(), game.getHeight())
    type = 'move'
    if game.getTiled()[nextMove[1]][nextMove[0]] not in [0, game.getTeamId()]:
        type = 'remove'
    game.addActions(i['agentID'], nextMove[0]-i['x'], nextMove[1]-i['y'], type)
game.move()