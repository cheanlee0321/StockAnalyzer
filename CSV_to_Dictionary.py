
import csv
import copy

from numpy import transpose

def csv_to_dictionary(filename, years, type):
    # years : first N years
    # type : 1, original data
    #        2, transposed data
    # Read csv files and convert it to list of dictionary
    DataList=[]
    with open(filename) as data:
        for row in csv.reader(data):
            if row[2] != '':
                DataList.append(row)

    #years = len(DataList[0]) - 2
    dictionary_main = []
    if type == 1:
        for i in range(years): # years
            dictionary_sub={}
            dictionary_sub[DataList[0][0]] = DataList[0][2+i] # date
            for j in range(len(DataList)-1): # remove date
                dictionary_sub[DataList[1+j][1]] = DataList[1+j][2+i]
            dictionary_main.append(copy.deepcopy(dictionary_sub))
            dictionary_sub.clear()
    else:
        for i in range(years): # years
            dictionary_sub={}
            dictionary_sub[DataList[0][0]] = DataList[0][1+i] # date
            for j in range(len(DataList)-1): # remove date
                dictionary_sub[DataList[1+j][0]] = DataList[1+j][1+i]
            dictionary_main.append(copy.deepcopy(dictionary_sub))
            dictionary_sub.clear()
    dictionary_main.reverse()


    mesg = "CSV to Dict: " + filename + " done."
    print(mesg)

    return dictionary_main