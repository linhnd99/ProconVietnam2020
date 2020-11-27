import requests 
import json

TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiYXNzeXJpYW4iLCJpYXQiOjE2MDY0NTk3NDUsImV4cCI6MTYwNjU0NjE0NX0.Kg43OkKqxeDoNPwZW8x3ebu7f1i88Ownd3Kw82Zf9Qo'
DOMAIN = 'http://112.137.129.202:8004'

class RequestToServer:    
    def __init__(self):
        return
        
    def getMatches(self):
        res = requests.get(DOMAIN+'/matches',headers={'Authorization':TOKEN})
        data = json.loads(res.content.decode('utf-8'))
        if 'message' in data :
            print(data['message'])
            return -1
        return data

    def getDataMatch(self,id):
        url = DOMAIN+'/matches/'+str(id)
        res = requests.get(url,headers={'Authorization':TOKEN})
        data = json.loads(res.content.decode('utf-8'))
        if 'message' in data :
            print(data['message'])
            return
        return data
