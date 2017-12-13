from flask import Flask, request, jsonify
import requests
import json

# Import parsing functions to test
from rank import rankUrls

import sys
import os
sys.path.append(os.path.abspath('./rankURL_test'))

expected = ['www.example.com']
print('test one'.ljust(30)[:30], "\t", 'expected')
from rankURL_test1 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')

expected = ['www.anotherexample.com', 'www.example.com']
print('test two'.ljust(30)[:30], "\t", 'expected')
from rankURL_test2 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')

#  print(sorted_adocs[0].document)

expected = ['www.example.com', 'www.anotherexample.com']
print('test three'.ljust(30)[:30], "\t", 'expected')
from rankURL_test3 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')

#  print(sorted_adocs[0].document)

expected = ['www.example-3.com']
print('test four'.ljust(30)[:30], "\t", 'expected')
from rankURL_test4 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')
#  print(sorted_adocs[0].document)

expected = ['www.anotherexample.com', 'www.example.com', 'www.example-3.com']
print('test five'.ljust(30)[:30], "\t", 'expected')
from rankURL_test5 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')
#  print(sorted_adocs[0].document)

expected = ['https://www.lucre.zone', 'https://www.business.biz',
            'https://www.money.com', 'https://www.sales.org', 'https://www.free.market']
print('test six'.ljust(30)[:30], "\t", 'expected')
from rankURL_test6 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)

for i in range(0, len(sorted_adocs)):
    print(sorted_adocs[i].document.ljust(30)[:30], "\t", expected[i])
print('\n')
#  print(sorted_adocs[0].document)
