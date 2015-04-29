#!/usr/bin/python
#coding=utf-8

import urllib, os

def make_url_from_keyword_file(input_dir, input_filename, cityid, output_filename):
    input_file = open(os.path.join(input_dir, input_filename), "r")
    output_file = open(os.path.join(input_dir, output_filename),"w")
    lst_reader = input_file.readlines()
    for keyword in lst_reader:
        url_str = "query=term(cityid," + str(cityid) + "),term(categoryids,10),keyword(searchkeyword," + str(urllib.quote(keyword.strip("\n"))) + ")&sort=desc(popularity)&fl=shopid,defaultpic,shopname,branchname,avgprice,displayscore1,displayscore2,displayscore3,shoppower,fulladdress,categoryids,regionids,votetotal,category1,category2,region1,region2,shoptype&limit=0,20&info=app:RsWeb,platform:WWW,bookseattype:4,unrelatedguidefields:regionids%3Bcategoryids%3Bshoptagsnames%3Bpricerange,bookstarttime:2014-01-01_00-00\n"
        #url_str = "query=term(categoryids," + keyword.strip("\n") + "),term(cityid," + str(cityid) + ")&sort=desc(dpscore)&fl=shopid,shopname,shoppower,branchname,altname,power,shopgroupid,shoptype,cityid,defaultpic,avgprice,phone,address,crossroad,score1,score2,score2,dishtags,pictotal,hasbooksetting,dealgroupid,membercardid,membercardtitle,smspromoid,booktype,dealgrouptitle,dealgroupprice,contenttitle,hasticket,region1,category1,gpoi,isnewshop,shoptags,publictransit,businesshours,prepaidcards&limit=0,25&info=clientversion:6.3,app:DistrictShopSearch,platform:MAPI,userlng:121.41583,clientip:192.168.211.162,userlat:31.21777,sorttype:1,unrelatedguidefields:categoryids%3Bregionids,geoFieldName:poi,bookstarttime:2014-01-01_00-00,mobileplatform:1,poi:121.41583%3A31.21777,bookseattype:3\n"
        output_file.write(url_str)
    input_file.close()
    output_file.close()

make_url_from_keyword_file("F:\\", "hot-keyword-shanghai.csv", 1, "www-book-query-shanghai.txt")


