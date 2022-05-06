import Account
import Instruments
import Order
import Trade
import Transactions
import datetime
import calendar
import time




class Configuration():
    def __init__(self, buyType, myToken):
        self.token = myToken
        if buyType.upper() == "P":
            self.type = "api-fxpractice.oanda.com"
        else:
            self.type = "api-fxtrade.oanda.com"

    # Account

    def Accounts(self):
        return Account.OandaAccount(self.type, self.token)

    # Instruments

    def Instruments(self):
        return Instruments.OandaInstruments(self.type, self.token)

    # Orders
    def Orders(self):
        return Order.AondaOrder(self.type, self.token)


    # Trades
    def Trades(self):
        return Trade.Trade(self.type, self.token)

    
    # Transations
    def Transactions(self):
        return Transactions.Transactions(self.type, self.token)
    
    
    def data(self):
        return self.type, self.token

    #
    # Other functions
    #
    
    # Get the diference between dates
    def getCount(self, date, interval):

        dateArr = date
        nowYear = str(datetime.datetime.now()).split(" ")[0]
        totYears = int(str(nowYear).split("-")[0]) - int(dateArr)
        totDays = []
        totCount = []
        for c in range(0, totYears):
            if self.isLeapYear(int(dateArr) + +c):
                tot = round(336 * (60 / interval))
                print(tot)
                totDays.append(366)
                if tot > 5000:
                    totCount.append(tot)
                    totDays.append(366)
                else:
                    totCount.append(tot)
            else:
                tot = round(336 * (60 / interval))
                totDays.append(365)
                if tot > 5000:
                    totCount.append(tot)
                    totDays.append(365)
                else:
                    totCount.append(tot)

        return totCount, totDays

    # Return True/False if not is leep year
    def isLeapYear(self, year):

        return calendar.isleap(year)

    # Get the date formated especific date
    def timeZone(self, date):  # format yyyy-mm-dd

        if "-" in str(date):
            return str(date) + "T00%00%00.000000Z"
        else:
            return str(datetime.datetime.now()).split(" ")[0] + "T00%00%00.000000Z"

    # Get the date formated especific date and hour
    def timeZoneDay(self, date, h):  # format yyyy-mm-dd / h:hour(24)
        
        if h < 10:
                h = "0" + str(h)
        if "-" in str(date):
            
            return str(date) + "T"+str(h)+"%00%00.000000Z"
        else:
            return str(datetime.datetime.now()).split(" ")[0] + "T"+str(h)+"%00%00.000000Z"
    
    
    # get the now date formated
    def timeZoneNow(self, timer=0):

        if timer <= 0:
            ret = str(datetime.datetime.now())
        else:
            ret = str(datetime.datetime.now() - datetime.timedelta(hours=+timer)).split(" ")

        time.sleep(2)
        return ret[0] + "T" + ret[1] + "Z"

    # get day of week
    def getDay(self):

        weekDay = calendar.weekday(int(str(str(datetime.datetime.now()).split(" ")[0]).split("-")[0]),
                                   int(str(str(datetime.datetime.now()).split(" ")[0]).split("-")[1]),
                                   int(str(str(datetime.datetime.now()).split(" ")[0]).split("-")[2]))
        if weekDay == 0:
            return "Monday"
        if weekDay == 1:
            return "Tuesday"
        if weekDay == 2:
            return "Wednesday"
        if weekDay == 3:
            return "Thursday"
        if weekDay == 4:
            return "Friday"
        if weekDay == 5:
            return "Saturday"
        if weekDay == 6:
            return "Sunday"

        return weekDay

    # Get date hour in timestamp
    def getTimeStamp(self):

        return datetime.datetime.today().timestamp()

    # Get the date minus Days/Hours/Minuts
    def newDate(self, change, value):

        if str(change).upper() == "D":
            date = str(datetime.datetime.now() - datetime.timedelta(days=value)).split(" ")[0]
        if str(change).upper() == "H":
            date = str(datetime.datetime.now() - datetime.timedelta(hours=value)).split(" ")[0]
        if str(change).upper() == "M":
            date = str(datetime.datetime.now() - datetime.timedelta(minutes=value)).split(" ")[0]

        return date
