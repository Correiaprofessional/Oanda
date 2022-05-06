import json
import requests
from json import encoder
import logData





class OandaAccount():
    
    
    # Establish base URL
    def __init__(self,urlBase,token):
        self.urlBase = "https://"+urlBase+"/v3/"
        self.headerGet = {"Content-Type" : "application/json",
            "Authorization": "Bearer " + token}


    # Get the Account ID
    def getID_acc(self):


        try:
            url = self.urlBase + "accounts"
            response = requests.get(url, headers=self.headerGet)
            jsn = json.loads(response.content.decode())
            myID = jsn["accounts"][0]["id"]

            return myID
        except:
            return {"ERROR" : ""}

    # Get Account Details
    def getDet_acc(self):

        url = self.urlBase + "accounts/" + self.getID_acc()
        response = requests.get(url, headers=self.headerGet)
        details = json.loads(response.content.decode())

        return details["account"]


    # Get Account summary
    def getSumma_acc(self):

        url = self.urlBase + "accounts/" + self.getID_acc() + "/summary"
        response = requests.get(url, headers=self.headerGet)
        summa = json.loads(response.content.decode())

        return summa["account"]

    # Get Instrument instruments allowed by account, and definitions to each intrument
    def getInsts_acc(self):

        url = self.urlBase + "accounts/" + self.getID_acc() + "/instruments"

        response = requests.get(url, headers=self.headerGet)
        inst = json.loads(response.content.decode())
        #print(inst)
        lstArrInst = []
        lstArrPrec = []
        for k in range(0, len(inst["instruments"]) - 1):
            lstArrInst.append(inst["instruments"][k]["name"])
            lstArrPrec.append([inst["instruments"][k]["minimumTrailingStopDistance"], inst["instruments"][k]["maximumOrderUnits"]])
            #print(inst["instruments"][k]["name"])

        return lstArrInst,lstArrPrec

    # Get changes on account
    def getChanges_acc(self,lstId):

        url = self.urlBase + "accounts/" + self.getID_acc() +"/changes?sinceTransactionID=" + str(lstId)

        response = requests.get(url,headers=self.headerGet)
        chng = json.loads(response.content.decode())


        return chng["changes"]




if __name__ == "__main__":
    Ocon = OandaAccount()
    print(Ocon.getID_acc())
    print(Ocon.getInsts_acc())
    print(Ocon.getSumma_acc())
    print(Ocon.getDet_acc())
    print(Ocon.getChanges_acc(1)["ordersCreated"])