# Stock Analyzer
Stock Analyzer consists of two parts, data processing python script and DCF Modeling xlsx sheet.

# Data processing
The python script is for requesting stock financial data through financialmodelingprep(FMP) API and data processing.

For FMP API:
https://site.financialmodelingprep.com/developer/docs

APIkey in main.py is empty, put your API key into APIkey as a string to launch the script.

grep_data_from_FMP(): 
grep data frmo API then save it in csv format.
Run this function whenever you need update stock financial data.

csv_to_dictionary(): convert csv to list of dictionary.

run main.py to grep selected data.

Watch https://youtu.be/ZAAuGEVJsH8 for more usage example 

# DCF Modeling
DCF_Modeling.xlsx is for DCF model calculation

Copy selected data to blue slots in DCF_Modeling.xlsx

Input your assumptions according to your understanding on the business of the company.

Then let it do all the work for you.

DCF modeling tutorial
https://youtu.be/LXGSeJsUAaw
