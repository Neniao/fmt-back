import requests
import json
from flask import Flask

class CustomerUpdater():

    def __init__(self,vid = None, cus = None):
        if vid is None:
            self.vid = cus['vid']
        elif cus is None:
            self.vid = vid

        self.customer = {"properties":[]}

    def setScore(self,score):
        self.customer["properties"].append({"property":"score","value":score})

    def setCoach(self,coach):
        self.customer["properties"].append({"property":"coach","value":coach})

    def update(self):
	    url="https://api.hubapi.com/contacts/v1/contact/vid/" + str(self.vid) + "/profile?hapikey=2b0cbf32-bc72-40b6-8953-c40aeebeec07"
	    headers = {"Content-Type":"application/json","Accept":"application/json"}
	    response = requests.post(url, headers=headers, data=json.dumps(self.customer))
	    print("update result:",response.text)

def getCustomer(email):
	url="https://api.hubapi.com/contacts/v1/contact/email/"+ email +"/profile?hapikey=2b0cbf32-bc72-40b6-8953-c40aeebeec07"
	return requests.get(url).json()

def setAssessmentResult(result):
	pass
    
    
app = Flask(__name__)


@app.route("/hello")
def a():
    return "hello"
    

app.run()