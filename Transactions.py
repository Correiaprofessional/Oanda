import json
import requests
import datetime
from json import encoder
import time


class Transactions():
    def __init__(self,urlBase,token):
        
        self.urlBase = "https://" + urlBase + "/v3/" + "accounts/"
        self.urltype = "/transactions"
        self.headerGet = {"Content-Type": "application/json",
                          "Authorization": "Bearer " + token}
        
        
    def TransByDate(self,fDta,lDta, account):
        
        body = {"to":lDta,
                "from": fDta,
                "pageSize": 500}
        url = self.urlBase + account + self.urltype
        response = requests.get(url, json=body, headers=self.headerGet)
        lstTrans = json.loads(response.content.decode())
        return self.TransByDatePages(lstTrans["pages"])

    def TransByDatePages(self,lnks):
        
        ret = []
        for url in lnks:
        #url = lnks[0]
            response = requests.get(url, headers=self.headerGet)
            lstTransPages = json.loads(response.content.decode())
            ret.append(lstTransPages)
        df = [x for x in lstTransPages["transactions"]]
        return df



