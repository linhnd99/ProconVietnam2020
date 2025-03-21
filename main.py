import requests
import json
from time import time, sleep

# config
apiUrl = 'http://112.137.129.202:8004/'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiYXNzeXJpYW4iLCJpYXQiOjE2MDc0MTgwNTAsImV4cCI6MTYwNzUwNDQ1MH0.rh6LCNo_1DIEiheW2m6AJutxUq2tPn9pYOTZsdJqpjo'

# define
INF = 1000000000
delta = [[-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1], [-1, 0], [1, 0]]
maxScore = -INF
myPos = []


def creatRequest(url, type, data=None):
    url, result = apiUrl + url, ''
    if type == 'get':
        result = requests.get(url, headers={'Authorization': token})
    elif type == 'post':
        result = requests.post(url, headers={
            'Authorization': token, 'Content-Type': 'application/json'}, data=json.dumps(data))
    print(result)
    return result.json()


class Procon:
    def __init__(self):
        self.data = creatRequest('matches', 'get')
        print(self.data)
        try:
            self.data = self.data[0]
            self.teamId, self.turn = self.data['teamID'], self.data['id']
            self.match = creatRequest('matches/' + str(self.turn), 'get')
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
            self.match['tiled'][one[1] - 1][one[0] - 1] = self.getTeamId()
        return self.match['tiled']

    def getMyAgents(self):
        for team in self.match['teams']:
            if team['teamID'] == self.teamId:
                return team['agents']

    def getTeamId(self):
        return self.teamId

    def addActions(self, agentId, x, y, type):
        self.actions.append(
            {"agentID": agentId, "dx": x, "dy": y, "type": type})

    def move(self):
        cmd = {'actions': self.actions}
        creatRequest('matches/' + str(self.turn) + '/action', 'post', cmd)

    def getObstacles(self):
        return self.match['obstacles']

    def getTurn(self):
        return self.match['turn']

    def getPointTreasure(self, x, y):
        for one in self.match['treasure']:
            if one['x'] == x and one['y'] == y:
                return one['point']
        return 0


def isValid(x, y, h):
    return x > 0 and y > 0 and x <= h and y <= h


