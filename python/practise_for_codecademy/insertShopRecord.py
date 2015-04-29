#!/usr/bin/python
#coding=utf-8

#argv[1] is the Csv to be modified
#argv[2] is the Csv which contains info of the specified shop
#argv[3] is the output Csv
import sys
import csv
#if len(sys.argv) < 4:
#    print 'Usage: \n\tinsertShopRecord [inputCsvPath] [sourceCsvPath] [outputCsvPath]'
#    sys.exit(1);
##原shop.csv
#argv1 = "D:\work\workspaceForQATraining\python-self-practise\shop.csv"
##要插入的shop的记录csv，第一行可以用“20131122index-data-shop-head”，shop记录可以从“20131122index-data-shop”里grep
#argv2 = "D:\work\workspaceForQATraining\python-self-practise\shop-test.csv"
##生成的添加了特定shop的新shop.csv
#argv3 = "D:\work\workspaceForQATraining\python-self-practise\shop-new.csv"

fieldexist = 0

with open(sys.argv[1],'r') as csvinput:
    with open(sys.argv[2],'r') as source:
        with open(sys.argv[3], 'w') as csvoutput:
            reader = csv.reader(csvinput,dialect="excel-tab",quoting=csv.QUOTE_ALL)
            sourceReader = csv.reader(source,dialect="excel-tab",quoting=csv.QUOTE_ALL)
            writer = csv.writer(csvoutput, lineterminator='\n',dialect="excel-tab",quoting=csv.QUOTE_ALL)

            list_input = list(reader)
            list_resource = list(sourceReader)
            origin_row_num = len(list_input)
            #先把以前存在的商户都写到outputfile里
            for i in range(origin_row_num):
                writer.writerow(list_input[i])

            #对source里的每一行：每一条新商户记录
            for k in range(len(list_resource)-1):
                list_input.append([])
                #对原始csv中每一个字段，找到它在source里是否存在，如果存在，找到对应的列号newDataColumn
                for i in range(len(list_input[0])):
                    fieldname = list_input[0][i]
                    fieldexist = 0
                    for j in range(len(list_resource[0])):
                        if list_resource[0][j] == fieldname:
                            fieldexist = 1
                            break
                    newDataColumn = j
                    if fieldexist == 1:
                        list_input[origin_row_num + k].append(list_resource[k+1][newDataColumn])
                    else:
                        list_input[origin_row_num + k].append("")
                writer.writerow(list_input[origin_row_num + k])



