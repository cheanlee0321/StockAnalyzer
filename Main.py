# This script is using financialmodelingprep API to grep company financial data.
# https://site.financialmodelingprep.com/developer/docs
# Register an account to get free API Key

import requests
import csv
import copy
import matplotlib.pyplot as plt
from DataGrep import grep_data_from_FMP
from CSV_to_Dictionary import csv_to_dictionary

company = 'TCEHY' # for testing
companies_L1 = ['BABA','TCEHY','PLTR','HD','WLTW','ZM','SNPS','GOOG','ADBE','KO','NVDA','BRKB','AMD'] # tracking list
years = 5
APIkey = '' # put your APIkey here
path = './Financial/'

# Grep data from FMP, save data under 'path'
grep_data_from_FMP(companies_L1, 5, APIkey, path)

# Read csv files and convert it to list of dictionary
income_data = csv_to_dictionary(path+company+'_income.csv', years, 1)
balance_sheet_data = csv_to_dictionary(path+company+'_balance_sheet.csv', years, 1)
metrics_data = csv_to_dictionary(path+company+'_metrics_transpose.csv', years, 2)
enterprise_values_data = csv_to_dictionary(path+company+'_enterprise_values_transpose.csv', years, 2)

# This section grep selected data and save it to csv file under Financial folder
# Revenues/EBITDA/NetIncome/FCFPerShare/SharesOutstanding/CashAndCashEquivalents/TotalDebt/SharePrice
FYdate = list([income_data[i]['date'] for i in range(len(income_data))])
FYdate.insert(0, 'FYdate')
Revenues = list([income_data[i]['revenue'] for i in range(len(income_data))])
Revenues.insert(0, 'Revenue')
EBITDA = list([income_data[i]['EBITDA'] for i in range(len(income_data))])
EBITDA.insert(0, 'EBITDA')
NetIncome = list([income_data[i]['netIncome'] for i in range(len(income_data))])
NetIncome.insert(0, 'NetIncome')
FCFPerShare = list([metrics_data[i]['freeCashFlowPerShare'] for i in range(len(metrics_data))])
FCFPerShare.insert(0, 'FCFPerShare')
SharesOutstanding = list([enterprise_values_data[i]['numberOfShares'] for i in range(len(enterprise_values_data))])
SharesOutstanding.insert(0, 'SharesOutstanding')
CashAndCashEquivalents = list([balance_sheet_data[i]['cashAndCashEquivalents'] for i in range(len(balance_sheet_data))])
CashAndCashEquivalents.insert(0, 'CashAndCashEquivalents')
TotalDebt = list([balance_sheet_data[i]['totalDebt'] for i in range(len(balance_sheet_data))])
TotalDebt.insert(0, 'TotalDebt')
SharePrice = list([enterprise_values_data[i]['stockPrice'] for i in range(len(enterprise_values_data))])
SharePrice.insert(0, 'SharePrice')

#add newline='' to avoid additional empty line
with open('./Financial/'+company+'_selected_data.csv', 'w', newline='') as f1:
    writer = csv.writer(f1)
    writer.writerow(FYdate)
f1.close()

with open('./Financial/'+company+'_selected_data.csv', 'a', newline='') as f2:
    writer = csv.writer(f2)
    writer.writerow(Revenues)
    writer.writerow(EBITDA)
    writer.writerow(NetIncome)
    writer.writerow(FCFPerShare)
    writer.writerow(SharesOutstanding)
    writer.writerow(CashAndCashEquivalents)
    writer.writerow(TotalDebt)
    writer.writerow(SharePrice)
f2.close()

mesg = "Python script finished."
print(mesg)

"""
API usage notes:
Access specific data
income = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={APIkey}")
income_data = income.json()

First year revenue = income[0]['revenue']
               EPS = income[0]['eps']
            EBITDA = income[0]['ebitda']

print(income_data[0]['revenue'])

revenues = list(reversed([income[i]['revenue'] for i in range(len(income))]))
plt.plot(revenues, label="Revenue")
plt.show()

"""
