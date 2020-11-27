class MatchInfo:
    def __init__(self, js):
        self.id = js['id']
        self.intervalMillis = js['intervalMillis']
        self.turns = js['turns']
        self.turnMillis = js['turnMillis']
        self.teamID = js['teamID']
        self.matchTo = js['matchTo']

class XY:
    def __init__(self, data):
      self.x=data['x']
      self.y=data['y']

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = 0
        self.point = 0
        self.isBrick = False

class Agent: 
    def __init__(self,data):
        self.x = data['x']
        self.y = data['y']
        self.teamID = data['teamID']