
import requests
import csv

def grep_data_from_FMP(companies, years, APIkey,path):

# This section grep original data in csv format and save it to csv file under Financial folder

    for company in companies:
        
        income = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?datatype=csv&limit={years}&apikey={APIkey}")
        balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?datatype=csv&limit={years}&apikey={APIkey}")
        metrics = requests.get(f"https://financialmodelingprep.com/api/v3/key-metrics/{company}?datatype=csv&limit={years}&apikey={APIkey}")
        enterprise_values = requests.get(f"https://financialmodelingprep.com/api/v3/enterprise-values/{company}?datatype=csv&limit={years}&apikey={APIkey}")

        with open(path+company+'_income.csv', 'wb') as f:
            f.write(income.content)
        f.close()
        with open(path+company+'_balance_sheet.csv', 'wb') as f:
            f.write(balance_sheet.content)
        f.close()
        with open(path+company+'_metrics_original.csv', 'wb') as f:
            f.write(metrics.content)
        f.close()
        with open(path+company+'_enterprise_values_original.csv', 'wb') as f:
            f.write(enterprise_values.content)
        f.close()

        # transpose original data.
        a = zip(*csv.reader(open(path+company+'_metrics_original.csv', "r")))
        csv.writer(open(path+company+'_metrics_transpose.csv', "w", newline='')).writerows(a)
        a = zip(*csv.reader(open(path+company+'_enterprise_values_original.csv', "r")))
        csv.writer(open(path+company+'_enterprise_values_transpose.csv', "w", newline='')).writerows(a)
        
    mesg = "Data grep is completed. \n"
    print(mesg)

