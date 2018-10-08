# coding=utf-8

import tushare as ts
import json

df = ts.month_boxoffice() #取上月票房数据
#print(df)
movie1to5 = {}
for index, row in df.iterrows():
    if index < 5:
        i = str(index)
        movie1to5[i] = {}
        movie1to5[i]["irank"] = str(row["Irank"])
        movie1to5[i]["name"] = str(row["MovieName"])
        movie1to5[i]["avgprice"] = str(row["avgboxoffice"])
        movie1to5[i]["avgshowcount"] = str(row["avgshowcount"])
        movie1to5[i]["boxoffice"] = str(row["boxoffice"])

with open("box-office-data.json", "w+") as f:
    json.dump(movie1to5, f)