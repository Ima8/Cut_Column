# -*- coding: utf-8 -*-
import csv
from collections import defaultdict

fileInput = "data/input1.csv"
fileOutput = "output/output.csv"


def getColumnsByHeader():
    # each value in each column is appended to a list
    columns = defaultdict(list)
    with open(fileInput, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        # read a row as {column1: value1, column2: value2,...}
        for row in reader:
            for (k, v) in row.items():  # go over each column name and value
                    # append the value into the appropriate list
                columns[k].append(v)
                    # based on column name k

    # print(columns['user_messages'])
    # print(columns['answers.message'])
    return columns
# getColumnsByHeader()


def getColumnsByNumber():
    # each value in each column is appended to a list
    columns = defaultdict(list)
    with open(fileInput, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip first line
        for row in reader:
            for (i, v) in enumerate(row):
                columns[i].append(v)
    # print(columns[0])
    return columns


# getColumnsByHeader()
# getColumnsByNumber()
def cutColumns(col1,col2):
    with open(fileOutput, 'a', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        columns = getColumnsByNumber()
        for pair in zip(columns[col1], columns[col2]):
            outfile.write(pair[0]+"\t"+pair[1])
            outfile.write('\n')

cutColumns(1,3) # Keep only column 1 and 3
