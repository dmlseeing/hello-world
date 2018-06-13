# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient
# conn = MongoClient('192.168.235.55', )
conn = MongoClient('localhost')
db = conn.mydb
data = db.company_2016
# data = db.company_2017

# 2016
# 插入数据
with open('./2016.txt', 'r+') as f:
    for line in f.readlines():
        dict0 = {}
        line_data = line.split('')
        dict0['_id'] = line_data[1].split('\n')[0]
        dict0['year'] = 2016
        dict0['movie_name'] = line_data[0]

        i = 0
        company = open('./2016/' + dict0['movie_name'] + '.txt', 'r+', encoding='gbk')
        for company_data in company.readlines():
            try:
                company_data = company_data.split('{')[1].split('}')[0]
                if i == 0:
                    dict0['p_company'] = company_data
                    i = 1
                elif i == 1:
                    dict0['l_company'] = company_data
            except IndexError as ex1:
                if i == 0:
                    dict0['p_company'] = 'null'
                    i = 1
                elif i == 1:
                    dict0['l_company'] = 'null'
        data.insert(dict0)
"""
# 2017
# 插入数据
with open('./2017.txt', 'r+') as f:
    for line in f.readlines():
        dict0 = {}
        line_data = line.split('')
        dict0['_id'] = line_data[1].split('\n')[0]
        dict0['year'] = 2017
        dict0['movie_name'] = line_data[0]

        i = 0
        company = open('./2017/' + dict0['movie_name'] + '.txt', 'r+', encoding='gbk')
        for company_data in company.readlines():
            try:
                company_data = company_data.split('{')[1].split('}')[0]
                if i == 0:
                    dict0['p_company'] = company_data
                    i = 1
                elif i == 1:
                    dict0['l_company'] = company_data
            except IndexError as ex1:
                if i == 0:
                    dict0['p_company'] = 'null'
                    i = 1
                elif i == 1:
                    dict0['l_company'] = 'null'
        data.insert(dict0)
"""