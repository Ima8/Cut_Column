# -*- coding: utf-8 -*-
import csv
from collections import defaultdict
from os import listdir
from os.path import isfile, join

fileInput = "data/me_intentions - ME by TMB App.tsv"
fileOutput = "output/output.csv"


def getColumnsByHeader(fileInput):
    # each value in each column is appended to a list
    columns = defaultdict(list)
    with open(fileInput, 'rt', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        # read a row as {column1: value1, column2: value2,...}
        for row in reader:
            for (k, v) in row.items():  # go over each column name and value
                    # append the value into the appropriate list
                columns[k].append(v)
                    # based on column name k
    return columns
# getColumnsByHeader()


def getColumnsByNumber(fileInput):
    # each value in each column is appended to a list
    columns = defaultdict(list)
    with open(fileInput, 'rt', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None)  # Skip first line
        next(reader, None)  # Skip second line
        for row in reader:
            for (i, v) in enumerate(row):
                columns[i].append(v)
    # print(columns[0])
    return columns


# getColumnsByHeader()
# getColumnsByNumber()
def cutColumns(file,col1,col2):
    print(file)
    with open(fileOutput, 'a', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        columns = getColumnsByNumber(file)
        for pair in zip(columns[col1], columns[col2]):
            if len(pair[0])>5 and len(pair[1])>5:
                outfile.write(pair[0]+"\t"+pair[1])
                outfile.write('\n')

#cutColumns('data/me_intentions - Contact.tsv',1,3) # Keep only column 1 and 3

def cutAllFiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        cutColumns('data/'+file,1,3)

cutAllFiles('data')