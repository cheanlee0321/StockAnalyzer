# Stock Analyzer
Stock Analyzer consists of two parts, data processing python script and DCF Modeling xlsx sheet.

# Data processing
The python script is for stock financial data grep through financialmodelingprep API 

https://site.financialmodelingprep.com/developer/docs

APIkey is empty, put your API key into APIkey as a string to launch the script

grep_data_from_FMP(): 
grep data frmo API then save it in csv format.
Run this function whenever you need update stock financial data.

csv_to_dictionary(): convert csv to list of dictionary.

run main.py to grep selected data.

# DCF Modeling
DCF_Modeling.xlsx is where the magic happens.

Copy selected data to blue slots in DCF_Modeling.xlsx

Input your assumptions according to your understanding on the business of the company.

Then let it do all the magic for you.
