# Stock Analyzer
Stock Analyzer consists of two parts, data processing python script and DCF_Modeling.xlsx sheet.

# Data processing
The python script is for requesting stock financial data through financialmodelingprep(FMP) API and data processing.

FMP API document: https://site.financialmodelingprep.com/developer/docs

For more usage example: https://youtu.be/ZAAuGEVJsH8 

APIkey in Main.py is empty. Put your API key into APIkey as a string to launch the script.

grep_data_from_FMP(): 
Requesting data from API then save it in csv format.
Run this function whenever you need update stock financial data.

csv_to_dictionary(): Convert csv to list of dictionary.

Run Main.py to get selected data for DCF modeling.

Selected data includes
Revenues/EBITDA/NetIncome/FCFPerShare/SharesOutstanding/CashAndCashEquivalents/TotalDebt/SharePrice per FY.

# DCF Modeling
DCF_Modeling.xlsx is for DCF model calculation.

Copy selected data to blue slots in DCF_Modeling.xlsx.

Input your assumptions according to your understanding on the business of the company.

Then let it do all the work for you.

DCF modeling tutorial
https://youtu.be/LXGSeJsUAaw


**The Data processing and DCF modeling is base on fiscal year data. You may change to quarterly data according to your need.**
