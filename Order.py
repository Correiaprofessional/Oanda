import re
import urllib3
import certifi
import json
import requests
import datetime
from json import encoder
import logData



class AondaOrder():
    def __init__(self,urlBase,token):

        self.urlBase = "https://" + urlBase + "/v3/" + "accounts/"
        self.urltype = "/orders"
        self.headerGet = {"Content-Type": "application/json",
                          "Authorization": "Bearer " + token}


    def basicBuyOrder_ord(self,units,inst,account):


        url = self.urlBase + str(account) + self.urltype
        body = {
          "order": {
            "units": units,
            "instrument": inst,
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }
        response = requests.post(url, json=body,  headers=self.headerGet)
        order = json.loads(response.content.decode())

        return order

    def basicSellOrder_ord(self,units,inst,account):


        url = self.urlBase + str(account) + self.urltype
        body = {
          "order": {
            "units": "-"+ str(units),
            "instrument": inst,
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }
        response = requests.post(url, json=body,  headers=self.headerGet)
        order = json.loads(response.content.decode())

        return order

    def takeProfitOrder_ord(self,price,tradeId,account):


        url = self.urlBase + str(account) + self.urltype
        body = {
              "order": {
                "timeInForce": "GTC",
                "price": str(price),
                "type": "TAKE_PROFIT",
                "tradeID": str(tradeId)
              }
            }
        response = requests.post(url, json=body,  headers=self.headerGet)
        order = json.loads(response.content.decode())

        return order

    #( >0int,>0int,>0int)
    def limitOrder(self,pricebuy,pricestopLoss,priceProfitFill,inst,units,account):
        try:
            '''if priceProfitFill == "" or pricestopLoss == "":
                return {"error" : "Profit/Loss must be fill" }

            if priceProfitFill <= pricebuy:
                return {"error" : "Profit can't be smaller than Buying price"}

            if pricestopLoss >= pricebuy:
                return {"error" : "Loss can't be higher than Buying price "}'''


            url = self.urlBase + str(account) + self.urltype
            body = ""

            #if pricestopLoss <= 0 and priceProfitFill > 0:
            body = {
                "order": {
                    "price": str(pricebuy),
                    "takeProfitOnFill": {
                        "price": str(priceProfitFill)
                        },
                    "timeInForce": "GTC",
                    "instrument": str(inst),
                    "units": str(units),
                    "type": "LIMIT",
                    "positionFill": "DEFAULT"
                    }
                }
            '''if priceProfitFill <= 0 and pricestopLoss > 0:
                body = {
                    "order": {
                        "price": str(pricebuy),
                        "stopLossOnFill": {
                            "timeInForce": "GTC",
                            "price": str(pricestopLoss)
                        },
                        "timeInForce": "GTC",
                        "instrument": str(inst),
                        "units": str(units),
                        "type": "LIMIT",
                        "positionFill": "DEFAULT"
                    }
                }'''



            response = requests.post(url, json=body,  headers=self.headerGet)
            order = json.loads(response.content.decode())
            
            return order["orderFillTransaction"]
        except Exception as e:
            return {"ERROR" : e}


    def cancelOrderId(self,id):
        pass


    def getOrder(self,inst,account):

        url = self.urlBase + account+"/orders?instrument=" + inst
        response = requests.get(url, headers=self.headerGet)
        order = json.loads(response.content.decode())
        return order

    def deleteOrder(self,orderId,account):

        url = self.urlBase + account + "/orders/"+orderId+"/cancel"
        response = requests.put(url, headers=self.headerGet)
        order = json.loads(response.content.decode())
        return order

    def allOrder(self,account):


        url = self.urlBase + account + "/pendingOrders"
        response = requests.get(url, headers=self.headerGet)
        order = json.loads(response.content.decode())
        return order["orders"]
