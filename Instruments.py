import json
import requests
import datetime
from json import encoder
import logData
import Account



class OandaInstruments():
    def __init__(self,urlBase,token):
        acc = urlBase
        self.urlBase = "https://"+urlBase+"/v3/"
        self.urltype = "instruments/"
        self.headerGet = {"Content-Type": "application/json",
                          "Authorization": "Bearer " + token}

    def getCandles_inst(self, inst,type="1", datefrom = 0, interval = 1, count =1):

        try:
            if type == "1": #Get the 6 most recent midpoint-based EUR/USD 5-second candles
                url = self.urlBase + self.urltype + inst + "/candles?count="+str(count)+"&price=M&granularity=S" + str(interval)
            if type == "2": #Get all bid/ask-based USD/CAD 1-minute candles since 2016-10-17T15:00:00
                url = self.urlBase + self.urltype + inst + "/candles?price=BA&from=" + str(datefrom) + "&granularity=M" + str(interval)
            if type == "3": #Get 10 ask-based USD/JPY 1-day candles starting at 2016-10-01T00:00:00
                url = self.urlBase + self.urltype + inst + "/candles?count="+str(count)+"&price=BA&from="+str(datefrom)+"&granularity=D"
            response = requests.get(url,headers=self.headerGet)
            cand = json.loads(response.content.decode())
            #print(cand)
            return cand["candles"]
        except Exception as e:
            return e

    def getOrderBook_inst(self, inst):

        url = self.urlBase + self.urltype + inst + "/orderBook"
        response = requests.get(url, headers=self.headerGet)
        ordbk = json.loads(response.content.decode())

        return ordbk


    def getPosBook_inst(self,inst, date="", type="1"):

        if type == "1":
            url = self.urlBase + self.urltype + inst + "/positionBook"
        if type == "2":
            url = self.urlBase + self.urltype + inst + "/positionBook?time=" + str(date)

        response = requests.get(url, headers=self.headerGet)
        posbk = json.loads(response.content.decode())

        return posbk


