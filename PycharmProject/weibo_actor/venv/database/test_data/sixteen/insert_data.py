# -*- coding: utf-8 -*-

from pymongo import MongoClient
conn = MongoClient('localhost')
db = conn.mydb
my_set = db.test_set

# 插入数据
with open('./2016.txt', 'r+') as f:
    for line in f.readlines():
        line_data = line.split('')
        _id = line_data[1]
        year = 2016
        movie_name = line_data[0]
    company = open('./' + movie_name + '.txt', 'r+')

    i = 0
    for company_data in company.readlines():
        company_data = company_data.split('{')[1].split('}')[0]
        if i == 0:
            p_company = company_data
            i = 1
        elif i == 1:
            l_company = company_data

    my_set.insert({"_id": _id, "year": year, "movie_name": movie_name, "p_company": {p_company}, "l_company": {l_company}})

# 查询数据
for data in my_set.find():
    print(data)