def findPath(x, y, points, tiled, teamID, h, obstacles):
    h = int(h)
    delta = [[-1, -1], [0, -1], [1, -1],
             [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    path = [[[-5, -5] for i in range(h)] for j in range(h)]
    visited = [[0 for i in range(h)] for j in range(h)]
    cost = [[0 for i in range(h)] for j in range(h)]
    score = [[-10000 for i in range(h)] for j in range(h)]
    result, minCost, totalScore = [], 100000, 0
    S = [[x, y]]
    visited[y][x], cost[y][x], score[y][x] = 1, 0, 0
    origin = [x, y]
    while len(S) > 0:
        dau = S.pop(0)
        x, y = dau[0], dau[1]
        if tiled[y][x] != teamID and points[y][x] > 0 and origin != [x, y]:
            if (cost[y][x] < minCost) or (cost[y][x] == minCost and score[y][x] > totalScore):
                result = path[y][x]
                minCost = cost[y][x]
                totalScore = score[y][x]
                continue
        for i in delta:
            xM, yM = x + i[0], y + i[1]

            if not isValid(xM, yM, h):
                continue
            if visited[yM][xM] == 1:
                continue
            else:
                visited[y][x] = 1
            if score[y][x] + points[yM][xM] < score[yM][xM]:
                continue
            if tiled[yM][xM] == teamID:
                continue
            if {'x': xM, 'y': yM} in obstacles:
                continue
            score[yM][xM] = score[y][x] + points[yM][xM]
            cost[yM][xM] = cost[y][x] + 1
            S.append([xM, yM])
            if path[y][x] == [-5, -5]:
                path[yM][xM] = [xM, yM]
            else:
                path[yM][xM] = path[y][x]
    return result


# -------- Linh ----------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def findMaxPath(step, x, y, points, tiled, teamID, h, obstacles, score):
    global maxScore
    global nextStep
    if isValid(x, y, h) == False:
        return

    score += points[y - 1][x - 1] + game.getPointTreasure(y, x)
    if step >= 7:
        if maxScore < score:
            maxScore = score
            nextStep = path[0]
        else:
            nextStep = nextStep
    else:
        isVisited[x][y] = True
        for next in delta:
            if not isValid(x + next[0], y + next[1], h):
                continue
            if {'x': x + next[0], 'y': y + next[1]} in obstacles:
                continue
            # =))))))))))))
            if isVisited[x + next[0]][y + next[1]] or tiled[y + next[1] - 1][x + next[0] - 1] == teamID:
                continue
            path.append([next[0], next[1]])
            if tiled[y + next[1] - 1][x + next[0] - 1] != 0 and tiled[y + next[1] - 1][x + next[0] - 1] != teamID:
                findMaxPath(step + 2, x + next[0], y + next[1],
                            points, tiled, teamID, h, obstacles, score)
            else:
                findMaxPath(step + 1, x + next[0], y + next[1],
                            points, tiled, teamID, h, obstacles, score)
            path.pop()
        isVisited[x][y] = False


def findPath2(x, y, points, tiled, teamID, h, obstacles):
    global maxScore
    global nextStep
    global isVisited
    global path
    global game
    maxScore = -INF
    nextStep = [0, 0]
    isVisited = [[False for i in range(h + 1)] for j in range(h + 1)]
    path = []
    for i in range(1, h + 1):
        for j in range(1, h + 1):
            if game.getTiled()[i - 1][j - 1] == game.getTeamId:
                points[i - 1][j - 1] = 0
    findMaxPath(1, x, y, points, tiled, teamID, h, obstacles, 0)
    return [x + nextStep[0], y + nextStep[1]]


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# findPath2 + bao

def computeScore(tiled, isVisited):
    global game

    kt = [[False for i in range(0, game.getHeight() + 3)]
          for j in range(0, game.getHeight() + 3)]

    # compute point score
    res = 0
    for i in range(1, game.getHeight() + 1):
        for j in range(1, game.getHeight() + 1):
            if tiled[i-1][j-1] == game.getTeamId() or isVisited[i][j]:
            # if tiled[i - 1][j - 1] == game.getTeamId():
                # res = res + game.getMap()[i][j]
                kt[i][j] = True

    # compute convex
    # except area edge
    for i in range(1, game.getHeight()+1):
        for j in [1, game.getHeight()]:
            queue = []
            queue.append(i)
            queue.append(j)
            if kt[i][j]:
                queue = []
            kt[i][j] = True
            while len(queue) > 0:
                x = queue.pop(0)
                y = queue.pop(0)
                if not isValid(x, y, game.getHeight()):
                    continue
                if not kt[x + 1][y]:
                    queue.append(x + 1)
                    queue.append(y)
                    kt[x + 1][y] = True
                if not kt[x - 1][y]:
                    queue.append(x - 1)
                    queue.append(y)
                    kt[x - 1][y] = True
                if not kt[x][y + 1]:
                    queue.append(x)
                    queue.append(y + 1)
                    kt[x][y + 1] = True
                if not kt[x][y - 1]:
                    queue.append(x)
                    queue.append(y - 1)
                    kt[x][y - 1] = True

            queue = []
            queue.append(j)
            queue.append(i)
            if tiled[j-1][i-1] == game.getTeamId():
                queue = []
            else:
                kt[j][i] = True
            while len(queue) > 0:
                x = queue.pop(0)
                y = queue.pop(0)
                if not isValid(x, y, game.getHeight()):
                    continue
                if not kt[x + 1][y]:
                    queue.append(x + 1)
                    queue.append(y)
                    kt[x + 1][y] = True
                if not kt[x - 1][y]:
                    queue.append(x - 1)
                    queue.append(y)
                    kt[x - 1][y] = True
                if not kt[x][y + 1]:
                    queue.append(x)
                    queue.append(y + 1)
                    kt[x][y + 1] = True
                if not kt[x][y - 1]:
                    queue.append(x)
                    queue.append(y - 1)
                    kt[x][y - 1] = True

    # compute area score
    for i in range(1, game.getHeight()):
        for j in range(1, game.getHeight()):
            if not kt[i][j]:
                res = res + abs(game.getMap()[i-1][j-1])
    return res

def findMaxPath4(step, x, y, points, tiled, teamID, h, obstacles, score):
    global maxScore
    global nextStep
    global path

    if not isValid(x, y, h):
        return

    score += points[y - 1][x - 1] + game.getPointTreasure(y, x) + computeScore(tiled, isVisited)
    if step >= 7:
        if maxScore < score:
            maxScore = score
            nextStep = path[0]
        else:
            nextStep = nextStep
    else:
        isVisited[x][y] = True
        for next in delta:
            if not isValid(x + next[0], y + next[1], h):
                continue
            if {'x': x + next[0], 'y': y + next[1]} in obstacles:
                continue
            # =))))))))))))
            if isVisited[x + next[0]][y + next[1]] or tiled[y + next[1] - 1][x + next[0] - 1] == teamID:
                continue


            path.append([next[0], next[1]])
            if tiled[y + next[1] - 1][x + next[0] - 1] != 0 and tiled[y + next[1] - 1][x + next[0] - 1] != teamID:
                findMaxPath(step + 2, x + next[0], y + next[1],
                            points, tiled, teamID, h, obstacles, score)
            else:
                findMaxPath(step + 1, x + next[0], y + next[1],
                            points, tiled, teamID, h, obstacles, score)
            path.pop()
        isVisited[x][y] = False

def findMaxPath3(step, x, y, points, tiled, teamID, h, obstacles, score, path):
    global maxScore
    global nextStep
    global numberStep
    global game
    global isVisited
    global action

    if {'x':x, 'y':y} in action:
        return

    score = score + (0 if tiled[x-1][y-1] == teamID else points[x-1][y-1]) + computeScore(tiled,isVisited) if game.data['turns'] - game.getTurn() <= 10 else 0
    path.append([x,y, step])

    if step == 7:
        if score > maxScore:
            nextStep = [path[1][0] - path[0][0], path[1][1] - path[0][1]]
            maxScore = score
            numberStep = step
        elif score == maxScore:
            if numberStep > step:
                nextStep = [path[1][0] - path[0][0], path[1][1] - path[0][1]]
                numberStep = step
        return

    if isValid(x + 1, y, h):
        if not isVisited[x + 1][y]:
            isVisited[x+1][y] = True
            findMaxPath3(step + (1 if tiled[x][y-1] != teamID and tiled[x][y-1] != 0 else 2), x+1, y, points, tiled, teamID, h, obstacles, score, path)
            isVisited[x + 1][y] = False
    if isValid(x - 1, y, h):
        if not isVisited[x - 1][y]:
            isVisited[x - 1][y] = True
            findMaxPath3(step + (1 if tiled[x - 2][y - 1] != teamID and tiled[x - 2][y - 1] != 0 else 2), x - 1, y,
                         points, tiled, teamID, h, obstacles, score, path)
            isVisited[x - 1][y] = False
    if isValid(x, y + 1, h):
        if not isVisited[x][y + 1]:
            isVisited[x][y + 1] = True
            findMaxPath3(step + (1 if tiled[x - 1][y] != teamID and tiled[x - 1][y] != 0 else 2), x, y+1,
                         points, tiled, teamID, h, obstacles, score, path)
            isVisited[x][y + 1] = False
    if isValid(x, y - 1, h):
        if not isVisited[x][y - 1]:
            isVisited[x][y - 1] = True
            findMaxPath3(step + (1 if tiled[x - 1][y - 2] != teamID and tiled[x - 1][y - 2] != 0 else 2), x, y - 1,
                         points, tiled, teamID, h, obstacles, score, path)
            isVisited[x][y - 1] = False

def findPath3(x, y, points, tiled, teamID, h, obstacles):
    global nextStep
    global maxScore
    global numberStep
    global game
    global isVisited
    global action
    global path

    maxScore = -INF
    numberStep = 0
    nextStep = [0, 0]
    isVisited = [[False for i in range(h+1)] for j in range(h+1)]
    path=[]

    isVisited[x][y] = True
    findMaxPath4(1, x, y, points, tiled, teamID, h, obstacles, 0)
    return [x + nextStep[0], y + nextStep[1]]

while True:
    global game
    global action
    global nextStep

    game = Procon()
    myPos = []
    if game is None:
        continue
    print('chạy turn: ', game.getTurn())
    action = []
    maxScore = 0
    for i in game.getMyAgents():
        nextMove = findPath2(i['x'], i['y'], game.getMap(), game.getTiled(), game.getTeamId(), game.getHeight(), game.getObstacles())
        type = 'move'
        if game.getTiled()[nextMove[1] - 1][nextMove[0] - 1] != 0 and game.getTiled()[nextMove[1] - 1][
            nextMove[0] - 1] != game.getTeamId():
            type = 'remove'
        print('agent ', i, ' ', type, ' ', nextMove)
        game.addActions(i['agentID'], nextMove[0] - i['x'], nextMove[1] - i['y'], type)
        action.append({'x':nextMove[0], 'y':nextMove[1]})
        myPos.append(nextMove)

    game.move()

    print("Đã chạy")
    print("---------------------------------")
    print("sleeping", (int(game.data['turnMillis']) - 2000) // 1000, "s\n")
    sleep((int(game.data['turnMillis']) - 2000) // 1000)
