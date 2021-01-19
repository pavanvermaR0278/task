
# def amortize(amount_cents: int, start_date: datetime, end_date: datetime) -> List[int]
#     pass # your code here
from  datetime import datetime
import calendar
import unittest

# def start_date_isfullmonth(date):
#     #s = int(date.strftime('%d').lstrip("0").replace(" 0", " "))
#     #print(type(s),s)
#     daysInMonth = calendar.monthrange(date.year, date.month)[1]
#     print("No of days in this month ", daysInMonth)
#     print("today's date",int(date.strftime("%d")))
#     if int(date.strftime("%d")) == 1:
#         print("full month")
#         return True
#     else:
#         print("partial month")
#         return False
    #print("inside isfullmonth",date)

# def end_date_isfullmonth(date):
#     #s = int(date.strftime('%d').lstrip("0").replace(" 0", " "))
#     #print(type(s),s)
#     daysInMonth=calendar.monthrange(date.year,date.month)[1]
#     print("No of days in this month ", daysInMonth)
#
#     print("today's date",int(date.strftime("%d")))
#     if int(date.strftime("%d")) == daysInMonth:
#         print("full month")
#         return True
#     else:
#         print("partial month")
#         return False
    #print("inside isfullmonth",date)

def amortize(amount_cents, start_date=None , end_date=None ):
    amount_cents=int(amount_cents*100)
    amount_cent_backup=amount_cents
    LIST = list()
    start_month_full = False
    end_month_full=False
    #print("Amount_cents", amount_cents)
    total_days=int((end_date-start_date).days)
    #print("total no of days",total_days)
    amountperday=round(amount_cents/total_days,2)
    #print("amount per days",amountperday)
    #print("total days in between dates is: ",total_days)
    #print(amount_cents,start_date,end_date)
    #print("start date isFullMonth: ",start_date_isfullmonth(start_date))
    daysInStartMonth = calendar.monthrange(start_date.year, start_date.month)[1]
    #print("daysInStartMonth", daysInStartMonth)
    #print("today's date", int(start_date.strftime("%d")))
    if int(start_date.strftime("%d")) == 1:
        #print("full month")
        start_month_full=True
    # else:
    #     end_month_full+=1
    #     print("partial month")

    #print("end date is full month:", end_date_isfullmonth(end_date))

    daysInEndMonth = calendar.monthrange(end_date.year, end_date.month)[1]
    #print("daysInEndMonth ", daysInEndMonth)

    #print("today's date", int(end_date.strftime("%d")))
    if int(end_date.strftime("%d")) == daysInEndMonth:
        #print("full month")
        end_month_full=True
    # else:
    #     end_month_full+=1
    #     print("partial month")

    #print("start_month_full :",start_month_full)
    #print("end_month_full :",end_month_full)
    total_No_ofmonth=0

    if start_month_full is True and end_month_full is True:
        #print("11111")
        total_No_ofmonth = int(end_date.strftime("%m")) - int(start_date.strftime("%m")) + 1
        #print("total_No_of month", total_No_ofmonth)
        for i in range(total_No_ofmonth-1):
            LIST.append(round(amount_cents/total_No_ofmonth))
        LIST.append(amount_cent_backup-sum(LIST))
        #print("LIST",LIST)
        #print("SUM OF LIST",sum(LIST))
        #print("LIST LENGTH",len(LIST))
        return LIST
    elif start_month_full is True and end_month_full is False:
        #print("22222")
        total_No_ofmonth = int(end_date.strftime("%m")) - int(start_date.strftime("%m"))
        #print("Total no of month excluding last month",total_No_ofmonth)
        amountforlastMonth = round((int(end_date.strftime("%d")))*amountperday)
        #print("amount for last month ",amountforlastMonth)
        amount_cents=amount_cents-amountforlastMonth
        #print("amount excluding last month",amount_cents)
        for i in range(total_No_ofmonth):
            #print("iii",i)
            #print("range",range(total_No_ofmonth-1))
            LIST.append(round(amount_cents / total_No_ofmonth))
            #print("LIST", LIST)
        LIST.append(amount_cent_backup-(sum(LIST)))
        #print("LIST", LIST)
        #print("SUM OF LIST", sum(LIST))
        #print("LIST LENGTH", len(LIST))
        return LIST
    elif start_month_full is False and end_month_full is True:
        #print("3333")
        total_No_ofmonth = int(end_date.strftime("%m")) - int(start_date.strftime("%m"))
        #print("no of month excluding start month",total_No_ofmonth)
        #print("daysInStartMonth",daysInStartMonth)
        k=round((daysInStartMonth-int(start_date.strftime("%d")))*amountperday)
        #print("amount in start month",k)
        LIST.append(k)
        amount_cents=amount_cents-k

        for i in range(total_No_ofmonth-1):
            LIST.append(round(amount_cents / total_No_ofmonth))
        LIST.append(amount_cent_backup-sum(LIST))
        #print("LIST", LIST)
        #print("SUM OF LIST", sum(LIST))
        #print("LIST LENGTH", len(LIST))
        return LIST
    else:# condition if, start and end month both are partial
        #print("4444")
        total_No_ofmonth = int(end_date.strftime("%m")) - int(start_date.strftime("%m"))-1
        #print("no of month excluding start and end month", total_No_ofmonth)
        amountforlastMonth = round((int(end_date.strftime("%d"))) * amountperday)
        #print("amount for last month ", amountforlastMonth)

        #print("amount excluding last month", amount_cents)
        #print("daysInStartMonth", daysInStartMonth)
        k = round((daysInStartMonth - int(start_date.strftime("%d"))) * amountperday)
        #print("amount in start month", k)
        LIST.append(k)
        amount_cents = amount_cents - (k+amountforlastMonth)
        #L = (int(end_date.strftime("%d"))) * amountperday
        #print("amount for last month",L)
        #amount_cents = amount_cents - (L+k)
        for i in range(total_No_ofmonth):
            LIST.append(round(amount_cents / total_No_ofmonth))
        LIST.append(amount_cent_backup-sum(LIST))
        #print("LIST", LIST)
        #print("SUM OF LIST", sum(LIST))
        #print("LIST LENGTH", len(LIST))
        return LIST
