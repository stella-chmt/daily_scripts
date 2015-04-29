#!/usr/bin/python
#coding=utf-8

import urllib, os

def make_url_from_keyword_file(input_dir, input_filename, output_filename):
    input_file = open(os.path.join(input_dir, input_filename), "r")
    output_file = open(os.path.join(input_dir, output_filename),"w")
    lst_reader = input_file.readlines()
    for shopinfo in lst_reader:
        cityid = shopinfo.split("\t")[0]
        keyword = shopinfo.split("\t")[1].strip("\n")
        url_str = cityid + "&keyword=" + str(urllib.quote(keyword)) + "\n"
        #url_str = "cityid=" + cityid + "&keyword=" + str(keyword) + "\n"
        output_file.write(url_str)
    input_file.close()
    output_file.close()

make_url_from_keyword_file("../Docs", "shop-hot_keyword.txt", "query-suggest.bin.txt")


