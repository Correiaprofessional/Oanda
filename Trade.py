import re
import urllib3
import certifi
import json
import requests
import datetime
from json import encoder
import logData



class Trade():
    def __init__(self,urlBase,token):

        self.urlBase = "https://" + urlBase + "/v3/" + "accounts/"
        self.urltype = "/openTrades"
        self.headerGet = {"Content-Type": "application/json",
                          "Authorization": "Bearer " + token}



    def getTrades(self,account):

        url = self.urlBase + account + self.urltype
        response = requests.get(url, headers=self.headerGet)
        lstTrade = json.loads(response.content.decode())
        return lstTrade["trades"]


    def CloseTrades(self,id,units,account):



        body = {"units": units}
        url = self.urlBase + account +  "/trades/"+id+"/close"
        response = requests.put(url, json=body, headers=self.headerGet)
        delTrade = json.loads(response.content.decode())
        return delTrade["orderFillTransaction"]





