#!/usr/bin/python
#coding=utf-8

import os

def del_invalid_limit_query(dir, input_filename, output_filename):
    input_file = open(os.path.join(dir, input_filename), "r")
    output_file = open(os.path.join(dir, output_filename), "w")
    lst_query = input_file.readlines()
    for query in lst_query:
        del_this_query = False
        query_part = query.split("&")
        for item in query_part:
            if "limit" in item:
                temp = item[item.index("=")+1:]
                start = temp.split(",")[0]
                pagesize = temp.split(",")[1]
                if (int(start) + int(pagesize)) >= 60000:
                    del_this_query = True
            else:
                continue
        if not del_this_query:
            output_file.write(query)
        else:
            continue
    input_file.close()
    output_file.close()


del_invalid_limit_query("F:\\", "test.query.tuangou.log", "query.tuangou.log")