#amortize(997,datetime(2019,2,12),datetime(2019,3,25))
#amortize(991,datetime(2019,3,1),datetime(2019,5,31))


class amortizeTest(unittest.TestCase):

    def test_1_length(self):
        self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,3,25))), 2, "Should be 2")
    def test_1_sum(self):
        self.assertEqual(sum(amortize(997,datetime(2019,2,12),datetime(2019,3,25))), 99700, "Should be 99700")

    def test_2_length(self):
        self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    def test_2_sum(self):
        self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")

    def test_3_length(self):
        self.assertEqual(len(amortize(991,datetime(2019,2,1),datetime(2019,5,31))), 4, "Should be 4")
    def test_3_sum(self):
        self.assertEqual(sum(amortize(991,datetime(2019,2,1),datetime(2019,5,31))), 99100, "Should be 99100")

    def test_4_length(self):
        self.assertEqual(len(amortize(997,datetime(2019,2,15),datetime(2019,5,31))), 4, "Should be 4")
    def test_4_sum(self):
        self.assertEqual(sum(amortize(997,datetime(2019,2,12),datetime(2019,5,31))), 99700, "Should be 99700")

    def test_5_length(self):
        self.assertEqual(len(amortize(99,datetime(2019,3,12),datetime(2019,5,31))), 3, "Should be 3")
    def test_5_sum(self):
        self.assertEqual(sum(amortize(99,datetime(2019,3,12),datetime(2019,5,31))), 9900, "Should be 9900")

    def test_6_length(self):
        self.assertEqual(len(amortize(997,datetime(2019,2,1),datetime(2019,6,15))), 5, "Should be 5")
    def test_6_sum(self):
        self.assertEqual(sum(amortize(997,datetime(2019,2,1),datetime(2019,6,15))), 99700, "Should be 99700")

    def test_7_length(self):
        self.assertEqual(len(amortize(997,datetime(2019,4,12),datetime(2019,10,25))), 7, "Should be 7")
    def test_7_sum(self):
        self.assertEqual(sum(amortize(9555,datetime(2019,4,12),datetime(2019,10,25))), 955500, "Should be 955500")

    # def test_8_length(self):
    #     self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    # def test_8_length(self):
    #     self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")
    #
    # def test_9_length(self):
    #     self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    # def test_9_length(self):
    #     self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")
    #
    # def test_10_length(self):
    #     self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    # def test_10_length(self):
    #     self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")
    #
    # def test_11_length(self):
    #     self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    # def test_11_length(self):
    #     self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")
    #
    # def test_12_length(self):
    #     self.assertEqual(len(amortize(997,datetime(2019,2,12),datetime(2019,5,25))), 4, "Should be 4")
    # def test_12_length(self):
    #     self.assertEqual(sum(amortize(991,datetime(2019,2,12),datetime(2019,5,25))), 99100, "Should be 99100")
if __name__ == '__main__':
     unittest.main()